[![build](https://github.com/AngryMaciek/angry-moran-simulator/workflows/build/badge.svg?branch=master)](https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Abuild)
[![pytest](https://github.com/AngryMaciek/angry-moran-simulator/workflows/pytest/badge.svg?branch=master)](https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Apytest)
[![codecov](https://codecov.io/gh/AngryMaciek/angry-moran-simulator/branch/master/graph/badge.svg?token=V9IFEOWN71)](https://codecov.io/gh/AngryMaciek/angry-moran-simulator)
[![flake8](https://github.com/AngryMaciek/angry-moran-simulator/workflows/flake8/badge.svg?branch=master)](https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Aflake8)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/angrymaciek/angry-moran-simulator/badge)](https://www.codefactor.io/repository/github/angrymaciek/angry-moran-simulator)
[![publish](https://github.com/AngryMaciek/angry-moran-simulator/workflows/publish/badge.svg)](https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Apublish)
[![PyPI](https://img.shields.io/badge/pypi-1.0.38-blue)](https://pypi.org/project/moranpycess/)
[![conda](https://anaconda.org/angrymaciek/moranpycess/badges/version.svg?service=github)](https://anaconda.org/AngryMaciek/moranpycess)
[![DockerHub](https://img.shields.io/badge/DockerHub-1.0.38-blue)](https://hub.docker.com/r/angrymaciek/moranpycess)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AngryMaciek/angry-moran-simulator/master?filepath=tests%2Fusecase.ipynb)
[![GitHub issues](https://img.shields.io/github/issues/AngryMaciek/angry-moran-simulator)](https://github.com/AngryMaciek/angry-moran-simulator/issues)
[![GitHub license](https://img.shields.io/github/license/AngryMaciek/angry-moran-simulator)](https://github.com/AngryMaciek/angry-moran-simulator/blob/master/LICENSE)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.02643/status.svg)](https://doi.org/10.21105/joss.02643)

# Moran [Py]cess

![scheme.svg](images/scheme.svg)

## General information

The following Python package presents a general game-theoretical framework to carry out scientific simulations according to the [Moran model]. Registering distinct types of individuals together with specification of payoffs between them allows to replicate evolution of the population and observe growth dynamics.

For more information please visit project's homepage.

## Example results

### General Moran Model

![figure.png](images/figure.png)
> Simulations of population evolution according to four basic models of game theory: (A) Stag Hunt, (B) Chicken, (C) Prisoners Dilemma, (D) Rock-Paper-Scissors

### Moran Model based on 2D neighbourhood

Average payoff for an individual is calcualted based on interactions with 8 direct neighbours of a given individual (2D grid). Periodic boundary conditions are applied.

![figure.png](images/supplementary_figure1a.png)
> Population snapshots during an evolution according to a Prisoners Dilemma model. Starting from a small subpopulation of Defectors (A, t=0) we observe gradual growth (B, t=50000), (C, t=200000) until the whole population is almost completely overtaken (D, t=500000).

![figure.png](images/supplementary_figure1b.png)
> Growth curve for the population evolution according a Prisoners Dilemma model.

### Moran Model based on 3D neighbourhood

Average payoff for an individual is calcualted based on interactions with 26 direct neighbours of a given individual (3D grid). Periodic boundary conditions are applied.

![figure.png](images/supplementary_figure2.png)
> Growth curve for the population evolution according a Prisoners Dilemma model.

[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Moran model]: <https://en.wikipedia.org/wiki/Moran_process>
[Python package manager]: <https://pypi.org/project/pip/>
