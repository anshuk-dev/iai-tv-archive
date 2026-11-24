'use strict';
const DEFAULT_SLUG='atheism-cannot-escape-its-religious-origins-auid-3706';
const $=id=>document.getElementById(id);
const escapeHTML=value=>String(value??'').replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const safeURL=value=>{try{const u=new URL(value,location.href);return ['https:','http:'].includes(u.protocol)?u.href:''}catch{return ''}};
const imageURL=a=>a.slug===DEFAULT_SLUG?'images/atheism-origins.webp':safeURL(a.heroImage);
let catalog=[],videoCatalog=[],currentArticle=null,requestNumber=0,page=1,videoPage=1,filtered=[],filteredVideos=[],toastTimer;
const pageSize=18,videoPageSize=18;
const preferences={scale:1,contrast:false,underline:false};
try{Object.assign(preferences,JSON.parse(localStorage.getItem('iai-editorial-preferences')||'{}'));}catch{}
preferences.scale=Math.min(1.5,Math.max(.9,Number(preferences.scale)||1));
function applyPreferences(){document.documentElement.style.setProperty('--reading-scale',preferences.scale);document.body.classList.toggle('high-contrast',!!preferences.contrast);document.body.classList.toggle('underline-links',!!preferences.underline);$('textSize').textContent=`${Math.round(preferences.scale*100)}%`;$('contrastToggle').checked=!!preferences.contrast;$('underlineToggle').checked=!!preferences.underline;$('smallerText').disabled=preferences.scale<=.9;$('largerText').disabled=preferences.scale>=1.5;try{localStorage.setItem('iai-editorial-preferences',JSON.stringify(preferences))}catch{}}
function SiteMenu(open){$('siteMenu').hidden=!open;$('menuButton').setAttribute('aria-expanded',String(open));$('moreButton').setAttribute('aria-expanded',String(open));}
function ShareButtons(){return `<div class="share-buttons" data-component="ShareButtons"><button id="shareArticle" aria-label="Share article"><svg width="19" height="19" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 5V2l8 7-8 7v-4C7 12 4 15 3 20c-1-8 2-14 10-15Z" fill="currentColor"/></svg></button><button id="citeArticle" aria-label="Cite article">cite</button></div>`;}
function ArticleHeader(a){return `<header class="article-header" data-component="ArticleHeader"><h1 id="articleTitle">${escapeHTML(a.title)}</h1>${a.subtitle?`<p class="article-subtitle">${escapeHTML(a.subtitle)}</p>`:''}</header>`;}
function HeroImage(a){const url=imageURL(a);return url?`<figure class="hero-image" data-component="HeroImage"><img src="${escapeHTML(url)}" alt="${escapeHTML(a.heroCaption||a.title)}" width="1280" height="720" fetchpriority="high">${a.heroCaption?`<figcaption class="image-caption" data-component="ImageCaption">${escapeHTML(a.heroCaption)}</figcaption>`:''}</figure>`:'';}
function AuthorBiography(a){return `<p class="author-biography" data-component="AuthorBiography"><strong class="author-name">${escapeHTML(a.author)}</strong>${a.authorBio?`<span> | ${escapeHTML(a.authorBio)}</span>`:''}</p>`;}
function ReadingStats(a){return `<div class="reading-stats" data-component="ReadingStats"><p class="word-count">${escapeHTML(a.wordCount)}</p><p class="reading-time">${escapeHTML(a.readingTime)}</p></div>`;}
function ArticleMetadata(a){return `<section class="article-metadata" aria-label="Article information" data-component="ArticleMetadata"><time class="article-date">${escapeHTML(a.publicationDate)}</time>${ShareButtons()}<hr class="metadata-divider">${AuthorBiography(a)}${ReadingStats(a)}<hr class="intro-divider"></section>`;}
function ArticleIntro(a){return a.introduction?`<div class="article-introduction" data-component="ArticleIntro">${a.introduction}</div>`:'';}
function ArticleBody(a){return `<div class="article-body${a.introduction?'':' no-intro'}" data-component="ArticleBody">${a.body}</div>`;}
async function openArticle(slug){const ticket=++requestNumber;currentArticle=null;$('library').hidden=true;$('videosLibrary').hidden=true;$('article').hidden=false;$('article').innerHTML='<p class="loading" role="status">Loading article…</p>';window.scrollTo(0,0);try{if(!catalog.some(a=>a.slug===slug))throw new Error('This article is not in the library.');const response=await fetch(`reader-data/${encodeURIComponent(slug)}.json`);if(!response.ok)throw new Error('Article text could not be loaded.');const a=await response.json();if(ticket!==requestNumber)return;currentArticle=a;document.title=`${a.title} | IAI — Private Reading Room`;$('article').innerHTML=ArticleHeader(a)+HeroImage(a)+ArticleMetadata(a)+ArticleIntro(a)+ArticleBody(a)+`<footer class="article-end"><a href="#library">← All articles</a><a href="${escapeHTML(safeURL(a.sourceUrl))}" target="_blank" rel="noopener noreferrer">Read on IAI.tv ↗</a></footer>`;$('shareArticle').addEventListener('click',shareArticle);$('citeArticle').addEventListener('click',showCitation);$('article').querySelectorAll('img').forEach(img=>img.addEventListener('error',()=>{img.hidden=true;}));}catch(error){if(ticket!==requestNumber)return;$('article').innerHTML=`<h1 id="articleTitle">Unable to open article</h1><p class="error-message">${escapeHTML(error.message)}</p><a href="#library">Browse the library</a>`;}}

