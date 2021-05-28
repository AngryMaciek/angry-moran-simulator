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

# imports
import os
import sys
from .Individual import Individual
from .MoranProcess import MoranProcess
from .MoranProcess2D import MoranProcess2D
from .MoranProcess3D import MoranProcess3D
from .CustomExceptions import IncorrectValueError

# modify PYTHONPATH so that modules can import each other
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
