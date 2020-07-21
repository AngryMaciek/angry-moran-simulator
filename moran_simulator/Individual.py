"""
##############################################################################
#
#   Init file for the package
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
        self.ID = ID # private, + getter
        self.label = ind_label # private, + getter
        self.BirthFitness = None
        self.DeathFitness = None
