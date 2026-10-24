---
title: "Computer creativity is a matter of agency"
subtitle: "It isn't just about the novelty and value of AI-generated artwork"
author: "Dustin Stokes"
date: "11th November 2021"
article_id: "1971"
channel: "Arts & Culture"
themes: "Art & Aesthetics"
tags: "None"
word_count: "2,314 words"
read_time: "Read time: approx. 12 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/AI-ART.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/ai-will-never-rival-picasso-auid-1971"
---

# Computer creativity is a matter of agency

*It isn't just about the novelty and value of AI-generated artwork*

**By Dustin Stokes** | *11th November 2021* | *Read time: approx. 12 mins* | *2,314 words*

![Computer creativity is a matter of agency](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/AI-ART.webp)

---

*Even when AI makes beautiful, awe-inspiring new artworks, people are understandably reluctant to call it creative. Why? It's because real creativity is an expression of agency, write Dustin Stokes and Elliot Samuel Paul.*

An up-and-coming visual artist is gaining international fame for making images in response to prompts from curious fans. When asked for “a calm still life in ethereal blue”, the artist replied with this:

![AI 1](assets/Uploads/_resampled/ResizedImageWzYwMCwzMDBd/AI-1.jpg)

[source](https://twitter.com/advadnoun/status/1441518499952664577): [@advadnoun](https://twitter.com/advadnoun) on Twitter

Check out the artist’s rendering of “Studio Ghibli landscape”:

![ai 2](assets/Uploads/ai-2.jpg)

[source](https://twitter.com/ak92501/status/1402134906931720195?s=20): [@ak92501](https://twitter.com/ak92501) on Twitter

The artist is prolific, offering numerous options for any given prompt, including these, inflected through the style of a fellow illustrator, for “a painting of climate change killing humanity, by Greg Rutkowski”:

![ai 4](assets/Uploads/_resampled/ResizedImageWzYwMCwzNDBd/ai-4.jpg)

[source](https://twitter.com/RiversHaveWings/status/1455125825859112967): [@RiversHaveWings](https://twitter.com/RiversHaveWings) on Twitter

“A painting of humanity surviving artificial intelligence, by Greg Rutkowski”:

![ai 6](assets/Uploads/_resampled/ResizedImageWzYwMCwzMzld/ai-6.jpg)

([source](https://twitter.com/RiversHaveWings/status/1455509201233403913): [@RiversHaveWings](https://twitter.com/RiversHaveWings) on Twitter)

Commissioned for an illustrated story called “[Tour of the Sacred Library](https://moultano.wordpress.com/2021/07/20/tour-of-the-sacred-library/),” the artist drummed up an elaborate series of scenes, including these:

![ai5](assets/Uploads/ai5.jpg)

![ai 7](assets/Uploads/ai-7.jpg)

source: [Ryan Moulton](https://moultano.wordpress.com/2021/07/20/tour-of-the-sacred-library/)

If you’re like most people, you recognize these images as having notable aesthetic properties: they are variously intriguing, cool, balanced, trippy, captivating, impressionistic, abstract, lovely, serene, evocative, and more. Furthermore, you probably take these works to be expressions of *creativity*, at first.

But while you may acknowledge the creativity of the human beings involved – the programmers and perhaps the users who crafted the prompts – you may be reluctant to say the program itself is creative. Why?

But here’s the twist: the “artist” behind these artworks is a computer program. It involves a neural network called CLIP and [you](https://www.youtube.com/watch?v=5Zf8kRPJ6TU) [can](https://www.youtube.com/watch?v=LM8dil6n5h8) [try](https://www.youtube.com/watch?v=8hnZmtqi-YE) [it](https://alexasteinbruck.medium.com/vqgan-clip-how-does-it-work-210a5dca5e52) [out](https://docs.google.com/document/d/1Lu7XPRKlNhBQjcKr8k8qRzUzbBW7kzxb5Vu72GMRn2E/edit) [yourself](https://blog.roboflow.com/ai-generated-art/).

Does learning the artist’s identity change your assessment of its work? Presumably you still see its images as having various aesthetic properties: they are still arresting or soothing, lively or mellow, and so on. But while you may acknowledge the creativity of the human beings involved – the programmers and perhaps the users who crafted the prompts – you may be reluctant to say the program itself is creative. Why?

The classic statement of skepticism regarding the possibility of computer creativity goes back to Ada Lovelace in the 19th century. Her friend, Charles Babbage, had published his design for the Analytical Engine, a hypothetical machine that would use punched cards to represent mathematical values, and would implement various “formulae” in what we now call programs to perform calculations. Though Babbage never managed to build this machine, it is widely regarded as the first complete design for a general computer. In 1842, Lovelace wrote an important set of reflections on the Analytical Engine, for which many scholars celebrate her, along with Babbage, as one of the founders of modern computational theory. One of Lovelace’s key insights was that, in theory, the Engine could be programmed to perform functions beyond calculation. But even so, she sounded this precaution:

“It is desirable to guard against the possibility of exaggerated ideas that might arise as to the powers of the Analytical Engine. The Analytical Engine has no pretensions whatever to *originate* anything. It can do *whatever we know how to order it* to perform.” (italics added)

A program can never generate anything *new*, Lovelace says, because it can only yield outputs that are already stored in its memory or coded into its program. We can’t get more out of a program than what its programmer has already put into it.

We can’t get more out of a program than what its programmer has already put into it.

Lovelace was right about the Analytical Engine and about any program that is limited to strict conditional rules of the form, ‘Given input X, deliver output Y’. The very act of coding that kind of rule requires the programmer to specify the inputs and outputs in advance, so the results are always predictable.

But we’ve come a long way since Babbage. The rules coded into CLIP-based systems and other artistic programs are not just conditional; they’re combinatorial – they enable a computer to form new combinations out of the elements it stores or receives. Further, as the philosopher [Margaret Boden](https://ojs.aaai.org/index.php/aimagazine/article/view/2254) emphasizes, these programs also include meta-rules – rules for altering their own combinatorial rules – so what they develop over time are not just new combinations, but new waysof forming combinations, enabling results that were “downright impossible” in the program’s initial state.

Things get even more impressive when we peer under the hood. Our featured program is actually a combination of two neural networks: a GAN which generates images, and CLIP which uses natural language to steer the generative process.

A GAN (Generative Adversarial Network), such as BigGAN or [VQ-GAN](https://compvis.github.io/taming-transformers/), uses a codebook, developed through machine learning, which identifies patterns of coloured pixels as features or objects like hat, blue, face, rain, city, etc. This codebook is used by two components of a GAN: a *generator* which produces new images, and a *discriminator* which scores how realistic they are. The process is then repeated through feedback loops, incrementally improving the score. The results are so convincing that they are being exploited in ‘[Deepfakes](https://theaisummer.com/deepfakes/)’, synthesized products that look just like photos or videos of real people. On its own, a GAN only works with images, not natural language, so that’s where CLIP comes in.

If it has never seen a zebra, for example, it can still recognize a zebra the first time it sees one, given that it has seen horses and knows that a zebra looks like a striped horse.

[CLIP](https://openai.com/blog/clip/) ([Contrastive Image-Language Pretraining](https://cdn.openai.com/papers/Learning_Transferable_Visual_Models_From_Natural_Language_Supervision.pdf)) is able to classify images with ordinary words. Earlier efforts of this kind required tremendous amounts of manual labour; [ImageNet](https://image-net.org/update-mar-11-2021.php) employed over 25,000 people to label 14 million images using 22,000 categories. Instead, CLIP is trained by machine learning on over 400 million text-image pairs already available in the massive, messy dataset of the internet. It has remarkable ‘zero-shot’ capabilities, meaning that it can classify objects in categories it has never been trained on. If it has never seen a zebra, for example, it can still recognize a zebra the first time it sees one, given that it has seen horses and knows that a zebra looks like a striped horse.

Brilliant hackers like [Katherine Crowson](https://twitter.com/RiversHaveWings/status/1455125825859112967) and [Ryan Murdoch](https://twitter.com/advadnoun) figured out how to pair CLIP with a GAN, so it runs in reverse, from text to image. Given a description in natural language, CLIP guides a search through GAN’s generative possibilities, and it evaluates combinations of visual features, scoring them for how well they fit the description. The system displays the highest scoring combination at the end of each trial, and it goes through multiple trials to improve the score. Roughly, the GAN and CLIP respectively implement what some psychologists identify as the two main processes in human creativity: generating and evaluating new ideas.

Compare how you create. What would do for, say, “an abstract painting of a planet ruled by little castles”? Pause for a moment and actually try to come up with a painting in your mind.

If you’re anything like us, you begin by searching your mental storehouse for images you associate with words from the prompt – associations you acquired from the massive, messy dataset of your experience. You try to combine images to fit the overall description. You evaluate the results. And you repeat the process with variations to improve the outcome. That is basically what the program did with the very same prompt, but with a more satisfying outcome than most of us can manage:

![ai 8](assets/Uploads/ai-8.jpg)

[source](https://twitter.com/RiversHaveWings/status/1386755619164622848?s=20): [@RiversHaveWings](https://twitter.com/RiversHaveWings) on Twitter

Those who made and use this technology [marvel](https://ml.berkeley.edu/blog/posts/clip-art/) in unison, “[I could never have produced anything close to these images on my own](https://moultano.wordpress.com/2021/07/20/tour-of-the-sacred-library/).”

Systems like these are too many to name and new ones are being developed at a dizzying pace.

CLIP-based programs are just the tip of the iceberg when it comes to computer-generated novelty. *AlphaGo*is a program that defeated the world champion Go player, Lee Sodol, and by Sodol’s own report, AlphaGo’s style of play was surprising and novel. David Cope’s ‘[EMI](http://artsites.ucsc.edu/faculty/cope/)’ (Experiments in Musical Intelligence) composes musical works in the styles of Bach, Stravinsky, and other composers, and some of them have been adopted by actual record labels (e.g. see ‘[Emily Howell](http://artsites.ucsc.edu/faculty/cope/Emily-howell.htm)’ on Spotify or Apple Music). Simon Colton’s [*Painting Fool*](http://www.thepaintingfool.com/galleries/amelies_progress/index.html)is a system that produces portraits with varying emotional expressions based on images of film characters. Other systems are discovering new [mathematics](https://www.vice.com/en/article/xgzkek/machines-are-inventing-new-math-weve-never-seen). Systems like these are too many to name and new ones are being developed at a dizzying pace.

Despite Lovelace’s objection, these programs produce things that are astonishingly new. We can and do get more out of them than what their programmers have put into them.

Nevertheless, you might still be reluctant to call a computer creative. To clarify the matter, compare the issue of whether computers can think.

In 1950, [Alan Turing](https://theconversation.com/imitation-game-brings-to-life-the-real-alan-turing-pioneer-of-the-computer-age-32517) proposed “the imitation game”, now called “the Turing test”, for determining whether a computer is thinking. The test involves an interrogator who uses a keyboard to engage in an open-ended conversation with two unseen interlocutors: one of them is another human being, while the other is a computer. Turing postulated that if the computer answers questions in such a way as to trick the interrogator into thinking that it’s human, this would suffice to show that the computer is thinking. Turing predicted that computers would pass the test by the turn of the century, but most experts agree that none have succeeded even to this day.

Even so, Turing was also posing a philosophical question: If one day a computer finally manages to converse so fluently that we cannot distinguish it from a human interlocutor, would it actually be thinking, as Turing proposed? Or would it merely be behaving *as if* it were thinking?

Inspired by Turing, we might consider an analogous test for whether a computer is creative: Does it produce works that are so original and impressive that it reliably tricks us into thinking that it’s a human creator? To some extent, computers are already fooling us on this score.

In one dramatic example from 1997, a concert audience was informed that the three works being performed by the pianist that evening were written by three different composers: one was an original Bach, one was by a music professor, and one was by a program we mentioned earlier, EMI. The audience was tasked with guessing which of these pieces was the real Bach, and, remarkably, the composition they chose wasn’t the one by Bach. It wasn’t by the other human composer either. The winner was EMI.

More generally, unwitting observers are routinely amazed to learn that artworks they are admiring or compositions they are enjoying are in fact the handiworks of a machine. You may have had that reaction yourself with the artworks we viewed at the beginning.

Real creativity is an expression of agency.

Which brings us back to our philosophical question: Are these programs actually creative? Or are they merely behaving *as if* they are creative?

According to the standard definition, creativity is the ability to produce things that are new and valuable. If this were all there is to being creative, the programs we’re considering would definitely be creative.

But creativity requires something more. Water molecules crystallizing in cold air form a unique and intricate snowflake. Wind blows sand into a novel and tranquil pattern of dunes across a desert plain. Atmospheric gases scatter sunlight over the horizon in a distinctive and stunning array of red-orange hues. In each case, the result is something new and aesthetically valuable. But water, wind, and gases are not creative. They’re not creative because they’re not *agents* who bear responsibility for what they bring about. Thus, as philosophers like [Berys Gaut](https://onlinelibrary.wiley.com/doi/10.1111/j.1747-9991.2010.00351.x) have argued, the production of valuable novelty may be necessary for creativity, but it isn’t sufficient. Real creativity is an expression of agency.

This leaves open the question of exactly how agency must be exercised in creative acts. One proposal is that the act has to be intentional. Suppose you are snowboarding on a powder day and, unbeknownst to you, the tracks from your board happen to trace out a pleasing profile of a face in the mountain as viewed from above. The pattern is new and has aesthetic value, but you weren’t creative in making it. That’s because it was a lucky coincidence that you didn’t know about or intend. Underlying the assessments of this case and of the natural phenomena above is the fact that “creative” is a term of praise, and we do not extend praise (or blame) for things that are not done by an agent, or for things that an agent does accidentally rather than intentionally. Real creativity requires intentional agency.

This would explain our residual hesitation to call CLIP and other programs creative. The problem isn’t that they can’t produce things that are valuable and new – they clearly do. But the question that remains is this: Are these systems genuine agents?

Well, they aren’t *moral* agents. If a program were to do something offensive, we don’t hold the program morally responsible. If anyone is morally responsible, it’s the human programmers or users, not the program itself.

These programs aren’t *legal* agents, either. No one is seriously proposing that legal credit – ownership, patents, copyright – should go to a program itself, independently of the programmers who designed it, hackers who may have modified it, or end-users who run it with their own prompts or other specifications.

We are not claiming definitively that these programs aren't creative. Maybe creative agency requires something less than moral or legal agency, and maybe these programs have what it takes. Someone might make that argument.

Still, it *isn't obvious* that these programs are actually creative – even when it’s obvious that their outputs are valuable and new – and our aim has been to explain why not. The reason it isn't clear that these programs are really creative is because it isn't clear that they are really agents. It all boils down to the tricky question of what kind of agency is required for creativity and whether computers can be agents in that way.

We can enjoy their products regardless. But if we’re curious about whether computers could really be creative, agency, it seems, is the final frontier.
