"""
##############################################################################
#
#   Implementation of the population evolution
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
import moran_simulator as ms

class MoranProcess:
    '''
    General Moran Process with multiple types of individuals
    '''
    def __init__(self, size_list, label_list, BirthPayoffMatrix, DeathPayoffMatrix):

        try:
            assert len(size_list) == len(label_list)
        except AssertionError as e:
            e.args += ("Mismatch length of size and label lists")
            raise

        ID_counter = 0
        self.population = []
        for label_index in range(len(label_list)):
            for i in range(size_list[label_index]):
                self.population.append(
                    ms.Individual(ID=ID_counter, ind_label=label_list[label_index])
                )
                ID_counter += 1
        
        self.init_size_list = size_list
        self.init_label_list = label_list

        try:
            assert len(BirthPayoffMatrix.shape) == 2
            assert BirthPayoffMatrix.shape[0] == BirthPayoffMatrix.shape[1] == len(label_list)
        except AssertionError as e:
            e.args += (".")
            raise

        try:
            assert len(DeathPayoffMatrix.shape) == 2
            assert DeathPayoffMatrix.shape[0] == DeathPayoffMatrix.shape[1] == len(label_list)
        except AssertionError as e:
            e.args += (".")
            raise

        self.BirthPayoffMatrix = BirthPayoffMatrix
        self.DeathPayoffMatrix = DeathPayoffMatrix
        

    # a method to count labels, counter
