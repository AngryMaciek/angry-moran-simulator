---
title: 'Moran Pycess: a Python package to simulate Moran processes driven by game theory'
tags:
- Python
- Moran Process
- evolutionary stable strategy
- evolutionary game theory
authors:
- name: Maciej Bak
  orcid: 0000-0003-1361-7301
  affiliation: "1, 2"
- name: Anna M. Rozlach
  orcid: 0000-0002-5195-4299
  affiliation: 3
affiliations:
 - name: Biozentrum, University of Basel
   index: 1
 - name: Swiss Institute of Bioinformatics
   index: 2
 - name: Faculty of Biochemistry, Biophysics and Biotechnology, Jagiellonian University
   index: 3
date: 25 August 2020
bibliography: paper.bib
---

# Summary

Moran Pycess is a bioinformatics Python package created to simulate population’s growth based on evolutionary game theory and the Moran Process model. Growth dynamics is controlled solely by the interactions of individuals with each other. Our software is primarily targeted to evolutionary and computational biologists, however students who learn basic concepts behind evolution may find it equally practical.

# Introduction

A population consists of individuals of the same species living simultaneously on a shared area and related to each other by a complex system of mutual dependencies. Population characteristics (e.g reproduction, mortality, abundance or life strategy) change over time as a result of evolutionary mechanisms. A complicated network of interactions with several degrees of freedom is very challenging for evolutionary biologists to decode. A simple mathematical model proposed by Patrick Moran is often used to describe probabilistic dynamics of a finite population of constant size [@Moran:1958]. Within this framework, each individual might be assigned with a fitness score calculated solely based on the scored interactions with all the other members of the group. Fitness drives the probability of an individual to reproduce while mutual interaction scores are calculated according to a common ‘payoff matrix’, treating the whole system as a game. In many populations the emergence of evolutionary stable strategy (ESS) is observed. ESS complements Nash's equilibrium with an additional stability condition. A strategy is considered evolutionarily stable if it is resistant to an invasion of a small group with a different phenotype and cannot be overtaken [@Smith:1982]. Evolutionary game theory set grounds for a solid framework for quantitative population biology, allowing researchers to simulate dynamics and estimate trajectories of biological systems.

# Statement of need 

We have developed Moran Pycess - a Python package with a general game-theoretical framework for scientific simulations according to the Moran model. Such an approach allows the stochastic nature of evolution to be preserved. This is not the case for cellular automata, which are completely deterministic systems and where evolution of each cell follows some strictly defined local rules. We chose Python because of its availability and popularity in the fields of bioinformatics and data analysis. It is worth emphasizing that Moran Pycess is capable of carrying out simulations over 2D and 3D grid where individuals consider their direct neighbours. Three-dimensional space is particularly important for modeling dynamics of population growth in cell biology [@Macnamara:2020]. Another strength of Moran Pycess lays in its simplicity which turns it into a useful research aid for evolutionary and computational biologists. An open source license as well as its accessibility endorse Moran Pycess as a practical tool for biology, economics and math students to learn about population evolution based on game theory or for computer science students aiming to properly encapsulate their research software. A remarkable advantage of our module is that any possible model of an antagonistic game may be considered. In terms of quality assurance: our repository incorporates Travis CI mechanism alongside Coveralls code coverage measurement (currently: 100%).

# State of the field

In principle, such computations could be recreated within DEAP - a framework dedicated to genetic and evolutionary algorithms [@Fortin:2012]. However, these simulations would not be as straightforward to implement in DEAP as in Moran Pycess. Due to its complexity, DEAP is more suitable for users with good software engineering skills. Notably, another powerful Python package - Axelrod - is limited to Prisoners' Dilemma, while Moran Pycess allows to model evolution of cooperation in various strategies [@axelrodproject]. 

# Example results

We have designed four distinct systems based on well-known interaction examples which have been vastly described in the literature [@Tadelis:2012].

![Simulations of population evolution based on: (A) Stag Hunt (B) Chicken game, (C) Prisoners' Dilemma, (D) Rock Paper Scissors.](images/figure.png)

(A) The stag hunt game model describes a conflict between safety and social cooperation: hare - small but certain profit, stag - great benefit but adventurous. Failure in cooperation leads to a player’s loss. There is no dominant strategy in this game as it is most beneficial for individuals to agree on the same strategy. Both stag hunt and hare hunt are considered as an ESS. A perfect example of this type of interaction is the “carousel feeding” as a cooperative hunting method used by Norwegian orcas which force the school of fish to form a tight ball, then stun fish with their tails [@Fort:2007].
(B) In the game of Chicken a confrontational strategy brings a greater profit. However, if chosen by both individuals it yields the worst outcome. A peaceful strategy, while protecting against the greatest possible loss brings no reward when challenged by an aggressor. No player has a dominant strategy and there are no ESS in pure strategies in this game. Consider an example of two strains of the yeasts S. cerevisiae: wildtype and a mutant lacking the invertase gene. In a monosaccharide-poor environment yeasts may utilise invertase to produce an energy source from more complex molecules. Most monosaccharides are excreted to the extracellular environment from where they can also be taken up by other cells. Mutant strains (“cheaters”) follow a confrontational strategy: they consume glucose created by wildtype cells without bearing the metabolic cost of invertase production and secretion. Therefore, in a population, a confrontational strategy has a good advantage over the peaceful one, given the number of wildtype yeasts exceeds the number of mutants vastly. In case this condition is not met cheaters would fail to live off the others, leading to starvation - the worst possible scenario for them. Moreover, the analogy holds while inspecting the behaviour of wildtype yeasts. Trying to avoid that worst scenario, in the presence of mutants, wildtype cells cooperate in invertase expression over a wide range of conditions. However, when competing against other wildtype strains, invertase expression is repressed, causing them to exhibit the confrontational strategy - cheat. [@Gore:2009].
(C) Prisoners’ dilemma, often analyzed in game theory due to its multiple applications, presents a case where two completely rational individuals might not cooperate, even if it appears that it is in their best interests to do so. The most rational strategy yields the worst collective outcome. Every participant has a dominant strategy. The only ESS is to always cooperate. In biological context the prisoner’s dilemma successfully captures the essential features of cancer growth and allows to test hypotheses and formulate claims in a quantitative manne [@West:2016]. In the case of malignant tumors, we observe the possibility of infiltration of adjacent tissues by cancer cells. Their characteristic uncontrolled proliferation leads to the growth of another tumor in this place and the destruction of healthy tissue.
(D) Rock-paper-scissors is a game with cyclic dominance resulting in an oscillating number of individuals of a given type. There is no ESS in this game. Remark the case of the side-blotched lizard. The male lizards come in three color morphs: orange, yellow, and blue. The orange males defend large territories. The yellow males invade orange males territories. The blue male effectively expels yellow males from their territory but are outcompeted by aggressive orange meles [@Sinevro:1996]. As a result: yellow beats orange, which bests blue which beats yellow.

# Supplementary data: Stochastic nature of the simulations

To demonstrate the stochastic nature of the simulations let us consider a Hawk-Dove model where the resources value is only slightly higher than the confrontational cost. A small group of hawks, having an ESS, try to invade a larger community of doves. However, if the initial number of predators is too low their advantage might not be sufficient for them to overtake the whole population.

![Replicated simulations of evolution according to the Hawk-Dove model: (A) 5 hawks invade a group of 95 doves: 5/10 times the population is overtaken by the invaders, (B) 15 hawks invade a group of 85 doves: 10/10 times the population is overtaken by the invaders.](images/supplementary_figureA1.png)

# References

