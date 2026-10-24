---
title: "The future of AI is analogue"
subtitle: "How neuromorphic computing will solve AI's energy usage problem"
author: "Jonathan Peters"
date: "13th August 2024"
article_id: "2917"
channel: "Science"
themes: "Technology & Environment"
tags: "None"
word_count: "2,421 words"
read_time: "Read time: approx. 12 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/the-future-of-ai-is-neuromorphic2.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/the-future-of-ai-is-analogue-auid-2917"
---

# The future of AI is analogue

*How neuromorphic computing will solve AI's energy usage problem*

**By Jonathan Peters** | *13th August 2024* | *Read time: approx. 12 mins* | *2,421 words*

![The future of AI is analogue](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/the-future-of-ai-is-neuromorphic2.webp)

---

*Much of the talk around AI is hyperbolic, speculative, and often misses the point. In our attempts to recreate our own intelligence using conventional computers we have ended up creating energy inefficient and over engineered systems that rely more on computation scale than “intelligence”. If we want intelligent machines as efficient as our own brains, then we must mimic how it computes. Following recent developments in architecture and learning, Jonathan Peters argues that the future of AI will be analogue.*

The rise to prominence of artificial intelligence (AI) technology is arguably the most important technological change since the turn of the 21st Century. So rapid have the technological advancements been that in a matter of a few years global understanding and perspectives on AI have changed from ignorance to a mixture of intrigue, curiosity, and fear of the unknown future consequences.

