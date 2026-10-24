---
title: "Puzzles reveal the limits of AI"
subtitle: "The missing Aha! moments"
author: "Cristopher Moore"
date: "29th July 2026"
article_id: "3638"
channel: "Science"
themes: "Technology & Environment"
tags: "None"
word_count: "2,271 words"
read_time: "Read time: approx. 11 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/puzzles-reveal-the-limits-of-ai.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/puzzles-reveal-the-limits-of-ai-auid-3638"
---

# Puzzles reveal the limits of AI

*The missing Aha! moments*

**By Cristopher Moore** | *29th July 2026* | *Read time: approx. 11 mins* | *2,271 words*

![Puzzles reveal the limits of AI](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/puzzles-reveal-the-limits-of-ai.webp)

---

*Puzzles compress the experience of insight into miniature, letting us watch understanding take shape in real time. Computer scientist **Cristopher Moore** argues that while AI can brute-force its way to a correct answer, only humans experience the leap from confusion to clarity that marks real insight, replacing mechanical search with an elegant path. As AI makes knowledge ever cheaper and easier to look up, Moore warns that we risk losing the habit—and the reward—of struggling toward answers ourselves.*

**What is understanding?**

Artificial intelligence produces images that look like reality, and text that looks like thought. We all know that it merely recombines its training data to produce its responses, and yet this ability to recall and remix human knowledge produces amazing results.

Debates rage about whether AI understands what it says. But what does it mean to understand? What does it mean to have an insight, a realization about something? What is the nature of that “Aha!” moment when you suddenly grasp what was mysterious before?

Puzzles are understanding in miniature. Solving puzzles, designing them, and posing them to each other lets us create and navigate worlds of pure insight—worlds where “Aha!” experiences are central.

