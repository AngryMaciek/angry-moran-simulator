.. Moran [Py]cess documentation master file, created by
   sphinx-quickstart on Fri Apr  2 19:24:36 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: General Information

   general-info/installation
   general-info/background
   general-info/example-results
   general-info/citing-contributing
   CHANGELOG.md
   general-info/license

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: API

   api/users-api
   api/internal-api

Moran [Py]cess
==========================================

.. image:: https://github.com/AngryMaciek/angry-moran-simulator/workflows/build/badge.svg?branch=master
   :alt: build
   :target: https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Abuild
.. image:: https://github.com/AngryMaciek/angry-moran-simulator/workflows/pytest/badge.svg?branch=master
   :alt: pytest
   :target: https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Apytest
.. image:: https://codecov.io/gh/AngryMaciek/angry-moran-simulator/branch/master/graph/badge.svg?token=V9IFEOWN71
   :alt: codecov
   :target: https://codecov.io/gh/AngryMaciek/angry-moran-simulator
.. image:: https://github.com/AngryMaciek/angry-moran-simulator/workflows/flake8/badge.svg?branch=master
   :alt: flake8
   :target: https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Aflake8
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :alt: Code style: black
   :target: https://github.com/psf/black
.. image:: https://www.codefactor.io/repository/github/angrymaciek/angry-moran-simulator/badge
   :alt: CodeFactor
   :target: https://www.codefactor.io/repository/github/angrymaciek/angry-moran-simulator
.. image:: https://github.com/AngryMaciek/angry-moran-simulator/workflows/publish/badge.svg
   :alt: publish
   :target: https://github.com/AngryMaciek/angry-moran-simulator/actions?query=workflow%3Apublish
.. image:: https://img.shields.io/badge/pypi-1.0.38-blue
   :alt: PyPI
   :target: https://pypi.org/project/moranpycess/
.. image:: https://anaconda.org/angrymaciek/moranpycess/badges/version.svg?service=github
   :alt: conda
   :target: https://anaconda.org/AngryMaciek/moranpycess
.. image:: https://img.shields.io/badge/DockerHub-1.0.38-blue
   :alt: DockerHub
   :target: https://hub.docker.com/r/angrymaciek/moranpycess
.. image:: https://mybinder.org/badge_logo.svg
   :alt: Binder
   :target: https://mybinder.org/v2/gh/AngryMaciek/angry-moran-simulator/master?filepath=tests%2Fusecase.ipynb
.. image:: https://img.shields.io/github/issues/AngryMaciek/angry-moran-simulator
   :alt: GitHub issues
   :target: https://github.com/AngryMaciek/angry-moran-simulator/issues
.. image:: https://img.shields.io/github/license/AngryMaciek/angry-moran-simulator
   :alt: GitHub license
   :target: https://github.com/AngryMaciek/angry-moran-simulator/blob/master/LICENSE
.. image:: https://joss.theoj.org/papers/10.21105/joss.02643/status.svg
   :alt: JOSS
   :target: https://doi.org/10.21105/joss.02643

.. image:: ../images/scheme.svg
   :width: 500
   :alt: Population dynamics: schematic
   :align: center

The following Python package presents a general game-theoretical framework
to carry out scientific simulations according to the Moran model.
Registering distinct types of individuals together with specification of
payoffs between them allows to replicate evolution of the population
and observe growth dynamics.

If you use Moran [Py]cess in your research **please cite the following
article** in your paper:

   Bak et al., (2020). Moran Pycess: a Python package to simulate Moran processes driven by game theory. Journal of Open Source Software, 5(54), 2643, https://doi.org/10.21105/joss.02643

Feel free to inspect the code behind our work at the `official GitHub repository`_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _official GitHub repository: https://github.com/AngryMaciek/angry-moran-simulator