function route(){
  SiteMenu(false);$('readingSettings').hidden=true;$('accessibilityButton').setAttribute('aria-expanded','false');
  const hash=location.hash.slice(1);
  if(hash.startsWith('videos')){
    ++requestNumber;currentArticle=null;
    const params=new URLSearchParams(hash.split('?')[1]||'');
    $('videoSearchInput').value=params.get('search')||'';
    videoPage=1;
    showVideos();
  }else if(hash.startsWith('library')){
    ++requestNumber;currentArticle=null;
    const params=new URLSearchParams(hash.split('?')[1]||'');
    $('searchInput').value=params.get('search')||'';
    page=1;
    showLibrary(params.get('category')||'all');
  }else{
    openArticle(hash.startsWith('article=')?decodeURIComponent(hash.slice(8)):DEFAULT_SLUG);
  }
}

function showLibrary(category){
  $('library').hidden=false;$('videosLibrary').hidden=true;$('article').hidden=true;
  $('library').dataset.category=category;
  document.title=`${category==='all'?'The latest big ideas':category==='new'?'New articles':category} | IAI — Private Reading Room`;
  $('libraryTitle').textContent=category==='all'?'The latest big ideas':category==='new'?'New articles':category;
  filterLibrary();
  window.scrollTo(0,0);
}

function filterLibrary(){
  const query=$('searchInput').value.trim().toLowerCase();
  const category=$('library').dataset.category||'all';
  filtered=catalog.filter(a=>{
    const haystack=[a.title,a.subtitle,a.author,a.themes,a.channel,a.id].join(' ').toLowerCase();
    let matches=category==='all'||(category==='new'&&a.isNew)||[a.channel,a.themes].join(' ').toLowerCase().includes(category.toLowerCase());
    return matches&&(!query||haystack.includes(query));
  });
  const sort=$('sortSelect').value;
  filtered.sort((a,b)=>sort==='oldest'?Number(a.id)-Number(b.id):sort==='title'?a.title.localeCompare(b.title):sort==='author'?a.author.localeCompare(b.author):Number(b.id)-Number(a.id));
  page=Math.max(1,Math.min(page,Math.ceil(filtered.length/pageSize)||1));
  $('resultCount').textContent=`${filtered.length.toLocaleString()} of ${catalog.length.toLocaleString()} articles`;
  renderLibrary();
}

