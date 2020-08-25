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

