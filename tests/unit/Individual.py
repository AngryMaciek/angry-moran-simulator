"""
##############################################################################
#
#   Unit tests for the population individuals
#
#   AUTHOR: Maciej_Bak
#   AFFILIATION: University_of_Basel
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: wsciekly.maciek@gmail.com
#   CREATED: 20-07-2020
#   LICENSE: MIT
#
##############################################################################
"""

# imports
import moran_simulator as ms


class TestClass:
    def test_classIndividualInit(self):
        ind1 = ms.Individual(100, "A")
        assert ind1.ID == 100
        assert ind1.label == "A"
        assert ind1.BirthFitness is None
        assert ind1.DeathFitness is None
