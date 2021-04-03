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

.PHONY: help test install uninstall format lint docs

help:
	@echo "help - display this message"
	@echo "test - measure code coverage with pytest engine"
	@echo "install - pip-install the package"
	@echo "uninstall - pip-uninstall the package"
	@echo "format - format all package & test files with black"
	@echo "lint - static analysis of all package & test files with flake8"
	@echo "docs - generate HTML documentation with Sphinx"

test:
	coverage run -m pytest \
	tests/unit/Individual.py \
	tests/unit/MoranProcess.py \
	tests/unit/MoranProcess2D.py \
	tests/unit/MoranProcess3D.py
	coverage report -m

install:
	python -m pip install .

uninstall:
	python -m pip uninstall moranpycess --yes

format:
	black \
	moranpycess/__init__.py \
	moranpycess/Individual.py \
	moranpycess/MoranProcess.py \
	moranpycess/MoranProcess2D.py \
	moranpycess/MoranProcess3D.py \
	tests/unit/context.py \
	tests/unit/Individual.py \
	tests/unit/MoranProcess.py \
	tests/unit/MoranProcess2D.py \
	tests/unit/MoranProcess3D.py \

lint:
	flake8 --max-line-length=88 --ignore F401 moranpycess/__init__.py
	flake8 --max-line-length=88 moranpycess/Individual.py
	flake8 --max-line-length=95 --ignore F401,E231,W503,E741 moranpycess/MoranProcess.py
	flake8 --max-line-length=101 --ignore F401,E231,W503,E741 moranpycess/MoranProcess2D.py
	flake8 --max-line-length=101 --ignore F401,E231,W503,E741 moranpycess/MoranProcess3D.py
	flake8 --max-line-length=88 --ignore F401,E402 tests/unit/context.py
	flake8 --max-line-length=88 tests/unit/Individual.py
	flake8 --max-line-length=88 tests/unit/MoranProcess.py
	flake8 --max-line-length=88 --ignore E231 tests/unit/MoranProcess2D.py
	flake8 --max-line-length=88 --ignore E231 tests/unit/MoranProcess3D.py

docs:
	cd docs && \
	make html && \
	cd ..