function renderLibrary(){
  const articles=filtered.slice((page-1)*pageSize,page*pageSize);
  $('articleList').innerHTML=articles.length?articles.map(a=>`<article class="library-story"><a href="#article=${encodeURIComponent(a.slug)}">${imageURL(a)?`<img src="${escapeHTML(imageURL(a))}" alt="" width="640" height="360" loading="lazy">`:''}<h2>${escapeHTML(a.title)}</h2>${a.subtitle?`<p class="story-subtitle">${escapeHTML(a.subtitle)}</p>`:''}</a><p class="story-author">${escapeHTML(a.author)}</p><time class="story-date">${escapeHTML(a.publicationDate)}</time></article>`).join(''):`<div class="empty-results"><strong>No articles found.</strong><p>Try another title, author or idea${$('library').dataset.category==='all'?'.':' or browse all articles.'}</p><a href="#library">All articles</a></div>`;
  $('articleList').querySelectorAll('img').forEach(img=>img.addEventListener('error',()=>{img.hidden=true}));
  const total=Math.ceil(filtered.length/pageSize);
  $('pagination').innerHTML='';
  if(total<=1)return;
  const add=(label,target,disabled=false,current=false)=>{
    const b=document.createElement('button');b.textContent=label;b.disabled=disabled;if(current)b.setAttribute('aria-current','page');b.setAttribute('aria-label',typeof label==='number'?`Page ${label}`:label);b.onclick=()=>{page=target;renderLibrary();$('libraryTitle').scrollIntoView();};$('pagination').appendChild(b);
  };
  add('Previous',page-1,page===1);
  let start=Math.max(1,Math.min(page-1,total-2));
  for(let n=start;n<=Math.min(total,start+2);n++)add(n,n,false,n===page);
  add('Next',page+1,page===total);
}

/* ==================== VIDEOS LOGIC ==================== */
async function showVideos(){
  $('library').hidden=true;$('videosLibrary').hidden=false;$('article').hidden=true;
  document.title='Debates & Talks | IAI — Private Archive';
  window.scrollTo(0,0);
  if(videoCatalog.length===0){
    $('videoResultCount').textContent='Loading 2,050 debates…';
    try{
      const r=await fetch('reader-data/videos_index.json');
      if(!r.ok)throw new Error('Video index could not be loaded.');
      videoCatalog=await r.json();
    }catch(err){
      $('videoList').innerHTML=`<div class="empty-results"><strong>Failed to load video catalog</strong><p>${escapeHTML(err.message)}</p></div>`;
      return;
    }
  }
  filterVideos();
}

function filterVideos(){
  const query=$('videoSearchInput').value.trim().toLowerCase();
  filteredVideos=videoCatalog.filter(v=>{
    if(!v.video_url)return false;
    const haystack=[v.title,v.description,v.publication_date].join(' ').toLowerCase();
    return !query||haystack.includes(query);
  });
  const sort=$('videoSortSelect').value;
  filteredVideos.sort((a,b)=>{
    if(sort==='oldest')return (a.publication_date||'').localeCompare(b.publication_date||'');
    if(sort==='duration')return (b.duration_seconds||0)-(a.duration_seconds||0);
    if(sort==='title')return a.title.localeCompare(b.title);
    return (b.publication_date||'').localeCompare(a.publication_date||'');
  });
  videoPage=Math.max(1,Math.min(videoPage,Math.ceil(filteredVideos.length/videoPageSize)||1));
  $('videoResultCount').textContent=`${filteredVideos.length.toLocaleString()} of ${videoCatalog.length.toLocaleString()} debates`;
  renderVideos();
}

