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
from .context import moranpycess


class TestClass:
    """Test class for pytest package."""

    def test_classIndividualInit(self):
        """Test the initializer."""
        # initialize an instance of Individual:
        ind1 = moranpycess.Individual.Individual(100, "A")
        # test all the attributes:
        assert ind1.ID == 100
        assert ind1.label == "A"
        assert ind1.AvgBirthPayoff is None
        assert ind1.AvgDeathPayoff is None
        assert ind1.BirthFitness is None
        assert ind1.DeathFitness is None
