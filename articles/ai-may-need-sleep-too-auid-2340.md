---
title: "AI may need sleep too"
subtitle: "How sleep-like phases can prevent catastrophic forgetting"
author: "Darcy Bounsall"
date: "22nd December 2022"
article_id: "2340"
channel: "Science"
themes: "Technology & Environment"
tags: "None"
word_count: "1,137 words"
read_time: "Read time: approx. 6 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/AI-needs-to-sleep-min.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/ai-may-need-sleep-too-auid-2340"
---

# AI may need sleep too

*How sleep-like phases can prevent catastrophic forgetting*

**By Darcy Bounsall** | *22nd December 2022* | *Read time: approx. 6 mins* | *1,137 words*

![AI may need sleep too](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/AI-needs-to-sleep-min.webp)

---

*Drawing inspiration from the natural rhythms of the human brain, researchers are exploring how periods of "sleep" could enhance artificial intelligence learning capabilities and prevent the problem of catastrophic forgetting, writes Darcy Bounsall.*

For around eight hours each night - roughly a third of our lives in total - we exist in a state of unconscious paralysis. Our heartrate and breathing slow, our body temperature falls, and we lie immobile and unresponsive. But as we slowly progress through the stages of sleep something strange begins to happen: our brain activity shoots back up to levels similar to when we’re awake. Unbeknownst to us, as we drift off, our brains are spontaneously reactivating all that we’ve experienced in our waking states.

