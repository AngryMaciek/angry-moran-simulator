[![Build Status](https://travis-ci.org/AngryMaciek/angry-moran-simulator.svg?branch=master)](https://travis-ci.org/AngryMaciek/angry-moran-simulator)
[![Coverage Status](https://coveralls.io/repos/github/AngryMaciek/angry-moran-simulator/badge.svg?branch=master&kill_cache=1&service=github)](https://coveralls.io/github/AngryMaciek/angry-moran-simulator?branch=master&kill_cache=1&service=github)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# [Angry] Moran Simulator

![scheme.svg](images/scheme.svg)

## Table of Contents

- [[Angry] Moran Simulator](#angry-moran-simulator)
  - [Table of Contents](#table-of-contents)
  - [General information](#general-information)
  - [Example results](#example-results)
  - [Installation instructions](#installation-instructions)
    - [Download and install Miniconda](#download-and-install-miniconda)
    - [Clone the repository](#clone-the-repository)
    - [Build and activate a virtual environment](#build-and-activate-a-virtual-environment)
    - [Install the package](#install-the-package)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)

## General information

INFO

## Example results

![figure.png](images/figure.png)

> CAPTION

## Installation instructions

Our software is built as a [Python 3] package. Keeping research reproducibility in mind in this repository we provide a recipe for *conda* virtual environment which would contain all the required dependencies.

### Download and install Miniconda

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

### Clone the repository

Please use [git] to clone this repository into a desired location (here: `moran_simulator`) with the following command:

```bash
git clone https://github.com/AngryMaciek/angry-moran-simulator moran_simulator
```

### Build and activate a virtual environment

Dedicated environment might be created and activated with the following commands:

```bash
cd moran_simulator
conda env create -f env/main.yml
conda activate moran-simulator
```

### Install the package

Finally, please install our package into the new virtual environment with the [Python package manager]:

```bash
pip install .
```

## Contributing

This project lives off your contributions, be it in the form of bug reports,
feature requests, discussions, or fixes and other code changes. Please refer
to the [contributing guidelines](CONTRIBUTING.md) if you are interested to
contribute. Please mind the [code of conduct](CODE_OF_CONDUCT.md) for all
interactions with the community.

## Contact

For questions or suggestions regarding the code, please use the
[issue tracker](https://github.com/AngryMaciek/angry-moran-simulator/issues).  
For any other inquiries, please contact us by emails:
* 1
* 2

## License

MIT License

[Python 3]: https://www.python.org/download/releases/3.0/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[git]: https://git-scm.com/
[Python package manager]: <https://pypi.org/project/pip/>

---

Notes:
* https://github.com/Axelrod-Python/Axelrod
* https://axelrod.readthedocs.io/en/stable/
* https://github.com/daffidwilde/matching
* https://en.wikipedia.org/wiki/Moran_process
* https://en.wikipedia.org/wiki/Chicken_(game)#Chicken_and_prisoner's_dilemma
* https://locusofctrl.github.io/blog/posts-output/2019-02-03-male-strategy/  
* missing docstring, comments, flake8
* notebook: payoffs should not be negative?!, comment the code, explain the models
