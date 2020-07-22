"""
##############################################################################
#
#   Unit tests for the population evolution
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
    
    def test_classMoranProcessInit(self):
        size_list = [10,0,90]
        label_list = ["A","B","C"]
        mp = ms.MoranProcess(size_list=s, label_list=label_list)
        assert len(mp.population) = 100
