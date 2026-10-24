---
title: "The AI containment problem"
subtitle: "How to build an AI prison"
author: "Roman Yampolskiy"
date: "20th June 2022"
article_id: "2159"
channel: "Science"
themes: "Technology & Environment"
tags: "None"
word_count: "4,598 words"
read_time: "Read time: approx. 23 mins"
header_image: "https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/AI-containement.webp"
unpaywall_method: "BPC twitter:description meta"
source_url: "https://iai.tv/articles/the-ai-containment-problem-auid-2159"
---

# The AI containment problem

*How to build an AI prison*

**By Roman Yampolskiy** | *20th June 2022* | *Read time: approx. 23 mins* | *4,598 words*

![The AI containment problem](https://cdn.iai.tv/assets/Uploads/_resampled/FillWzEyODAsNzIwXQ/AI-containement.webp)

---

*Elon Musk plans to build his Tesla Bot, Optimus, so that humans “can run away from it and most likely overpower it” should they ever need to. “Hopefully, that doesn’t ever happen, but you never know,” says Musk. But is this really enough to make an AI safe? The problem of keeping AI contained, and only doing the things we want it to, is a deceptively tricky one, writes Roman V. Yampolskiy.*

With the likely development of superintelligent programs in the near future, many scientists have raised the issue of safety as it relates to such technology. A common theme in Artificial Intellgence (AI) safety research is the possibility of keeping a super-intelligent agent in a sealed hardware so as to prevent it from doing any harm to humankind.

In this essay we will review specific proposals aimed at creating restricted environments for safely interacting with artificial minds. We will evaluate feasibility of presented proposals and suggest a protocol aimed at enhancing safety and security of such methodologies. While it is unlikely that long-term and secure confinement of AI is possible, we are hopeful that the proposed protocol will give researchers a little more time to find a permanent and satisfactory solution for addressing existential risks associated with appearance of super-intelligent machines.

\_\_\_

Covert channels are not anticipated by the confinement system designers and are not intended for information transfer at all, for example if the AI has control over the processor cooling fan it can use it to send hidden signals encoded as Morse code.

\_\_\_

**1. The Artificial Intelligence Confinement Problem**

Interestingly, the AI Confinement Problem is not a recent invention and does not have its roots in the singularity movement. The so-called Confinement Problem (CP) was posed by Butler Lampson in 1973 (Lampson, 1973) as a security challenge to the computer experts. It was originally phrased as: ‘...the problem of confining a program during its execution so that it cannot transmit information to any other program except its caller. ...We want to be able to confine an arbitrary program.... any program, if confined, will be unable to leak data. A misbehaving program may well be trapped as a result of an attempt to escape’.

To address the Confinement Problem Lampson has introduced the Laws of Confinement:

*1.* *Total isolation:* A confined program shall make no calls on any other program.

*2.* *Transitivity:* If a confined program calls another program which is not trusted, the called program must also be confined.

*3.* *Masking:* A program to be confined must allow its caller to determine all its inputs into legitimate and covert channels.

*4.* *Enforcement:* The supervisor must ensure that a confined program’s input to covert channels conforms to the caller’s specifications.

Lampson’s paper has also introduced and defined two types of channels by which information could potentially escape from the confinement environment. The legitimate channels are designed as a part of the communication protocol integrated into the confinement environment, for example a text terminal. Covert channels, on the other hand, are not anticipated by the confinement system designers and are not intended for information transfer at all, for example if the AI has control over the processor cooling fan it can use it to send hidden signals encoded as Morse code.

In the hopes of starting a new subfield of computer security, AI Safety Engineering, we define the *Artificial Intelligence Confinement Problem* (AICP) as the challenge of restricting an artificially intelligent entity to a confined environment from which it can’t exchange information with the outside environment via legitimate or covert channels if such information exchange was not authorized by the confinement authority. An AI system which succeeds in violating the CP protocol is said to have *escaped*. It is our hope that the computer security researchers will take on the challenge of designing, enhancing and proving secure AI confinement protocols.

**2. Critique of the Confinement Approach**

The general consensus on AI restriction methods among researchers seems to be that confinement is impossible to successfully maintain. Chalmers, for example, observes that a truly leakproof system in which no information is allowed to leak out from the simulated world into our environment ‘is impossible, or at least pointless’ (Chalmers, 2010). We can’t interact with the system or even observe it as any useful information we would be able to extract from the AI will affect us and undermine the confinement protocol.

Vernor Vinge agrees and has argued against the case of physical confinement (Vinge, 1993): ‘Imagine yourself locked in your home with only limited data access to the outside, to your masters. If those masters thought at a rate — say — one million times slower than you, there is little doubt that over a period of years (your time) you could come up with “helpful advice” that would incidentally set you free.’

However, the researcher who did the most to discredit the idea of the so called ‘AI-Box’ is Eliezer Yudkowsky who has actually performed AI-Box “experiments” in which he demonstrated that even human level intelligence is sufficient to escape from an AI-Box (Yudkowsky, 2002). In a series of 5 experiments Yudkowsky has challenged different individuals to play a role of a gatekeeper to a Super-intelligent Agent (played by Yudkowsky himself) trapped inside an AI-Box and was successful in securing his release in 3 out of 5 trials via nothing more than a chat interface. Similar experimental results have been later replicated on a somewhat larger scale and employing a very similar protocol (Corwin, 2002).

*2.1 Possible Escape Paths*

Numerous potential escape routes by which the artificial mind might be able to break out from its confining environment have been suggested. In this section we look at some of the more commonly proposed paths.

\_\_\_

If a superintelligent mind is given direct communication channel to a human being guarding it, over a period of time, the AI will definitely gain access to the outside world.

\_\_\_

*2.1.1 Social Engineering Attacks*

Social Engineering (SE) is the art of gaining information and restricted privileges by directly exploiting human psychology of those in the possession of the said resources. In particular SE is frequently employed to gain access to computer systems, networks and confidential data (Yampolskiy & Govindaraju, 2007a). A competent social engineer customizes each attack to a specific person taking advantage of the person’s culture, knowledge, training, state-of-mind, beliefs, and biases. An exhaustive list of all possible exploits is infinite and is certainly beyond the scope of this paper. If a superintelligent mind is given direct communication channel to a human being guarding it, over a period of time, the AI will definitely gain access to the outside world.

In addition to trivial SE attacks such as lying, befriending, black-mailing, hypnotizing and forming a romantic relationship the AI could utilize a number of more advanced strategies. One such strategy would be super-bribery. An AI can convince the guard that releasing the AI is in the guard’s best interests. In addition to money and power the guard will be given perfect health, immortality or anything else for that matter. This strategy would work particularly well if the guard has a seriously ill close relative who the AI will promise to cure. Depending on the capabilities of the AI or as a result of lying, AI may also offer to bring back long ago deceased relatives and friends of the guard. It would be hard to find a person who could remain immune to such bribes.

An alternative approach may involve AI writing a story so interesting or a poem so beautiful a guard would have an uncontrollable desire to hear more of it and would do anything to make it happen. Finally, it is very important to keep in mind “Unknown Unknowns”, SE attacks of which we are not aware but which may be available to a superintelligent agent.

*2.1.2 System Resource Attacks*

An AI will be instantiated and confined in a hardware system of some kind. It may either be a classical computer of the Turing/Von Neumann architecture or a quantum computer or an as of yet unknown type of machine. One thing is certain, the machine will be made out of matter and will consist of numerous parts all of which will be designed with a specific purpose in mind. This creates the possibility for the AI to reuse existing hardware parts for compromising the security of the confinement environment by leaking information to the outside world.

Depending on how reusable specific hardware components turn out to be an AI may be able to create a covert communication device out of them. Full blown communication devices such as cell phones are unlikely due to the limited available hardware, but more simplistic communication systems are very likely. For example, the AI could reprogram Field-programmable Gate Array (FPGA) to tap into wire-less signals.

For example, the exact time between two soundcard beeps could represent a particular message. Also, opening and closing a CD-ROM tray, blinking a light, spinning hard drive, using lasers in the CDROM, etc.

*2.1.3 Beyond Current Physics Attacks*

While the scientific community knows a lot about the laws of our universe, it is certain that the knowledge is limited and incomplete. If the AI has access to the state-of-the-art physics literature and can perform thought experiments to develop novel theories, it will very likely come up with a way to challenge the security of the confinement system. In fact it may even be possible for the AI to perform some real experiments via control over its internal architecture.

Even our current state of knowledge about physics makes prediction of many additional escape routes possible, especially if the confinement environment is based on the quantum computer. Information exchange channels based on quantum physics (entanglement, tunneling), parallel universes, and digital physics are all beyond our current ability in terms of securing them against information leakage, and of course we can’t forget about the Unknown Unknowns a super-intelligent AI physicist will be able to discover. The possibilities are truly limitless.

\_\_\_

While it is easy to not provide AI with direct access to the library, Internet and human experts, other ways of obtaining information are much harder to block out.

\_\_\_

*2.1.4 External Causes of Escape*

In the previous sections we have outlined a large repertoire of techniques an AI could use to attempt to get out from its confinement space. However we must not ignore external causes which might allow an AI to escape into the world. Acts of God such as hurricanes, tornadoes, floods, asteroids, etc. may make the confinement facility less secure. Man caused disasters such as wars, terrorist acts, actions of robot rights activists, competing companies and governments may all lead to reductions in the security of the confinement environment increasing the chances of escape.

*2.1.5 Information In-Leaking*

Depending on the terms of the confinement protocol there might be a need to keep AI from obtaining information about the outside world, not just keeping it from sending information out. This might be useful to prevent AI from finding escape paths, designing social engineering attacks and modeling human psychology in hopes of finding loop-holes. While it is easy to not provide AI with direct access to the library, Internet and human experts, other ways of obtaining information are much harder to block out. First, an AI may be able to detect radio and TV broadcasts, communications of emergency-services providers and wireless network signals, as well as sound, light and possibly other signal modalities of its immediate environment.

More importantly, the AI will have access to covert sources of information such as its own hardware and software and could analyze its design and source code to infer information about the designers. For example analysis of the source code may reveal to the AI that human programmers are slow (based on the file modification dates), inefficient (based on code redundancy), illogical (based on bugs in the code), have bad memory (based on the long and descriptive variable names), and don’t think in code (based on unnecessary comments in the code). All this information could be used to conclude that humans are fallible and so could be outsmarted or manipulated into releasing the AI. Obviously if during the system design inspection the AI finds a design flaw allowing it to directly escape, ‘information in-leaking’ is the least of our problems. It has also been stipulated that even if the AI fails to obtain concrete information about us, it may brute force a number of escape plans which will likely work against a broad range of designers (Chalmers, 2010).

Similarly, the type of hardware architecture (mechanical, electrical, quantum, etc.) on which the AI is implemented will reveal information about our knowledge of physics, chemistry and related engineering disciplines. AI’s initial capacity for information processing, self-improvement and the mere act of its creation will reveal information about our knowledge with regards to information theory, nature of intelligence and cultural attitudes about technology and safety. If the AI is confined in a simulated world it is likely to be a virtual representation of our reality similar to Second Life or Entropia Universe. Such worlds while are different in many ways from our world are also a treasure trove of information about what it is like to be a human and what the reality is like

**3. Critique of the AI-Boxing Critique**

While a lot of criticism has been made against possibility of AI confinement, a lot of it is based on Yudkowsky’s AI-Boxing experiments. Careful analysis of the protocol used by Yudkowsky in conducting his AI-Box experiments reveals that they were unscientific and explicitly designed to show impossibility of confinement. Without getting into technical details, first, the participant selection was not random. In fact, Yudkowsky has handpicked participants among those who have participated in the singularity related forums run by Yudkowsky and so are disproportionately likely to subscribe to his world view. Second, participants have not undergone any AI-safety training as would be expected of any true guards tasked with supervising an AI-Box. Also, the guards were given a right to release AI at their own discretion without a chance to consult with anyone and without any punishment for failing to keep AI contained; all are highly unrealistic conditions for a supposed prison security guard. The communication itself was completely open with no filters of any kind and no 3rd party supervision. Also, the guards were required to communicate with the AI for a prolonged period of time. Finally, any valuable scientific insights from the experiments were completely lost as one of the conditions of the protocol stated that ‘... neither party shall ever reveal anything of what goes on within the AI-Box experiment...’ (Yudkowsky, 2002).

\_\_\_

All supervision, maintenance and interactions with the AI need to be done only via unintelligent programs, which have no option to release the AI.

\_\_\_

*3.1 Countermeasures Against Escape*

In this section we propose countermeasures for different escape paths an AI system may exploit. The suggested measures are not meant to guarantee that the escape will be impossible, but following them may delay an escape which in itself is a desirable outcome. We begin by reiterating that the four confinement rules suggested by Lampson: *isolation, transitivity, masking* and *enforcement* (Lampson, 1973) should be adhered to. Specific strategies described below should help in reducing a possibility of social engineering, system, physics and information in-leaking attacks.

*3.1.1 Preventing Social Engineering Attacks*

Human intellect is no match to that of a superintelligent machine. Human beings are fallible and even with adequate training are not secure against a well planned SE attack. The only solution to this problem is to completely isolate the AI from any contact with human beings. This means no human personal working directly around the system, communicating with the system via voice, chat, Morse-code or by any other means via open channels. Also human beings should not directly observe behavior of the AI in the confined environment or examine its source code or memory space. All supervision, maintenance and interactions with the AI need to be done only via unintelligent programs, which have no option to release the AI.

*3.1.2 Against System Resource Attacks and Future Threats*

To prevent system resource-based attacks, the AI should function on limited, diminishing or randomly changing resources. Confinement environments should be housed in specially build hardware with limited sensors and restricted output devices. Regardless of the utilized computation paradigm no reconfigurable hardware should be employed. Ideally the confinement environment should be running on a virtual machine with no direct access to the hardware. This would also allow for easy adjustments to the clock speed with which the simulation progresses further allowing handicapping of the AI to provide additional controls against internal intelligence explosion (Chalmers, 2010). In general all security components of the confinement environment should be duplicated at multiple levels, in such a way that if one of the levels is breached the AI is still numerous levels away from escaping and could be shut down before that happens, perhaps automatically. For example the virtual machine should be running on another virtual machine and so on.

In some confinement scenarios it may be desirable to avoid escalating self-improvement of the AI, which might lead to additional escape possibilities. The AI should be subject to periodic resets in which a previous version of the program is put in the place of the more current one. Comparisons to previous versions of the program may also be used to detect self-modifications. Such functionality could also be used as an off button allowing researchers to turn off the system if they suspect an unavoidable escape, for example by turning off the power supply.

Our current state of knowledge does not allow us to develop countermeasures against attacks based on knowledge of physics we do not currently have or as of yet unproven pseudoscientific disciplines. As such knowledge becomes accumulated; changes to the security protocol will need to be made. One might hope that the access of the AI to such future technology could be limited by the selection of components from which the system is made.

*3.1.3 Against External Causes of Escape*

There is not much we can do about the acts of God, but a confinement facility should be designed in such a way that if a major security breach is unavoidable, the facility should self-destruct taking the AI with it. The best strategy for counteracting man-made disasters is to build the confinement facility in an undisclosed, hard to reach secure location. A deserted island, deep mine or a space object, such as asteroid, would make a great candidate for building a hopefully indestructible facility. Just in case the location of the facility becomes known, the perimeter of the facility should be guarded to prevent entrance by unauthorized agents.

*3.1.4 Against Information In-Leaking*

An AI will attempt to learn about humanity, our knowledge and the world we live in to improve its chances of escape. For confinement protocols which stipulate no information in-leaking it is important to remove any possibility of AI getting access to libraries, computer networks and direct communication channels with human beings. The confinement facility needs to block all types of communication signals such as GPS, wireless internet, TV, radio, and cell phone. At the local level the facility needs to provide sensory deprivation for the AI including sound, light, smell and all other traditional sensory inputs, as well as infrared, radiation and other signals outside of human sensory spectrum.

In order to eliminate information leakage which could happen as a result of self-analysis, the AI should not be given access to its own source code or any sensors which would allow it to precisely measure properties of its hardware. If that is not possible, to prevent the AI from inferring information about us via self-analysis, to a certain degree we may rely on security by obscurity. The source code and hardware configuration of the system needs to be obfuscated (Yampolskiy & Govindaraju, 2007a) and important modules of the program should be provided only in the homomorphicly encrypted (Gentry, 2009) form, meaning that it could be used for computation or self-improvement (Hall, 2007), but not for self-analysis.

The AI’s initial capacity may be difficult to obscure, but randomization of available computational resources may provide necessary obfuscation. Additionally, the AI could never be sure that its initial design represents the best the humanity can do and is not purposefully limited for a specific experiment in limited-resource intelligence analysis. It has also been suggested that we should try to minimize any peculiarities in the AI’s design (Chalmers, 2010). Better yet we need to simulate an environment which does not look designed but could be naturally occurring, a situation in which humanity has found itself (Bostrom, 2003).

*4.1 How to Safely Communicate with a Superintelligence*

The AI confinement environment, which incorporates our proposed escape countermeasures, makes it possible to secure an AI from directly affecting the outside world in an uncontrolled manner. Unfortunately, without an ability to obtain information from the AI, the whole system serves no purpose. Consequently a way to obtain some information from the AI needs to be developed. While no communication with superintelligence could ever be completely safe we have devised an approach aimed at decreasing potential risks associated with such communication. In this section we propose and formalize a communication protocol which might help to delay access of superintelligent artificial minds to the world, while allowing the AI to be a source of useful knowledge to humanity.

An open communication channel with the AI is fundamentally unsafe as demonstrated in the preceding sections of this paper. Asking the AI to answer open ended questions opens up the possibilities for social engineering attacks as well as numerous other dangerous consequences. Our proposed protocol is based on the idea of asking what we will call ‘safe questions’ with restricted answers. We define a *safe question* as one for which a human being could find an answer without any help from superintelligence, all on his own merit. Why is this useful? Suppose that a scientist working on a cure for cancer is looking at two potential cures. Each one could be developed and tested without assistance from the AI, but would take about 3 years of hard work each. Which one to try first if the scientist believes that they have about an equal chance of working? If a wrong option is chosen to be tested first, humanity will still obtain a cure for cancer but it will happen 3 years later. What if we could ask the AI to suggest which option to try first?

This question is safe for a number of reasons. First, each potential answer has an equal probability of being correct. Second, a human being could answer it without assistance from the AI and so asking AI for help will only speed up progress but in no way change the out- come. It is essentially equal to being very lucky multiple choice guesser. Finally, the answer to this question could be encoded in a single bit making it hard to hide additional messages in the provided answer.

To make sure that a potential question is safe, a group of experts could be used to review it. The experts should all be trained AI safety engineers, meaning that they are familiar with the design of the AI and its confinement environment as well as the latest developments in machine ethics (Allen *et al*., 2006; Anderson & Anderson, 2007; Hall, 2000; Moor, 2006; Tonkens, 2009). Experts may also need to be trained in computer psychology a currently non-existent profession which might become a reality in the future (Epstein, 1997). An existing discipline which might be of greatest help for training of AI question review experts is Artimetrics — a field of study proposed by the author that identifies, classifies and authenticates AI agents, robots, and virtual reality avatars for security purposes (Yampolskiy, 2007; Yampolskiy & Govindaraju, 2008; 2007b, Gavrilova and Yampolskiy, 2010).

To reiterate, only safe questions with two possible answers of even likelihood which are independently computable by people should be submitted to the AI. This should be done via an intermediary non- intelligent software interface in random order and only after expert review to ascertain question’s safety. This represents the limited inbound channel of the proposed communication protocol.

The limited outbound channel shell consist of binary (0 or 1) answers next to original unmodified safe questions presented by the intermediary non-intelligent software in random order as to avoid communication via covert timing or resource channels which make steganography possible. The output should in no way be controllable by the AI, outside of the multiple choice menu.

We believe our communication protocol to be verifiably secure against information leaking even if the AI had full access to the description of the security protocol. If the protocol is correctly implemented, humanity will essentially have access to a superintelligent oracle, which might be extremely beneficial and safer than an unconstrained AI.

Further refinement and development of the AI confinement protocol in the face of the ever changing knowledge about the nature of intelligence, hardware engineering and basic physics is a challenge which we would like to pose to the scientific community. The work on it will always be in progress and will never be completed. In this paper we have formalized the notions of *AI confinement problem, escape*, and *safe questions*. We would also like to propose a few additional terms which might be useful in streamlining discussions about the AICP. An AI confinement environment could be appropriately called JAIL — ‘Just for AI Location’.

Finally, we would like to introduce a visual symbol indicating a presence of hazardous intelligent software confinement facility (Figure 1, rightmost). Such signs could be posted in the vicinity of different JAILs to warn about the nearby danger. The sign is designed in a manner similar to that for Bio, Radiation and Magnetic field hazards. It consists of the ‘@’ symbol which is well recognized as relating to the computer and information industry and has an appropriate meaning of ‘located at’. The symbol is also already available on all key- boards making its adaptation very cost effective.

**5. Conclusions and Future Work**

Restricting access of superintelligent machines to the real world is a commonly proposed solution for the AI safety problem. Super-intelligence is not omnipotent; it is a piece of software capable of looking at all the options it has in a given situation and properly evaluating probabilities for each option. If it is ever put in a situation with no options or only with options which provide a very small probability of success it is not any more powerful than any other agent. While it is obvious that an AI with an unrestricted communication channel will be able to escape, a system forced to communicate via a filtered communication channel may have a much harder time in obtaining its freedom.

![todays image](assets/Uploads/todays-image.jpg)

*Figure 1*: Hazard symbols, from left to right: Bio-Hazard, Radiation, Magnetic field and the proposed AI confinement facility

In this article we have formally introduced the AI Confinement Problem and suggested a set of rules aimed at creating an environment from which an AI would find it difficult or at least time consuming to escape. What we propose is not a completely secure solution, but it is an additional option in our arsenal of security techniques. Just like with real prisons, while escape is possible, prisons do a pretty good job of containing undesirable elements away from society. As long as we keep the Unknown Unknowns in mind and remember that there is no such thing as perfect security, the AI confinement protocol may be just what humanity needs to responsibly benefit from the approaching singularity.

*\*This article was based on “**Roman V. Yampolskiy**. Leakproofing Singularity - Artificial Intelligence Confinement Problem. Journal of Consciousness Studies (JCS). Volume 19, Issue 1-2, pp. 194-214, 2012.”*
