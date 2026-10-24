---
title: "DeepSeek exposed a fundamental AI scaling myth"
subtitle: "If scale is the answer, what is the question?"
author: "Danyal Akarca"
date: "29th January 2025"
article_id: "3063"
channel: "Science"
themes: "Technology & Environment"
tags: "None"
word_count: "2,040 words"
read_time: "Read time: approx. 10 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/if-scale-is-the-answer-what-is-the-question-danyal-akarca.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/deepseek-exposed-a-fundamental-ai-scaling-myth-auid-3063"
---

# DeepSeek exposed a fundamental AI scaling myth

*If scale is the answer, what is the question?*

**By Danyal Akarca** | *29th January 2025* | *Read time: approx. 10 mins* | *2,040 words*

![DeepSeek exposed a fundamental AI scaling myth](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/if-scale-is-the-answer-what-is-the-question-danyal-akarca.webp)

---

*Tech CEOs have long argued that for exponential improvements and emergent properties to develop in AI, the increased scale of computing power is all you need. This narrative has led to billions of dollars of investment in semiconductors. But in recent weeks, Chinese AI company DeepSeek claims to have produced models akin to OpenAI with a fraction of the compute and cost. Was the Tech CEO narrative about scale simply self-serving all along, and at its core, little more than a money grab? Dr Danyal Akarca here argues that scale is not sufficient to take AI to the new heights we have been promised.*

