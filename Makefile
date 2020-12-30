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

.PHONY: help test install uninstall docs

help:
	@echo "help - display this message"
	@echo "test - measure code coverage with pytest engine"
	@echo "install - pip-install the package"
	@echo "uninstall - pip-uninstall the package"
#	@echo "docs - generate Sphinx HTML documentation"

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

#docs:
#	$(MAKE) -C docs html
