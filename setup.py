"""
##############################################################################
#
#   Setup file for the package
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
from setuptools import setup

setup(
    name="moran-simulator",
    version="0.0.1",
    author="Maciek Bak",
    author_email="wsciekly.maciek@gmail.com",
    description="Moran Process for multiple types of individuals",
    url="https://github.com/AngryMaciek/angry-moran-simulator",
    packages=["moran_simulator"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.4',
    zip_safe=False
)
