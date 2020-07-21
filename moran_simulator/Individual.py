"""
##############################################################################
#
#   Implementation of the population individuals
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

class Individual:
    '''
    Abstract representation of an individual in the population
    '''
    def __init__(self, ID, ind_label):
        self.ID = ID
        self.label = ind_label
        self.BirthFitness = None
        self.DeathFitness = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID
    
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def BirthFitness(self):
        return self._BirthFitness

    @BirthFitness.setter
    def BirthFitness(self, BirthFitness):
        self._BirthFitness = BirthFitness

    @property
    def DeathFitness(self):
        return self._DeathFitness

    @DeathFitness.setter
    def DeathFitness(self, DeathFitness):
        self._DeathFitness = DeathFitness