It is hard to express the extent to which the last year has seen a seismic shift in AI, reshaping both the capabilities of these systems and the world’s perception of what is possible. With perhaps some exceptions, it is fair to say these systems have exceeded many lofty expectations. Public opinion and understanding are evolving at rapid pace. [Governments are priming themselves for a new future](https://www.gov.uk/government/news/prime-minister-sets-out-blueprint-to-turbocharge-ai).

\_\_\_

I believe that the core motif at the centre of this rapid recalibration of perception is our understanding of scale: what to scale, why scale and how to scale intelligence.

\_\_\_

At the same time, the economic landscape surrounding the building and deployment of AI is increasingly murky. As I write, NVIDIA is recovering from a [17% decrease in their market valuation](https://finance.yahoo.com/news/nvidia-stock-begins-recovery-after-deepseek-ai-frenzy-prompted-near-600-billion-loss-134240328.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMp2tpxFJeaTPVOiYMsOPE1XcpLmP0QTElnh71dwwVyPRuXzFl6KRY3z4r65j3fqI3b4NVrdlbNECQqAE237fNTVC_DEY3rhQHxYjJ6SdUG2xBaiYJQnecCHYkaAM9CjUTX7v89y6AhUTPwvahTNyyw-BVwLL4Qq73ekEnv0oAR5)—worth just shy of $600 billion—triggered by the (delayed) realisation that DeepSeek’s, China’s most famous AI company, breakthrough model reported required orders of magnitude less capital to build. This is the [largest single-day drop by any US listed company in history](https://www.wsj.com/livecoverage/stock-market-today-dow-sp500-nasdaq-live-01-27-2025/card/nvidia-stock-is-down-more-than-10-here-s-why--sZmsM8tvQFTS3iUBASHa). Commentators are now questioning the central economic assumptions about the cost of intelligence.

I believe that the core motif at the centre of this rapid recalibration of perception is our understanding of *scale*: *what* to scale, *why* scale and *how* to scale intelligence. I think it is increasingly clear that our relationship with what scaling means will effectively come to define the current era of AI acceleration.

[![related-video-image](https://iai.tv/assets/Uploads/ai-and-the-end-of-humanity.webp)

SUGGESTED VIEWING
AI and the end of humanity 
With Liv Boeree, Güneş Taylor, Joscha Bach, Eliezer Yudkowsky, Scott Aaronson](https://iai.tv/video/ai-and-the-end-of-humanity)

**Acing the Bitter Lesson**

We now know that there is no intelligence without – at least some necessary level of – scale. This was Richard Sutton’s [*Bitter Lesson*](http://www.incompleteideas.net/IncIdeas/BitterLesson.html): the most significant and lasting progress in AI will come from methods leveraging computation and general-purpose learning, not human-crafted solutions (as what used to be the dominant view). This lesson has been shown to be unanimously powerful. Indeed, the fundamental paradigm of intelligence today is fuelled by this core belief – scaling the *right* architecture with enough compute and data will deliver intelligence on tap. Our global society is currently going through one of the [largest capital allocation projects in history](https://www.forbes.com/sites/bethkindig/2024/11/14/ai-spending-to-exceed-a-quarter-trillion-next-year/) to fuel this vision *ad infinitum*.

This prompts some very fundamental questions about the future of our society. But here I will not focus on the broad implications for society. In the spirit of the current pandemonium due to the disruption caused by DeepSeek, I am going to focus on what it means for progress in AI moving forward.

**Emergence with scale**

*If scale is the answer, what is the question?* Most answers I hear centre around the eventual *emergence of general intelligence*. Before getting into the plausibility of that, let’s revisit scaling. Scaling can take many forms. It really becomes a matter of *what to scale, when to scale* and *why*. Traditionally, scaling is thought in context of *training*, where a relationship forms between the amount of compute (commonly denominated in floating-point operations, FLOPs), training data size (e.g., the Internet), training time (e.g., order of days to months) and the number of model parameters (i.e., model weights in the order of billions). Empirical studies have shown that model performance often scales as a power-law with proposed [optimality conditions to scale these models given a compute-budget](https://arxiv.org/abs/2203.15556).

[![related-video-image](https://iai.tv/assets/Uploads/H24STUDIO-Joscha-Bach-new-thumbnail.webp)

SUGGESTED VIEWING
Consciousness, AI, and the pattern of reality, with Joscha Bach
With Joscha Bach, Ricky Williamson](https://iai.tv/video/consciousness-ai-and-the-pattern-of-reality-with-joscha-bach)

This is *training*, where you are investing resources to build the model weights as to be able to do something useful. But for *inference*, which relates to putting the model to work, has its own associated scaling laws. As you can imagine, training and inference serve different purposes and thus their performance is constrained by distinct factors which better relate to the allocation of computational resources at *use time* (i.e., where there are potentially millions of customers who need the answers to their prompts). These include factors such as latency, throughput, computational cost, model size, hardware efficiency, batch sizes, weight quantisation and so forth. In some cases, simply increasing the resources available during inference allows for large models to tackle a broader variety of tasks, handle more complex queries, and demonstrate more robust performance without necessarily altering the underlying model weights.

\_\_\_

The central promise of scaling, in the various ways outlined above, is that intelligence emerges from a sufficiently large and richly trained model that has been given sufficient resources to perform inference.

\_\_\_

One of the key reasons “bigger is better” in neural networks has gained so much traction is the now robust body of empirical work demonstrating that performance on a variety of benchmarks often improves in predictable ways as these above critical resources increase. Importantly, scaling laws serve a further purpose quite distinct to the improvement in abilities afforded to the models by scale: they provide measures of *predictable* gains, which is ultimately what is needed to orient significant investment. Only with this predictability comes *belief* in spending millions of dollars on model training runs.

The central promise of scaling, in the various ways outlined above, is that intelligence *emerges* from a sufficiently large and richly trained model that has been given sufficient resources to perform inference. Qualitative leaps in ability—often unpredictable and unplanned—should emerge naturally once models pass some threshold, fuelling the belief that general intelligence (or at least something approaching it, *whatever it may be*) may simply be a matter of continuing along the current trajectory of bigger models, more data, and more compute. On the face of it, it is obviously true that models that scale well will do better with more resources.

[![related-video-image](https://iai.tv/assets/Uploads/The-values-of-AI.webp)

SUGGESTED VIEWING
The values of AI
With Ruth Chang](https://iai.tv/video/the-values-of-ai-ruth-chang)

But are these abilities *truly general*, or *just* high-dimensional curve fitting? This may seem academic and not matter for many current applications, but there is no clear consensus yet that the most crucial aspects of what *most people tend to consider as intelligence*—robust generalisation beyond exposure, causal reasoning, and creative exploration—will emerge from scale alone under the current architectural features of transformer-based architectures. One belief is that it is likely these capabilities would be better attained by hybrid novel architectures, with more structured forms of knowledge representation, intrinsic energetic-awareness and – in the limit – quite fundamentally different approaches to computation itself. Let’s delve into some of this.

**Intelligence primitives beyond attention**

One of the beautiful features of scaling is that it allows one to fully grasp the bottlenecks of a particular approach. Like a game of *Wack-a-mole*, as you scale to solve one problem, another will pop up once the later problem is solved. This in practice is what has led to the new instantiations of the various flavours of scaling laws as outlined above – new plateaus are met with new ways to fuel models. Had we chosen an alternate path—emphasising another scalable architecture from the start—we could now be wrestling with different limitations altogether. This in many ways is akin to evolutionary processes: we build the future on the foundations of the past.

Attention mechanisms within transformers were so remarkable because they allowed models to dynamically focus on the most relevant parts of input data, enabling them to capture long-range dependencies and contextual relationships more effectively than previously possible. The design was inherently trainable and highly parallelisable and could scale efficiently on modern hardware. *It was the core algorithmic ingredient to enable scaling at all.* This all prompts an obvious question: will new *algorithms* matter again? It is already becoming clear that, for sophisticated benchmark problems such as the successful [ARC-AGI challenge](https://arcprize.org/arc) (Abstraction and Reasoning Corpus), it already is. ARC-AGI wasdesigned to test conceptual generalisation, pattern recognition, and abstraction at a level akin to human problem-solving. It requires models to deduce underlying “rules” that govern transformations from small numbers of examples of inputs to outputs, rather than pattern-matching. As outlined by the [technical report](https://arxiv.org/abs/2412.04604), published in December 2024, ramping up parameter counts by orders of magnitude (e.g., 10,000-fold increases) did little to improve performance. Instead, algorithmic approaches such as discrete programme search, and chain-of-thought reasoning proved much more effective at uncovering and applying latent rules. Inductive (i.e., explicitly writing functions in a domain-specific-language that can be used to solve unseen related problems) and transductive (i.e., straight prediction from inputs) approaches using large models [were particularly effective](https://arxiv.org/abs/2411.02272#:~:text=We%20find%20inductive%20and%20transductive,succeeds%20on%20fuzzier%20perceptual%20concepts) and were analogised to mirroring [the System 1 and System 2 type cognition](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow) popularised by Tversky and Kahneman.

\_\_\_

It become equally clear that scale is necessary and not sufficient.

\_\_\_

This all speaks to the core idea that scale will clearly produce intelligent behaviour within the milieu of its training and inference environment. But only by diversifying the types of problems we care for these systems to solve will it become equally clear that scale is necessary and not sufficient. I think that algorithms will, perhaps counterintuitively at first, matter much *more* when we heighten our standards for what constitutes the totality of general intelligence.

**At the confluence of algorithms and hardware**

The magic happens at the confluence of the right objective, algorithm and hardware. We have recently been reminded of this fact by DeepSeek, who through constrained access to hardware managed to smartly engineer their cluster and training run (which you can see here for a [basic overview](https://www.youtube.com/watch?v=kv8frWeKoeo&t=259s), or read the [primary material](https://arxiv.org/abs/2412.19437) for v3) to produce a highly economical and performant model. If there was an existence proof that scale is *not* all you need, you have it there. What it should really underscore is that the search space for intelligence is vast, and a fixation on scale at the expense of all other optimisations has the downside that it will likely dilute our ambitions for what is possible.

\_\_\_

While in the current AI paradigm, performance has generally been the only proxy for success, this is not true for our primary existence proof for general intelligence in the real world: Humans.

\_\_\_

Taking a reasonable step back, it is useful to note there is no universally ‘good’ processing system (admittedly, with “*universally”* doing a reasonable amount of work there). Any one system’s advantage over another generally emerges from how well it aligns with its required task(s) given imposed constraint(s) and context(s). This is particularly apparent when any one system can be assessed across any number of dimensions in isolation or combination: performance, energy consumption, adaptability, cost, ease of integration, reliability. While in the current AI paradigm, performance has generally been the only proxy for success, this is not true for our primary existence proof for general intelligence in the real world: Humans. Evolution has selected at least one example – humans – exhibiting higher order cognitive intelligence, with the ability to learn from wide-ranging data sources, reason about its environment, adapt over time and handle uncertainty robustly. These are great features we wish to increasingly instantiate within our modern AI systems. Associated with these traits in evolving humans were explosive changes to the neural substrate, with the hominization of the human brain being accompanied by much more than just increases or cloning of more neurons (i.e., scaling). It encompassed the creation and expansion of cell type gradients, cortical layer composition and heterogeneous neuronal properties. It was about making a more intelligent and compartmentalised hardware in tandem with the computations. This all speaks to the convergent idea that through sophisticated co-optimisation of hardware and algorithms will we be able to learn much more about the nature of intelligence.

**Conclusions**

Scaling laws, in their many forms, remain a very useful tool. They explain why large-scale models have so far achieved feats once thought near impossible by many—and why continued investment in compute, data, and engineering has the potential to yield further breakthroughs. Yet scale alone is unlikely to deliver a smooth or automatic path to higher-order intelligence.  
  
The discovery and implementation of entirely new principles of intelligence will become particularly fruitful in the years to come. We have seen that current architectures powerfully exploit one core principle: scale through immense parallelism. What other principles exist that can fuel new eras of intelligent systems?
