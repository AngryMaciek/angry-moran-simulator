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
import numpy as np
import pandas as pd
import moran_simulator as ms

class TestClass:
    
    def test_classMoranProcessInit(self):
        size_list = [10,90]
        label_list = ["A","B"]
        BirthPayoffMatrix = np.array([[0,0],[0,0]])
        DeathPayoffMatrix = np.array([[0,0],[0,0]])
        mp = ms.MoranProcess(size_list=size_list, label_list=label_list, BirthPayoffMatrix=BirthPayoffMatrix, DeathPayoffMatrix=DeathPayoffMatrix)
        assert len(mp.population) == 100
