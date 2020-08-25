---
title: 'Moran Pycess: a Python package to simulate Moran processes driven by game theory'
tags:
- Python
- Moran Process
- evolutionary stable strategy
- game theory
authors:
- name: Maciej Bak
  orcid: 0000-0003-1361-7301
  affiliation: "1, 2"
- name: Anna M. Rozlach
  orcid: 0000-0002-5195-4299
  affiliation: 3
affiliations:
 - name: University of Basel
   index: 1
 - name: Swiss Institute of Bioinformatics
   index: 2
 - name: Faculty of Biochemistry, Biophysics and Biotechnology, Jagiellonian University
   index: 3
date: 25 August 2020
bibliography: paper.bib
---
# Summary

Population is created by individuals of the same species living simultaneously on a shared area and related to each other by a complex system of mutual dependencies.
Population characteristics, including: reproduction, mortality, abundance or life strategy change over time under the influence of evolutionary mechanisms. Complicated network of interactions with several degrees of freedom is very challenging for evolutionary biologists to decode. A simple mathematical model proposed by Patrick Moran is often used to describe probabilistic dynamics of a finite population of constant size `[@Moran:1958]`. Within this framework, each individual might be assigned with a fitness score calculated solely based on the scored interactions with all the other members of the group. Fitness drives the probability of an individual to reproduce while mutual interaction scores are calculated according to a common ‘payoff matrix’, treating the whole system as a game. In many populations the emergence of evolutionary stable strategy (EES) is observed. ESS complements Nash's equilibrium with an additional stability condition. A strategy is considered as evolutionary stable if it is resistant to an invasion of a small group with a different phenotype and cannot be overtaken `[@Smith:1982]`. Evolutionary game theory set grounds 
for a solid framework for quantitative population biology, allowing researchers 
to simulate dynamics and estimate trajectories of biological systems.

# Statement of need 

We have developed a Python package with a general game-theoretical framework for scientific simulations according to the Moran model. Contrary to cellular automata, the following approach allows the stochastic nature of evolution to be preserved. We chose Python because of its availability and popularity in the fields of bioinformatics and data analysis. In principle, such simulations could be recreated within DEAP - a framework dedicated to genetic and evolutionary algorithms `[@Fortin:2012]`. However, unlike DEAP, Moran Pycess is capable of carrying out simulations over 2D and 3D grid where individuals consider their direct neighbours. Three-dimensional space is particularly important for modeling dynamics of population growth in cell biology `[@Macnamara:2020]`. Moreover, due to its complexity, DEAP is more suitable for users with good software engineering skills. In contrast, the strength of Moran Pycess lays in its simplicity which turns it into a useful research aid for evolutionary and computational biologists. Open source license as well as its accessibility endorse Moran Pycess as a practical tool for biology, economics and math students to learn about population evolution based on game theory or for computer science students aiming to properly encapsulate their research software. A remarkable  advantage of our module is that any possible model of a game may be considered. This is not the case for another powerful Python package - Axelrod - which allows to model evolution of cooperation in various strategies, but is limited to Prisoners’ Dilemma only `[@axelrodproject:2016]`. In terms of quality assurance: our repository incorporates Travis CI mechanism alongside Coveralls code coverage measurement (currently: 100%).