function renderVideos(){
  const vids=filteredVideos.slice((videoPage-1)*videoPageSize,videoPage*videoPageSize);
  $('videoList').innerHTML=vids.length?vids.map(v=>`
    <article class="video-card" data-id="${v.id}">
      <div class="video-thumb-wrap">
        <img src="${escapeHTML(v.thumbnail_url)}" alt="${escapeHTML(v.title)}" loading="lazy">
        <div class="video-play-btn"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
        ${v.duration?`<span class="video-duration-badge">${escapeHTML(v.duration)}</span>`:''}
      </div>
      <h2>${escapeHTML(v.title)}</h2>
      ${v.description?`<p class="video-desc-preview">${escapeHTML(v.description)}</p>`:''}
      <div class="video-meta">${escapeHTML(v.publication_date||'')}</div>
    </article>
  `).join(''):`<div class="empty-results"><strong>No debates found.</strong><p>Try searching for different thinkers, topics or keywords.</p></div>`;

  $('videoList').querySelectorAll('.video-card').forEach(card=>{
    card.onclick=()=>{
      const id=Number(card.dataset.id);
      const item=videoCatalog.find(x=>x.id===id);
      if(item)openVideoModal(item);
    };
  });

  const total=Math.ceil(filteredVideos.length/videoPageSize);
  $('videoPagination').innerHTML='';
  if(total<=1)return;
  const add=(label,target,disabled=false,current=false)=>{
    const b=document.createElement('button');b.textContent=label;b.disabled=disabled;if(current)b.setAttribute('aria-current','page');b.onclick=()=>{videoPage=target;renderVideos();$('videosTitle').scrollIntoView();};$('videoPagination').appendChild(b);
  };
  add('Previous',videoPage-1,videoPage===1);
  let start=Math.max(1,Math.min(videoPage-1,total-2));
  for(let n=start;n<=Math.min(total,start+2);n++)add(n,n,false,n===videoPage);
  add('Next',videoPage+1,videoPage===total);
}

