#!/usr/bin/env python3
"""Build local article data without altering archived Markdown."""
import json,re,shutil,hashlib
from pathlib import Path
import yaml
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
OUT.mkdir(exist_ok=True)
DATA=OUT/'reader-data'; DATA.mkdir(exist_ok=True)
md=MarkdownIt('commonmark',{'html':False,'linkify':False})
EXAMPLE='atheism-cannot-escape-its-religious-origins-auid-3706'
extra={EXAMPLE:{'heroCaption':'Detail from The Ancient of Days setting a Compass to the Earth by William Blake (1794). British Museum.','authorBio':"Senior Fellow at the Shalom Hartman Institute, Senior Research Scholar at the UC Berkeley Center for Middle Eastern Studies, and author of In God's Image: How Western Civilization Was Shaped by a Revolutionary Idea (NYU Press, 2025)."}}
catalog=[]; hashes={}
for entry in json.loads((ROOT/'articles_index.json').read_text()):
 slug=entry['slug']; path=ROOT/'articles'/f'{slug}.md'
 raw=path.read_text(); hashes[slug]=hashlib.sha256(raw.encode()).hexdigest()
 parts=raw.split('---',2); meta=yaml.safe_load(parts[1]); body=parts[2].lstrip()
 meta={k:('' if v is None or v=='None' else str(v)) for k,v in meta.items()}
 # The archive prepends title, subtitle, byline and hero before a divider.
 preamble=re.match(r'^# [\s\S]*?\n---\s*\n',body)
 if preamble: body=body[preamble.end():]
 else:
  body=re.sub(r'^# [^\n]*\n+','',body,count=1)
 # Repair presentation-only artifacts emitted by the old archiver.
 body=re.sub(r'(?m)^\\_\\_\\_\s*$', '---', body)
 body=re.sub(r'(\[!\[[^\]]*\]\([^\n]*\))\n\n([\s\S]*?\]\(https?://[^\s]*\))',lambda m:m[1]+' '+re.sub(r'\s+',' ',m[2]),body)
 intro_source=''
 first_block,separator,remainder=body.partition('\n\n')
 if first_block.startswith('*') and not first_block.startswith('**') and first_block.rstrip().endswith('*'):
  intro_source=re.sub(r'(?<!\*)\*(?!\*)','',first_block)
  body=remainder
 soup=BeautifulSoup(md.render(body),'html.parser')
 for a in soup.find_all('a'):
  href=a.get('href','')
  if not (href.startswith(('https://','http://','#','mailto:'))):a.unwrap();continue
  a['target']='_blank';a['rel']='noopener noreferrer'
 for img in soup.find_all('img'):
  img['loading']='lazy';img['decoding']='async'
 intro=md.render(intro_source) if intro_source else ''
 item={'slug':slug,'title':meta.get('title',entry['title']),'subtitle':meta.get('subtitle',''),'author':meta.get('author',''),'publicationDate':meta.get('date',''),'heroImage':meta.get('header_image',''),'channel':meta.get('channel',''),'themes':meta.get('themes',''),'wordCount':meta.get('word_count',''),'readingTime':meta.get('read_time',''),'sourceUrl':meta.get('source_url',''),'introduction':intro,'body':str(soup),**extra.get(slug,{})}
 (DATA/f'{slug}.json').write_text(json.dumps(item,ensure_ascii=False,separators=(',',':')))
 catalog.append({k:item[k] for k in ['slug','title','subtitle','author','publicationDate','heroImage','channel','themes'] }|{'id':entry['id'],'isNew':entry.get('is_new',False)})
(DATA/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,separators=(',',':')))
if (ROOT/'iai_videos.json').exists():
 shutil.copy2(ROOT/'iai_videos.json', DATA/'videos_index.json')
for name in ['index.html','reader.js','videos.html','.nojekyll'] : 
 if (ROOT/name).exists(): shutil.copy2(ROOT/name,OUT/name)
(OUT/'css').mkdir(exist_ok=True);shutil.copy2(ROOT/'css/reader.css',OUT/'css/reader.css')
shutil.copytree(ROOT/'images',OUT/'images',dirs_exist_ok=True)
assert len(catalog)==len(hashes)>=2180
print(f'Built {len(catalog)} article JSON files; source Markdown unchanged; {len([a for a in catalog if a["heroImage"]])} hero images.')