We can use [puzzles as a philosophical playground](https://iai.tv/articles/the-universe-is-a-puzzle-that-fits-together-only-one-way-auid-3428) to think about the nature of insight, and compare human and artificial approaches. And we can explore what understanding means to us as human beings—both when we struggle toward it ourselves, and when we share it with each other.

**Puzzle #1: The magic square**

![figure one](assets/Uploads/_resampled/ResizedImageWzYwMCwzOTld/figure-one.webp)

*Figure 1. Steps toward the magic square. We use symmetry to conclude that if the center is unique it must be 5, and parity to place the even digits in the corners. Then everything is easy to fill in.*

Here’s an example. Ancient Chinese, Indian, and Persian mathematicians discovered that you can arrange the digits 1 through 9 in a three-by-three square so that every row, every column, and both diagonals sum to 15.

The fact that such a thing exists is lovely and mysterious, and these “magic squares” were sometimes ascribed occult powers. But how can we find one? Let’s pose this for ourselves as a puzzle. You might enjoy working it out for yourself. I’ll be over here.

The first thing you might notice is the symmetry of the problem. If we rotate a magic square by 90 degrees, or flip it top-to-bottom or left-to-right, it remains a magic square. The only part of it that doesn’t move is the center.

\_\_\_

We can use puzzles as a philosophical playground to think about the nature of insight, and compare human and artificial approaches.

\_\_\_

 Now suppose I give you the hint that there is essentially only one solution—that every magic arrangement is the same except for rotations and flips. That means there is one number which always has to be in the center.

We can find that central number using another kind of symmetry. If I subtract each digit from 10, replacing x with 10–x, the magic square stays magic—do you see why? We can think of this as reversing the order of the digits, counting from 9 down to 1 instead of 1 up to 9.

Combining our symmetries, if x is the digit in the center, we must have 10–x=x. But that means that x is 5, and we have our first digit. If you intuited that the 5 ought to be in the center since it’s midway from 1 to 9, you have the right idea.

Next we might consider the “parity” of the digits—their evenness and oddness. Since 15 is odd, if three digits sum to 15, then either one is odd and the other two are even, or all three are odd. A little thought reveals that 2,4,6, and 8 must be in the corners. Once we choose where one of them goes—say, 2 in the upper left corner—everything falls into place. (See Figure 1.)

\_\_\_

This is how I would define an insight: the replacement of a mechanical, brute-force approach with an elegant one.

\_\_\_

If you got there on your own or followed along, there’s a reason to be proud. The number of potential arrangements of the digits 1 through 9 is huge: there are 9 places 9 can go, then 8 places left for 8 to go, and so on, for a total of 9⨉8⨉7⨉6⨉5⨉4⨉3⨉2⨉1=362,800.

Of course a computer could search through all of these possibilities quickly. But even if such a computer is fast, it is stupid. In contrast, we pursued an intelligent path and bypassed this search entirely. Mathematically, this is how I would define an insight: the replacement of a mechanical, brute-force approach with an elegant one.

The magic square is a small puzzle, but it’s a good example. To solve it, we used several different kinds of reasoning: symmetry, parity, and a little arithmetic. Human thinking, at its best, is flexible and fluid. If one approach fails to make progress, we switch to another, using our experience, intuition, and luck to find a way forward.

**Puzzle #2: Fluid thinking**

![figure 2.1](assets/Uploads/figure-2.1.webp)

![figure 3.2](assets/Uploads/_resampled/ResizedImageWzYwMCwzMTNd/figure-3.2.webp)

*Figure 2. The twelve pentominoes, and one way that they can tile a rectangle.*

We see this same fluidity in puzzles where we have to fit things together. In Figure 2, you see a set of shapes fitting into a rectangle, covering it like a set of tiles. These tiles are carved like cats, but each one is a “pentomino” made of five squares, just as a domino is made of two. If you allow rotations and flips, pentominoes come in twelve different shapes. They are among the most beloved objects in recreational mathematics, and appear in many puzzles and games. It’s easy enough to write a computer program that solves this kind of puzzle. It starts at one corner and puts a tile there. Then it looks for the next empty space and puts a tile there, and so on. If it runs out of space or ends up with a gap where no tile fits, it backtracks to the last choice it made and tries the next alternative, in some fixed order. In this way, it explores a branching tree of arrangements, trying each tile in each place until it finds a solution or a contradiction.

Even for this kind of brute-force algorithm, there is some room for insight. In the early days of artificial intelligence—what we call “good old-fashioned AI”—people designed rules for guiding this kind of search, telling it what branch of the tree to try first. These rules or “heuristics” were used to solve problems with many interacting variables, like tiles that can’t overlap or leave gaps between them.

One popular heuristic tells us to set the most-constrained variable first. If a variable has fewer choices, there are fewer branches in the tree to explore. Moreover, if it interacts with many other variables then setting it will have widespread consequences, making the remaining problem easier to solve.

For instance, the “X” pentomino is quite picky about where it goes. It can’t fit in a corner, and it tends to exclude many options for its neighbors. This makes placing it as early as possible a good idea.

Humans do this sort of thing, but we do so much more. We feel the pieces, look at them, and turn them over in our hands. We notice that some pairs of them fit neatly together. As we start to place them, we switch fluidly from asking questions like “where can this go” to “what can go here.” We invent new kinds of variables with new logical relationships between them, adapting them to the problem at hand.

**Puzzle #3: New Sudoku**

![figure 4](assets/Uploads/figure-4.webp)

*Figure 3. A modern Sudoku by the author. In addition to the usual rules, digits a knight’s move apart much be different. Each purple line sums to 15, and each one does so with a different set of digits. Finally, the line with the bulb is a thermometer, with the digits increasing as we move away from the bulb. See [this video](https://www.youtube.com/watch?v=Iu9sDHZwjj8) for the solution.*

This human fluidity and invention is especially clear in a new genre of puzzles. The reader is probably familiar with old-fashioned Sudoku: the digits 1 through 9 have to appear once in each row, each column, and each three-by-three box in a nine-by-nine grid of cells.

Many people solve Sudoku puzzles with two kinds of “pencil marks.” Marks in the corners of cells mean things like “the 4 could go here,” and marks in the center mean things like “this digit must be 2 or 7.” These are two kinds of variables, as for the pentominoes—“where does this go” and “what can go here”—that the solver can try to figure out.

Switching between these two variables keeps things somewhat interesting. However, for experienced solvers this process becomes mechanical, more like vigilant bookkeeping than “Aha.”

Modern variants of Sudoku, popularized by the puzzle champions Simon Anthony and Mark Goodliffe on their channel Cracking the Cryptic, offer many more opportunities for insight. These puzzles are full of new rules and objects: thermometers along which digits must increase, palindromes where the digits read the same either way, “killer cages” that tell you their total but not any of the digits inside them, and so on. In fact, many of the most popular modern puzzles don’t start out with any digits at all.

These new puzzles are often hard or impossible to solve if we stick to the traditional pencil marks. But as humans always do, we invent new approaches. We can color cells to indicate that their digits are different or the same; mark cells as odd or even as we did for the magic square; scribble possible combinations of digits on a notepad; and so on.

Each of these is a new point of view, a new kind of knowledge to seek, and a new way of notating that knowledge. And puzzle designers, knowing well that solvers look for these insights, try to create, like a challenging but benevolent teacher, a series of “Aha!” moments for the solver to experience and enjoy.

My greatest hit, shown in Figure 3, is a magic square in disguise. The purple lines correspond to rows, columns, and diagonals of the magic square—but how? (Designing this puzzle was a meta-puzzle in itself.) The strongest AI systems can solve this puzzle by searching, but humans can find a simple path through a series of clever insights.

**Puzzles and proofs**

All this puzzling is very similar to what we do in mathematics. I think of a puzzle—especially a puzzle with a beautiful logical path—as an elegant proof of its own solution. It may be presented in cryptic form, or as a series of subtle signposts, but it provides just enough information to let the solver find, or build, its solution.

To continue the analogy, the best proofs are not just a series of logical steps arriving at a conclusion. Such a proof might establish that the conclusion is true, but that is all it does. It provides mere knowledge, and knowledge only of that one thing.

In contrast, a good proof gives us a sense of why something is true. It helps us learn, not just about that one problem, but about the larger web of mathematics: what analogies it has with other problems and other truths, how far these analogies can be stretched and where they break down. It teaches us something new about how truth works. It gives us insight and understanding.

\_\_\_

Rather than asking whether AI understands, we should ask whether it will help us understand.

\_\_\_

This is why, even after mathematicians have proved a theorem, we often look for other proofs that work in different ways. We want many proofs with many points of view: algebraic, geometric, probabilistic. [Pythagoras’ theorem](https://iai.tv/articles/mathematical-beauty-should-not-eclipse-truth-auid-3534) about the square of the hypotenuse has hundreds of proofs. Each one adds to our ability to understand it, to hold and turn it in our hands, to make it our own.

In the same way, [the best puzzles teach us a lesson](https://iai.tv/video/data-needs-theory-lisa-randall). They enlarge us and broaden our thinking. We come out of them with a sense that we have learned something, even [if that thing is hard to put into words](https://iai.tv/articles/most-truths-cannot-be-expressed-in-language-auid-2335).

**Knowledge vs. understanding**

As AI continues to advance, there is a great danger that knowledge will become too cheap. It is too easy to look up the answer rather than finding it for ourselves. If we are not careful, we will lose the experience of struggling to find our way, and the thrill when it all becomes clear. We will lose the habit of searching for the truth, and lose the sense that a deeper understanding is worth the effort.

Rather than asking whether AI understands, we should ask whether it will help us understand. After all, we often act like AI ourselves. We spit out strings of likely words without introspection, relying on our training without asking whether it is right or wrong. We are easily deceived and easily manipulated, and too willing to replace critical thinking with the latest prompts from those around us.

But at our best, we do something more. We measure our words and actions not by what others say, but by whether they are true and good. Whether we admit it or not, we sense that there is a truth external to us. We know that our perceptions of it are flawed and that we are often wrong, but we struggle toward it anyway. To reach it, we yearn to understand each other and the world around us.

As a librarian and translator, it is extraordinarily useful. And if I give AI a scientific problem, it might well solve it. But if I give that problem to a young researcher instead, I don’t just get the solution: I get a human being who [understands more than they did before](https://iai.tv/video/planck-and-the-consciousness-puzzle). And that is what matters.

Knowing is not enough. We have to understand.