function cleanVideoUrl(u){
  if(!u||!u.startsWith('http'))return '';
  if(u.includes('iai.tv/assets/videos/')&&!u.startsWith('https://cdn.iai.tv')){
    u=u.replace(/^https?:\/\/iai\.tv\/assets\/videos\//,'https://cdn.iai.tv/assets/videos/');
  }
  u=u.replace(/#/g,'%23');
  try{return encodeURI(decodeURI(u)).replace(/#/g,'%23')}catch(e){return u}
}

function openVideoModal(v){
  const cleanUrl = cleanVideoUrl(v.video_url);
  $('modalVideoTitle').textContent=v.title;
  $('modalVideoDate').textContent=v.publication_date?`Released: ${v.publication_date}`:'';
  $('modalVideoDuration').textContent=v.duration?`Duration: ${v.duration}`:'';
  $('modalVideoDesc').textContent=v.description||'';
  $('modalVideoDownload').href=cleanUrl;
  $('modalVideoDownload').setAttribute('download',v.filename||'video.mp4');
  const searchName = (v.filename || v.title).replace(/\.mp4$/i, '').trim();
  $('modalVideoDrive').href = `https://drive.google.com/drive/u/0/search?q=${encodeURIComponent(searchName)}`;
  const player=$('mainVideoPlayer');
  player.onerror = () => {
    // Fallback if CDN failed: try direct iai.tv server
    if (player.src.includes('cdn.iai.tv')) {
      player.src = cleanUrl.replace('https://cdn.iai.tv/', 'https://iai.tv/');
    }
  };
  player.src=cleanUrl;
  $('videoDialog').showModal();
  player.play().catch(()=>{});
}

function closeVideoModal(){
  const player=$('mainVideoPlayer');
  player.pause();
  player.src='';
  $('videoDialog').close();
}

$('closeVideoModal').onclick=closeVideoModal;
$('videoDialog').addEventListener('close',closeVideoModal);
$('videoSearchInput').addEventListener('input',()=>{
  videoPage=1;filterVideos();
  const params=new URLSearchParams();
  if($('videoSearchInput').value)params.set('search',$('videoSearchInput').value);
  history.replaceState(null,'',`#videos${params.size?'?'+params:''}`);
});
$('videoSearchForm').onsubmit=e=>{e.preventDefault();videoPage=1;filterVideos();};
$('videoSortSelect').onchange=()=>{videoPage=1;filterVideos();};

/* ==================== GLOBAL LISTENERS ==================== */
function notify(message){$('statusMessage').textContent=message;$('statusMessage').hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>{$('statusMessage').hidden=true;},4000);}
async function copyText(text,success){try{await navigator.clipboard.writeText(text);notify(success)}catch{notify('Copy is unavailable here. Select and copy the text manually.');}}
async function shareArticle(){if(!currentArticle)return;const data={title:currentArticle.title,url:location.href};if(navigator.share){try{await navigator.share(data);return}catch(error){if(error.name==='AbortError')return;}}await copyText(location.href,'Article link copied. Access remains private.');}
function showCitation(){if(!currentArticle)return;const a=currentArticle;$('citationText').textContent=`${a.author}. “${a.title}.” IAI News, ${a.publicationDate}. ${a.sourceUrl}`;$('citationDialog').showModal();}
$('menuButton').onclick=()=>SiteMenu($('siteMenu').hidden);$('moreButton').onclick=()=>SiteMenu($('siteMenu').hidden);
$('searchInput').addEventListener('input',()=>{page=1;filterLibrary();const params=new URLSearchParams();const category=$('library').dataset.category;if(category!=='all')params.set('category',category);if($('searchInput').value)params.set('search',$('searchInput').value);history.replaceState(null,'',`#library${params.size?'?'+params:''}`);});$('searchForm').onsubmit=e=>{e.preventDefault();page=1;filterLibrary()};$('sortSelect').onchange=()=>{page=1;filterLibrary()};
$('accessibilityButton').onclick=()=>{const open=$('readingSettings').hidden;$('readingSettings').hidden=!open;$('accessibilityButton').setAttribute('aria-expanded',String(open));if(open)$('closeSettings').focus();};function closeSettings(){$('readingSettings').hidden=true;$('accessibilityButton').setAttribute('aria-expanded','false');$('accessibilityButton').focus();}$('closeSettings').onclick=closeSettings;$('smallerText').onclick=()=>{preferences.scale=Math.max(.9,Math.round((preferences.scale-.1)*10)/10);applyPreferences()};$('largerText').onclick=()=>{preferences.scale=Math.min(1.5,Math.round((preferences.scale+.1)*10)/10);applyPreferences()};$('contrastToggle').onchange=e=>{preferences.contrast=e.target.checked;applyPreferences()};$('underlineToggle').onchange=e=>{preferences.underline=e.target.checked;applyPreferences()};$('resetSettings').onclick=()=>{Object.assign(preferences,{scale:1,contrast:false,underline:false});applyPreferences()};$('closeCitation').onclick=()=>$('citationDialog').close();$('citationDialog').addEventListener('close',()=>$('citeArticle')?.focus());$('copyCitation').onclick=()=>copyText($('citationText').textContent,'Citation copied.');
document.addEventListener('keydown',e=>{
  if(e.key==='Escape'){
    SiteMenu(false);
    if(!$('readingSettings').hidden)closeSettings();
    if($('videoDialog').open)closeVideoModal();
  }
});
async function init(){
  applyPreferences();
  try{
    const r=await fetch('reader-data/catalog.json');
    if(!r.ok)throw new Error('Library could not be loaded.');
    catalog=await r.json();
    window.addEventListener('hashchange',route);
    route();
  }catch(error){
    $('article').innerHTML=`<h1>Library unavailable</h1><p class="error-message">${escapeHTML(error.message)} Please reload to try again.</p>`;
  }
}
document.querySelector('.skip-link').addEventListener('click',event=>{event.preventDefault();$('main').focus();$('main').scrollIntoView();});
init();
