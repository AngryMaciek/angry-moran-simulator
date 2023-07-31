###############################################################################
#
#   dev commands for the project
#
#   AUTHOR: Maciej_Bak
#   AFFILIATION: University_of_Basel
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: wsciekly.maciek@gmail.com
#   CREATED: 30-12-2020
#   LICENSE: MIT
#
###############################################################################

.PHONY: help test install uninstall format lint build docs clean

help:
	@echo "help - display this message"
	@echo "test - measure code coverage with pytest engine"
	@echo "install - pip-install the package"
	@echo "uninstall - pip-uninstall the package"
	@echo "format - format all package & test files with black"
	@echo "lint - static analysis of all package & test files with flake8"
	@echo "build - build conda package"
	@echo "docs - generate HTML documentation with Sphinx"
	@echo "clean - remove common artifacts from the directory tree"

test:
	@coverage run -m pytest \
	tests/unit/Individual.py \
	tests/unit/MoranProcess.py \
	tests/unit/MoranProcess2D.py \
	tests/unit/MoranProcess3D.py
	@coverage report -m

install:
	@python -m pip install .

uninstall:
	@python -m pip uninstall moranpycess --yes

format:
	@black moranpycess/ tests/unit/
	@isort moranpycess/ tests/unit/

lint:
	@flake8 moranpycess/ tests/unit/

build:
	@conda build . -c conda-forge

docs:
	@cd docs && \
	make html && \
	cd ..

clean:
	@find . -type f -name '*.DS_Store' -delete
	@rm -rf build moranpycess.egg-info
	@rm -rf .coverage .pytest_cache
	@rm -rf moranpycess/__pycache__ tests/unit/__pycache__