When most think of concerns regarding AI technology, the prospect of robot-like technology terrorising humans and taking over the planet will often come to mind. Whilst this is dramatic and highly unlikely in the near future, one concern people should be more informed about is the implications of the technology on the climate. An example of this naivety is clear when looking at the recent [EU ‘artificial intelligence act’](https://eu.boell.org/en/2024/04/08/eu-ai-act-missed-opportunity), dubbed the ‘first of its kind’ in the world, does little to address climate threats. The bill itself asks companies to self-report climate-related statistics, such as consumption, however there is no limits/punishments for extreme energy usage.

Statistics put into perspective just how serious the problem really is. Academic research predicts by 2027, AI alone will be responsible for the same amount of energy expenditure as countries such as the [Netherlands, Croatia and Kenya](https://timesofindia.indiatimes.com/gadgets-news/alarming-ai-numbers-chatgpt-uses-17000-times-more-electricity-than-an-average-us-household-in-a-day/articleshow/108368128.cms).  Other research by the International Energy Agency forecasts energy use from data centres powering AI will be equal to that of [Japan within two years](https://www.bbc.com/news/articles/cj5ll89dy2mo).

Statistics so damning for the environment beg the question of why policy makers are not doing more now, especially with the Paris Climate Agreement in mind. But the answer is simple: there is a lack of knowledge on the subject. AI’s commercial profitability has brought secrecy from the largest players in the industry such as OpenAI, Google and Microsoft. This secrecy is competition driven, although sceptics would also suggest knowledge of such information could damage public interest in the technology, harming long-term business.

\_\_\_

To cause meaningful change in the AI industry, the technology must be attractive... If not as profitable as current technology, large companies responsible for emissions will not adopt novel systems.

\_\_\_

Reading this discussion, some people may argue that the power of the technology to change lives vindicates its extreme power consumption. Whilst the ability of AI to change lives is not disputed, the irony of praising the ability of current AI machines is that our brains are far more efficient AI computers.

[![related-video-image](https://iai.tv/assets/Uploads/23-10-16-consciousness-and-chatgbt-yt.tpu.jpg)

SUGGESTED VIEWING
Consciousness and ChatGPT
With James Tartaglia](https://iai.tv/video/consciousness-and-chat-gpt-james-tartaglia)

As an example, take chatbots: AI models designed to have human interactions online. In computing jargon, these often fall into the category of (large) language models (LLMs), and generative AI, which are notorious for requiring large networks to build successful models. GPT4 (just one LLM) has a daily power usage is equal to roughly [180,000 households in the USA](https://www.forbes.com/sites/cindygordon/2024/03/12/chatgpt-and-generative-ai-innovations-are-creating-sustainability-havoc/), even after the more energy intense training phase is complete. Predictions suggest models will become much larger very quickly (Figure 1), which consequently will rapidly increase the technology’s energy consumption and carbon footprint.

![size increase in llms over timer copy2](assets/Uploads/_resampled/ResizedImageWzkwMCw0NzNd/size-increase-in-llms-over-timer-copy2.jpg)

*Figure 1 Size increase of important Large Language Models (LLMs) over time. Recent models in the past three years have continued the trends demonstrated above of rapid enlargement, increasing their carbon footprints along the way. (Available [here](https://towardsdatascience.com/parameter-counts-in-machine-learning-a312dc4753d0) for a higher quality version)*

The brain’s efficiency is explained through two significant differences when comparing to current computers: first, its architecture, and second the way it learns. Bio-inspired, fundamental changes to computers in these two fields will provide the solution to efficient AI and solve the technology’s intense energy consumption.

\_\_\_

[Conventional] architecture is optimised for performing a small number of precise calculations whereas our brains are optimised to perform many imprecise calculations in parallel, the exact sort of task we are now getting AI to do.

\_\_\_

***Architecture***

Structurally, conventional computers today utilise the von Neumann architecture. Designed in 1945, before the rise of AI, it describes the idea of having separated processing and memory units. Processing units include CPUs and GPUs, whilst memory units include RAM and hard drives. Computation works through ‘shuffling’ data between the two units for every calculation. In contrast, the brain’s architecture is an interconnected system of neurons and synapses, which act as individual processing/memory units for signals in the brain. These structures are copied when creating neural networks.

Summarizing the benefits of each, von Neumann architecture is optimised for performing a small number of precise calculations whereas our brains are optimised to perform many imprecise calculations in parallel, the exact sort of task we are now getting AI to do.

![Sketch of neuronal network structure](assets/Uploads/_resampled/ResizedImageWzkwMCw2MzBd/Sketch-of-neuronal-network-structure.jpg)

*Figure 2 Sketch of the neuronal network structure that is mimicked by artificial neural networks in software. Circles represent network nodes, and links weight the flow of information across the network. ([Source](https://www.the-scientist.com/artificial-neural-networks-learning-by-doing-71687))*

As an example, computers perform arithmetic calculations far quicker than humans do. This is because manipulating a few bits is quicker than the time for signals to flow through the brain’s neuronal network. However, recognising a person is more efficient for the brain, since recognising relations between the pixels at the resolution of our retina requires millions of calculations, both between individual pixels as well as between pixel groups. Brains perform these calculations in parallel through neuronal networks, whilst computers expend vast energy when shuffling information between units for every precise calculation.

Neuromorphic computers are one set of systems that take inspiration directly from neuronal and synaptic structures. Devices can take several forms and use phenomena from a wide range of physics and engineering disciplines to mimic information processing in the brain. The research field’s birth was specific to emulating the integrate-fire spiking patterns of neurons studied in computational neuroscience but has since encompassed many other techniques.

Whilst not mentioned in the rest of this article, it is important to note the research that takes place today into spiking neural networks (SNNs). SNNs are artificial networks, where spike patterns characterize the behaviour of neuronal nodes. Spike pattern then transfer information, as they are dependent on signals from the rest of the network. SNNs often build upon the ideas of Hebbian learning, summarized by the (somewhat) famous phrase ‘neurons that fire together wire together’.

[![related-video-image](https://iai.tv/assets/Uploads/ai-and-the-end-of-humanity.webp)

SUGGESTED VIEWING
AI and the end of humanity 
With Liv Boeree, Güneş Taylor, Joscha Bach, Eliezer Yudkowsky, Scott Aaronson](https://iai.tv/video/ai-and-the-end-of-humanity)

The study of spikes within the brain, from how patterns can be replicated in hardware, to learning synaptic weights through algorithms such as spike-timing dependant plasticity (STDP), are not only fundamental in neuromorphic computing but also represent a shared challenge with neuroscience to understand the brain better. Whilst the potential of SNN’s is extremely high, current research is very theoretical (particularly with respect to learning) and may be too novel to provide fast solutions to the current AI climate crisis.

For neuromorphic computing, on a device level, a strong focus is towards memristor technology. Memristors are resistors that provide a memory function similar to a synapse when information signals flows through them. The particular power of memristors is their non-volatility, as well as having easy read-write functionality (can check or change their current state easily) and a small device footprint (allowing high on-chip information storage density). Additionally, they can be arranged into “crossbar” structures that directly link to the [structure of traditional neural networks](https://www.nature.com/articles/s41563-019-0291-x). Analogous to weights of a neural network modelled in software, this allows us then to manipulate the network when training a model easily.

Memristors are commonplace within current data storage technology, such as SSDs, providing non-volatile random-access memory (RAM). These forms of memristor technology are more ‘mature’, with examples such as phase-change memory (PCM), magnetic random-access memory (MRAM) and ferroelectric memory (FeRAM) available now (Figure 3). Utilising existing technology means one less barrier towards future production. However, the challenge is to use individual devices effectively within network structures, extending their purpose further than just for data storage.

![Schematics of different types of ram copy](assets/Uploads/_resampled/ResizedImageWzkwMCwyNjFd/Schematics-of-different-types-of-ram-copy.jpg)

*Figure 3 Schematics of different types of RAM devices used in network architectures. All change the information propagated by altering their resistance to signal flow, either through material changes (RRAM, PCM), or altering domains (FeRAM, MRAM). ([Source](https://medium.com/@filippomoro.it/memristor-aware-training-for-resilient-neural-networks-769f3d832d9f)).*

Statistics on memristor technology efficiency are very encouraging. Research on memristor-based neural networks have shown more than [90% reduction in energy usage and device footprint](https://www.nature.com/articles/s41928-019-0360-9) (when comparing to equivalent current hardware technology performing the same task). This is a clear indication of not only the technology’s potential, but also the inefficiency of current computers for AI tasks. It is important to note that these statistics are from small physical networks. Scaling up the technology whilst maintaining performance will provide different challenges.

Other devices are also being investigated in research for use in physical networks, though are further away from short-term physical realisations due to their novelty. Examples include the use of organic materials, nanowires, and magnetic textures.

***Learning***

Developments in bio-inspired learning are a consequence of progress in neuromorphic hardware. Abstract circuitry is only useful if we have mechanisms to learn what network configuration solves the required task.

\_\_\_

Wide belief, however, is that backpropagation is biologically implausible, since backward signals carrying information about the error would need to leave the physics of the network unaltered (which is physically impossible).

\_\_\_

In software, the majority of machine learning models utilise the backpropagation algorithm. Backpropagation is incredibly powerful since it gives us (through the chain rule for differentiation) the exact responsibility (the gradient) of every parameter of the network with respect to the network output. Learning is controlled by cost functions, which details how close the model is to finding a perfect solution. The gradient of this function with respect to each parameter then details how to vary the model.

Fast, accurate learning is achieved with backpropagation. Wide belief, however, is that backpropagation is biologically implausible, since backward signals carrying information about the error would need to leave the physics of the network unaltered (which is physically impossible). Software overcomes these challenges by storing the previous network, however as the cost function is dependent on the entire network, finding the gradients for every parameter requires knowledge of the entire network. For large networks, this then involves intensive (and energy-costly) data shuffling for every individual network parameter updates.

There is currently no evidence of such precise error signals in the brain’s network; in fact, information transfer in the brain consists of very noisy signals at low energy. Additionally, learning rules are ‘local’, meaning parameter updates depend on information obtained [within the vicinity of the neuron](https://www.nature.com/articles/s41583-020-0277-3). Implementing such behaviour into algorithms is an important step towards energy efficient training.

Learning algorithms are roughly categorised into two categories; supervised and unsupervised learning, with examples of each found in the brain. Supervised learning changes network parameters using external guidance to assess the quality of the output. Meanwhile, unsupervised algorithms attempt to ‘learn the data’, finding the important features and characteristics itself to classify information. Backpropagation is a supervised learning algorithm, as it relies on a cost function (whose values rely on external data labels) to guide the training of the network model.

Many unsupervised learning models are founded in biology, and are understood via statistical physics. One such example are energy-based models (EBMs). Learning within EBMs manipulates an ‘abstract’ (within software) scalar energy function, whose value depends on the parameters of the network. Learning then assigns lower energies to observed network configurations than unobserved ones. The process is analogous to how real objects often follow the minimums of energy potentials, making an obvious connection to real physics that can be exploited by future analog hardware. Attempts and proof-of-concepts exist to connect the concepts of probabilistic and energy-based learning into hardware that offer a lot of promise (as in [here](https://www.nature.com/articles/s41928-024-01182-4) and [here](https://www.nature.com/articles/s41928-024-01182-4)).

The most important factor though, for energy-efficiency, is to amend learning algorithms to utilise the principle of local learning. Two examples of local algorithms for supervised learning include [Difference Target Propagation (DTP)](https://link.springer.com/chapter/10.1007/978-3-319-23528-8_31) and [Equilibrium Propagation (EP)](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2017.00024/full) (Figure 4). Both link the concepts of local node activity and parameter gradients. Both are capable of [learning on large datasets](https://proceedings.mlr.press/v162/ernoult22a/ernoult22a.pdf) and demonstrated [on physical systems](https://www.nature.com/articles/s41467-024-46879-4), whilst also utilising concepts from statistical physics along the way to integrate the algorithms better with hardware.

EP changes the parameters of the network by comparing node activities for a physical system at two different equilibrium states controlled by the same energy function. One state is minimized with respect to the free energy of the system, whilst the other state is augmented by an additional force on the network proportional to its cost function. DTP is similar that it compares two different node activities, however the state is compared to a target value for every node in the network. This target value is found by learning the inverse function between layers of the forward network. This backward model then relays information from the output to the forward network through the target value.

![Network depictions of ep and dtp3](assets/Uploads/_resampled/ResizedImageWzEwMDAsNTYyXQ/Network-depictions-of-ep-and-dtp3.jpg)

*Figure 4 Network depictions for a) Equilibrium Propagation (EP) and b) Difference Target Propagation (DTP) algorithms. EP allows information to flow in both directions, with the output (y) influenced by an additional force (d) in its second phase. DTP has two separate network paths, where inverse operations (green arrows) create targets at each layer that are used for learning. [See here](https://www.nature.com/articles/s41583-020-0277-3)).*

Attaining future results with these algorithms (and other local learning rules) are critical since they properly address the major data-shuffling problem of global gradient-based learning algorithms.

[![24 01 30 ai needs an embodied brain](https://iai.tv/assets/Uploads/_resampled/FillWyI0MDAiLCIyNzUiXQ/24-01-30-ai-needs-an-embodied-brain.webp)

SUGGESTED READING
AI needs the constraints of the human brain
By Danyal Akarca](https://iai.tv/articles/ai-needs-the-constraints-of-the-human-brain-auid-2728)

***Final Remarks***

Throughout the discussion of both architectures and learning, it is important to keep in mind the overall goal of the research. To cause meaningful change in the AI industry, the technology must be attractive: this means offering performance competitive with current software in all aspects of performance and ease of use. If not as profitable as current technology, large companies responsible for emissions will not adopt novel systems. If the system is better but is very complex to maintain or has a massive physical footprint, the same conclusions apply. Whilst it is easy to delve into theoretical designs that offer promise, future results will be the most important factor to determine the success of current research. If these are satisfied, then adaption away from current digital technology, and embracing the potential of analog, is easy to imagine.

It should also be evident to readers the interconnection between AI technology and neuroscience. Progress in neuroscience research will shape the future of artificial intelligence, as will questions of the ethics of the technology that are not covered in this article. With the climate problems we face today, it is vital we adapt and change to create more sustainable AI technology.
