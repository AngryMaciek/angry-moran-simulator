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

# modify PYTHONPATH so that modules can import each other
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# import distinct classes from modules of this package
from .MoranProcess import MoranProcess
from .MoranProcess2D import MoranProcess2D
from .MoranProcess3D import MoranProcess3D
