---
title: "Cutting-edge science has moved beyond Occam's Razor"
subtitle: "Simplicity is no longer a guide for frontier science"
author: "Eric B. Winsberg"
date: "3rd July 2026"
article_id: "3613"
channel: "Philosophy"
themes: "Knowledge, Science & Method"
tags: "None"
word_count: "1,716 words"
read_time: "Read time: approx. 9 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/cutting-edge-science-has-moved-beyond-Occams-Razor.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/cutting-edge-science-has-moved-beyond-occams-razor-auid-3613"
---

# Cutting-edge science has moved beyond Occam's Razor

*Simplicity is no longer a guide for frontier science*

**By Eric B. Winsberg** | *3rd July 2026* | *Read time: approx. 9 mins* | *1,716 words*

![Cutting-edge science has moved beyond Occam's Razor](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/cutting-edge-science-has-moved-beyond-Occams-Razor.webp)

---

*For centuries, scientific progress meant taming complexity with simple, unified theories, guided by Occam’s Razor. Newton and Einstein captured vast, intricate systems in just a handful of elegant equations. But philosopher **Eric B. Winsberg**, a leading voice on the use of computer simulations in science, argues we’ve entered a revolutionary new scientific age, in which progress no longer requires crafting simple theories. Breakthroughs are being powered by machine learning systems like AlphaFold, which solve previously intractable problems like protein folding using vast datasets, and no simple, elegant theory at all. While there may be regions of reality in which traditional scientific theorizing is helpful, there’s no reason to insist that this applies to reality in its entirety.*

If you walk through Cambridge on a rare sunny day you can go straight from Trinity College, where Isaac Newton formulated the laws that govern the motion of everything from cannonballs to comets, to the Biomedical Campus, where the science of protein structure was born. Three centuries apart, these are both triumphs of prediction. Yet they are triumphs of a very different kind. The difference tells us something important about how AI is reshaping science. In particular, it is reshaping what we value in science.

**Newton and the classical ideal**

Newton set a high bar when it comes to producing simple, elegant, unifying theories. You start with just three laws of motion and one law of universal gravitation. From only these four equations you can derive the orbits of the planets, the trajectory of a thrown ball, and the rhythm of the tides.

This is the paradigm case of what philosophers of science call theoretical virtues: [simplicity, elegance, explanatory power, unification](https://iai.tv/video/the-elegant-universe). A handful of principles, and the heavens fall into order. For centuries, these theoretical virtues were treated as more than just things we happen to like for aesthetic reasons. They were taken to be guides to truth. [Occam’s Razor](https://iai.tv/video/how-occams-razor-changed-the-world-johnjoe-mcfadden) is the oldest formulation of this instinct. Eugene Wigner’s famous 1960 essay on “[The unreasonable effectiveness of mathematics in the natural sciences](https://web.njit.edu/~akansu/PAPERS/The%20Unreasonable%20Effectiveness%20of%20Mathematics%20(EP%20Wigner).pdf)” was another expression of this point. The tacit assumption was that the right theory will be simple because nature is fundamentally simple. [If your equations are ugly](https://iai.tv/articles/the-pursuit-of-beautiful-theories-has-become-an-obstacle-to-genuine-discovery-auid-3552), they are likely not the right equations.

**AlphaFold, simplicity, complexity, and biology**

Protein folding is a problem that refuses to bend to this method. A protein is made up of a chain of amino acids. The exact sequence of amino acids in the chain determines the shape the protein will crumple into. The shape of the protein, in turn, determines everything about what it will do in the body—what biological functions it will perform, what it will bind to, what it will catalyze, etc. Predicting the shape from the sequence alone was one of the hardest problems in biology for over 50 years. This is sometimes referred to as [Levinthal’s Paradox](https://web.archive.org/web/20041209175844/http:/www.sdsc.edu/~nair/levinthal.html): even a small protein has so many possible configurations that an exhaustive search would take longer than the age of the universe to complete. But there is no tidy set of laws that maps sequence to structure. Part of the reason is what physicists call scale separation. Newton could write simple laws for planets and cannonballs because at those scales the fine-grained details wash out: you can predict a planet’s orbit without tracking its individual atoms. Protein folding affords no such luxury—the shape of the whole molecule depends on the interactions of individual atoms, hydrogen bonds, electrostatic effects, and solvent forces, all operating at roughly the same scale and all mattering at once.

\_\_\_

If Newton gave us a cathedral built from four axioms, AlphaFold gave us a cathedral built from 93 million fitted stones, and nobody can quite tell you why each stone sits where it does.

\_\_\_

When AlphaFold 2 was unveiled at the CASP14 competition in 2020, [it obliterated all expectations](https://iai.tv/articles/ai-can-uncover-humanitys-unknown-unknowns-auid-3083), and the competition’s organizers declared the protein folding problem effectively solved. The scientific world was blown away. But consider what the solution looks like. AlphaFold 2 is a system of roughly 93 million trainable parameters that predicts three-dimensional atomic coordinates. It is extraordinarily complex by the standards philosophers and scientists usually have in mind when they talk about theoretical simplicity.

And by the classical scorecard of theoretical virtues, it fails on every count. It is not simple. It is not elegant. And it does not explain why a protein folds the way it does—it predicts the shape without delivering understanding. If Newton gave us a cathedral built from four axioms, AlphaFold gave us a cathedral built from 93 million fitted stones, and nobody can quite tell you why each stone sits where it does.

**A new kind of simplicity**

This is where things get interesting. AlphaFold is not simple in the way Newton’s laws are. But the recipe that researchers use for training AlphaFold is really incredibly simple—and each version of AlphaFold was built using a much simpler recipe than the last one.

AlphaFold 1, which debuted in 2018, was a multi-step pipeline. Deep convolutional neural networks predicted distance distributions between pairs of amino acids. A separate physics-based system—the Rosetta software—refined the resulting structures through energy minimization. It was a Rube Goldberg machine of clever parts. Each part required its maker to have his or her own domain expertise to build it and tune it.

AlphaFold 2 replaced this with what is called “end-to-end” architecture. There is no more back and forth between statistics and physics. But even in AlphaFold 2 the architecture itself was highly specific to protein folding, and indeed to specific aspects of protein folding on a case by case basis. Each component of the model was a custom-designed piece of engineering, designed specifically for the geometry of the protein folding problem.

AlphaFold 3, which was released in 2024, simplified things even further. They stopped relying on the specialized Structure Module and used a diffusion model. The bespoke Evoformer was streamlined into a leaner module called the Pairformer. And the tool is becoming more and more powerful: it now handles not just proteins but DNA, RNA, small-molecule drugs, and metal ions. It does this all within a single unified framework.

With each generation, the scientists use less domain-specific engineering. What remains is an increasingly general recipe. Take a large neural network, feed it a large dataset, and then train the neural network on the data. “Reward” it every time it gets the data right; “punish” it every time it gets it wrong. The AI researcher Rich Sutton named this pattern the bitter lesson: general methods that leverage more data and more computation consistently outperform systems built on painstakingly hand-crafted human knowledge. It is a bitter lesson because it means that your domain-specific cleverness is useless compared to sheer computational reach.

This same recipe is now solving protein folding, generating fluent prose, predicting weather systems, and playing superhuman chess. The simplicity is still there. It is still a feature of science. But it has moved from the scientific model to the method for constructing scientific models.

**Simplicity and truth**

Should we, then, abandon simplicity and elegance as guides to scientific truth? I do not think so. But I think we need to revise our understanding of where to look for them.

Newton’s achievement was a simple theory of a domain that happened to be, in a deep mathematical sense, tractable. Gravitational interactions between two bodies yield exact, closed-form solutions. Add more bodies and just a bit of computational power can give you very good predictions. The simplicity of Newton’s laws was, in part, a feature of the fit between human mathematical cognition and the structure of celestial mechanics. We were fortunate: the first great problem of physics was one that admitted a beautiful answer.

[![Dappled reality](https://iai.tv/assets/Uploads/_resampled/FillWyI0MDAiLCIyNzUiXQ/Dappled-reality.webp)

SUGGESTED READING
Physics can't deal with reality's complexity
By Nancy Cartwright](https://iai.tv/articles/nancy-cartwright-physics-cant-deal-with-reality-complexity-auid-2269)

Protein folding is not like that. The interactions that determine a protein’s shape involve thousands of atoms and the forces between them. These forces are governed by quantum mechanics. And quantum mechanics is extremely computationally expensive as the number of atoms goes up. There may simply be no *F = ma* that we can actually use for protein folding—not because we have failed to find it, but because the domain does not have one to offer.

What AlphaFold provides instead is a statistical prediction tool devoid of theoretical principles. But it finds that tool using a fairly simple strategy—and the strategies machine learning scientists use are getting still simpler. There is something that echoes Wigner’s old astonishment—a new unreasonable effectiveness—in the fact that the same basic computational recipe can predict both how a protein folds and how a sentence ends. Eleven years ago, Andrej Karpathy called this “[The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/).” He was early but he was certainly right.

But there is a tension I do not want to paper over. Newton’s laws do not just predict the behavior of the planets; they explain why, for example, the planets travel in ellipses. They tell you why the planets move as they do. AlphaFold predicts the shape of a protein but doesn’t clearly explain why it takes that shape. [Does prediction without explanation constitute genuine scientific understanding? This is an urgent question.](https://iai.tv/video/ai-and-the-mysteries-of-reality)

**Simplicity is in the eye of the beholder**

Cambridge has been in the business of forging tools of prediction for a long time—from Newton’s *Philosophiæ Naturalis Principia Mathematica* to the double helix to the protein structures now pouring out of AlphaFold’s servers on the Biomedical Campus. What has changed is not the city’s ambition. It is the tools. That change brings about a change in the virtues we admire.

Perhaps the deepest lesson of this story is that simplicity was always in the eye of the beholder. Or better said: in the eye of the predictor. What counts as a simple, elegant solution depends on what kind of mind—or what kind of machine—is doing the predicting. For a human mind armed with calculus,

F = G m1m2⁄r2 is the pinnacle of intellectual economy. For a neural network armed with a million sequences, 93 million parameters may be an equally powerful achievement. It is opaque to us, but it is the shortest path from data to prediction.

As artificial intelligence assumes more of the labor of model-building, the virtues we prize in scientific representations—especially the virtue of simplicity—may shift from properties of theories to properties of methods. That is not necessarily a loss. After all, it may be the key to unlocking the cures to many diseases. But it is a change worth understanding.