[![Why AI must learn to forget](https://iai.tv/assets/Uploads/_resampled/FillWyI0MDAiLCIyNzUiXQ/Why-AI-must-learn-to-forget.webp)

SUGGESTED READING
Why AI must learn to forget
By Ali Boyle](https://iai.tv/articles/why-ai-must-learn-to-forget-auid-2302)

There is a vast interdisciplinary literature spanning both psychology and neuroscience that supports the vital role sleep plays in learning and memory. Now a recent study undertaken by Maxim Bazhenov and his colleagues at the University of California San Diego has shown that [artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network) also learn better when combined with periods of off-line reactivation that mimic biological sleep.

\_\_\_

One weakness of many of these AI models is that, unlike humans, they are often only able to learn one self-defined task extremely well.

\_\_\_

Artificial neural networks loosely model the neurons in a biological brain, and are currently one of the most successful machine-learning techniques for solving a variety of tasks, including language translation, image classification, and even [controlling a nuclear fusion reaction.](https://www.wired.co.uk/article/deepmind-ai-nuclear-fusion)

One weakness of many of these AI models is that, unlike humans, they are often only able to learn one self-defined task extremely well. When trying to learn multiple different tasks, they have a tendency to abruptly override previously learned information in a phenomenon known as catastrophic forgetting. In contrast, the brain is able to learn continuously and typically learns best when new training is interleaved with periods of sleep for memory consolidation.

\_\_\_

DeepMind very explicitly cite biology as an inspiration for their own version of sleep when it comes to their artificial neural networks.

\_\_\_

Memories are thought to be represented in the human brain by patterns of what is called synaptic weight — the strength or amplitude of a connection between two neurons. When we learn new information, neurons fire in a specific order which can either increase or decrease synapses between them. When we are asleep, the spiking patterns learned when we were awake are repeated spontaneously in a process called reactivation or replay. This typically happens in the hippocampus, and it’s been best studied with respect to 'place cells' - cells that are only active when the animal or person is in a particular location within an environment. When you carry on recording these neurons when animals go to sleep, you see the same patterns of activity replay.

DeepMind very explicitly cite biology as an inspiration for their own version of this process when it comes to their artificial neural networks. In their Deep [Q-Networks paper,](https://doi.org/10.48550/arXiv.1312.5602) where they first beat Atari games, they 'replayed' previous experiences in a shuffled order. The effect of this is to 'decorrelate' the inputs so that learning generalises more effectively. Normally, you experience events in a particular order - but that's mostly just coincidence. By shuffling the experiences in this way during learning, you can get rid of these spurious correlations.

[![related-video-image](https://iai.tv/assets/Uploads/The-AI-Illusion.webp)

SUGGESTED VIEWING
The AI illusion
With Kate Devlin, Martin Rees, Hilary Lawson, Laura Mersini-Houghton, Stephanie Hare](https://iai.tv/video/the-ai-illusion)

The study used Spiking Neural Networks (SNNs) with reinforcement learning to investigate whether interleaving periods of learning a new task with periods of sleep-like autonomous activity, can avoid catastrophic forgetting. Spiking neural networks are artificial neural networks that were developed to closely emulate the brain. Instead of information being communicated continuously, SNNs crucially incorporate the concept of time into their [operating model](https://en.wikipedia.org/wiki/Operating_Model) and so transmit information as discrete events (spikes) at certain time points.

Bazhenov and his colleagues found that when the spiking networks were trained on a new task, but with occasional off-line periods that mimicked sleep, catastrophic forgetting was mitigated. Much like the human brain, said the study authors, “sleep” for the networks allowed them to replay old memories without explicitly using old training data.

We once thought the brain only changed during the early stages of development and not in adulthood, whereas now we know that the brain is changing constantly. Every trinket of experience causes its structure to change irreversibly. The changing and shaping of connections in our brain - known as synaptic plasticity - occurs both in our waking states and during sleep. During sleep, it further changes our synaptic weight leading to structural changes that allow for long-term memory storage. Much like in humans or animals, the researchers’ use of sleep-like activity optimized the network’s memory representation in synaptic weight space to prevent it forgetting old memories. This meant that the networks could learn continuously, much like humans.

Bazhenov and his colleagues’ research is part of a wider trend that suggests the development of hardware from an AI perspective is becoming more and more ‘brain-like.’ While AI often exercises interpretive power far beyond human understanding, unlike humans, it can often have difficulty carrying experiences from one set of circumstances to another.

\_\_\_

Sleep is critical to ensuring cognitive capabilities work at full pelt, and as such, it seems an excellent candidate for incorporation into artificial neural systems.

\_\_\_

When faced with multiple unfamiliar tasks AI is often useless. This is generally seen as one of the key impediments in the path to developing Artificial General Intelligence (AGI) which is commonly seen as AI that can learn in the same fashion as humans, in an extremely generalisable and adaptive way.

Unlike the brain, which has a genetic code to give it a head start, machine learning applications are incredibly inefficient as they start from a completely blank slate. Compared with biological neurons that use approximately 20 watts of power, about as much as a compact fluorescent lightbulb, a model like GPT-3 uses around 20 megawatts, enough to supply around 20,000 homes. Some see spiking neural networks, which are often referred to as the third generation of neural networks, as a potential breakthrough of the bottlenecks of ANNs as they typically require much lower energy for the operation.

[![All knowing machines are a fantasy](https://iai.tv/assets/Uploads/_resampled/FillWyI0MDAiLCIyNzUiXQ/All-knowing-machines-are-a-fantasy.webp)

SUGGESTED READING
All-knowing machines are a fantasy
By Emily M. Bender](https://iai.tv/articles/all-knowing-machines-are-a-fantasy-auid-2334)

Sleep is critical to ensuring cognitive capabilities work at full pelt, and as such, it seems an excellent candidate for incorporation into artificial systems. Neuroscience in general has historically served as a rich source of inspiration for developing AI. What would be better than emulating an evolutionarily validated template for intelligence? But perhaps in trying to recast the gains of such a process, honed over millions of years, we shouldn’t seek to simply reproduce the gains of our neurobiology but supersede it. Unlike humans - that certainly need their eight hours - the future of AI need not be ringfenced by the boundaries of biology.

**References**

“[Sleep prevents catastrophic forgetting in spiking neural networks by forming a joint synaptic weight representation](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010628)” by Maxim Bazhenov et al. *PLOS Computational Biology*
