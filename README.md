[![Build Status](https://travis-ci.org/AngryMaciek/angry-moran-simulator.svg?branch=master)](https://travis-ci.org/AngryMaciek/angry-moran-simulator)
[![Coverage Status](https://coveralls.io/repos/github/AngryMaciek/angry-moran-simulator/badge.svg?branch=master)](https://coveralls.io/github/AngryMaciek/angry-moran-simulator?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# [Angry] Moran Simulator

## Table of Contents

- [[Angry] Moran Simulator](#angry-moran-simulator)
  - [Table of Contents](#table-of-contents)
  - [General information](#general-information)
  - [Installation instructions](#installation-instructions)
  - [Contact](#contact)
  - [License](#license)

## General information

## Installation instructions

## Contact

For questions or suggestions regarding the code, please use the
[issue tracker](https://github.com/AngryMaciek/angry-moran-simulator/issues).  
For any other inquiries, please contact us by emails:
* 1
* 2

## License

MIT License

---

Notes:
* https://arxiv.org/pdf/1811.09552.pdf
* https://github.com/Axelrod-Python/Axelrod
* https://axelrod.readthedocs.io/en/stable/
* https://github.com/daffidwilde/matching
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2728855/pdf/GEN18241141.pdf
* https://en.wikipedia.org/wiki/Moran_process
* https://en.wikipedia.org/wiki/Chicken_(game)#Chicken_and_prisoner's_dilemma
* https://locusofctrl.github.io/blog/posts-output/2019-02-03-male-strategy/
* https://en.wikipedia.org/wiki/Evolutionary_game_theory

---



## Installation instructions

Snakemake is a workflow management system that helps to create and execute data processing pipelines. It requires [Python 3] and can be most easily installed via the [bioconda] channel from the [anaconda cloud] service.

### Step 1: Download and install Miniconda3

To install the latest version of [miniconda] please execute:  
  
[Linux]:
```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source .bashrc
```

[macOS]:
```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
source .bashrc
```

### Step 2: Clone the repository

Please clone this git repository into a desired location (here: binding_scanner_git) with the following command:

```bash
git clone https://github.com/zavolanlab/binding-scanner.git binding_scanner_git
```

Cloning repositories requires [git] to be installed.

### Step 3: Build and activate virtual environment for Binding Scanner

To ease the users in the installation process we have prepared a recipe for a *conda* virtual environment which contains all the software needed in order to run Binding Scanner. This environment might be created by the following script:

```bash
bash binding_scanner_git/scripts/create-conda-environment-main.sh
```

Following the built *conda* environment may be activated with:

```bash
conda activate binding-scanner
```





[Snakemake]: https://snakemake.readthedocs.io/en/stable/
[rule-graph]: images/rulegraph.svg
[Python 3]: https://www.python.org/download/releases/3.0/
[bioconda]: https://bioconda.github.io/
[anaconda cloud]: https://anaconda.org/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[git]: https://git-scm.com/
[ATtRACT]: https://attract.cnic.es/index
[res-issue-tracker]: <https://github.com/zavolanlab/binding-scanner/issues>
[res-zavolab]: <https://zavolan.biozentrum.unibas.ch/>




## Contributing

This project lives off your contributions, be it in the form of bug reports,
feature requests, discussions, or fixes and other code changes. Please refer
to the [contributing guidelines](CONTRIBUTING.md) if you are interested to
contribute. Please mind the [code of conduct](CODE_OF_CONDUCT.md) for all
interactions with the community.