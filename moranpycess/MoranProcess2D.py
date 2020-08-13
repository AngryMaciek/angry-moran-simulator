"""
##############################################################################
#
#   Implementation of the 2D population evolution
#
#   AUTHOR: Maciej_Bak
#   AFFILIATION: University_of_Basel
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: wsciekly.maciek@gmail.com
#   CREATED: 13-08-2020
#   LICENSE: MIT
#
##############################################################################
"""

# imports
import random
import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import moranpycess


class MoranProcess2D:
    """General Moran Process with multiple types of individuals."""

    def __init__(
        self,
        size_list,
        label_list,
        grid,
        BirthPayoffMatrix,
        DeathPayoffMatrix,
        TransitionMatrix=None,
    ):
        """Class initializer."""

        # check if the argument lists length match
        try:
            assert len(size_list) == len(label_list)
        except AssertionError as e:
            e.args += ("Mismatch length of size and label lists",)
            raise

        # keep record of the argument lists
        self.init_size_list = size_list
        self.curr_size_list = size_list
        self.init_label_list = label_list
        self.init_grid = grid
        self.curr_grid = grid

        # check if the argument matrices shape match
        try:
            assert len(BirthPayoffMatrix.shape) == 2
            assert (
                BirthPayoffMatrix.shape[0]
                == BirthPayoffMatrix.shape[1]
                == len(label_list)
            )
        except AssertionError as e:
            e.args += ("Invalid Payoff Matrix",)
            raise
        try:
            assert len(DeathPayoffMatrix.shape) == 2
            assert (
                DeathPayoffMatrix.shape[0]
                == DeathPayoffMatrix.shape[1]
                == len(label_list)
            )
        except AssertionError as e:
            e.args += ("Invalid Payoff Matrix",)
            raise

        # keep record of the argument matrices
        self.BirthPayoffMatrix = BirthPayoffMatrix
        self.DeathPayoffMatrix = DeathPayoffMatrix

        # introduce a payoff weight for the fitness calculation
        self.w = 0.5

        # check if the grid argument is correct
        try:
            unique, counts = np.unique(grid, return_counts=True)
            grid_dict = dict(zip(unique, counts))
            assert sorted(unique) == sorted(self.init_label_list)
            for i in range(len(self.init_label_list)):
                assert self.init_size_list[i] == grid_dict[self.init_label_list[i]]
        except AssertionError as e:
            e.args += ("Invalid Population Grid",)
            raise

        # initialize a list of Individuals
        ID_counter = 0
        self.population = np.empty(
            (self.init_grid.shape[0], self.init_grid.shape[1]),
            dtype=moranpycess.Individual,
        )
        for x in range(self.init_grid.shape[0]):
            for y in range(self.init_grid.shape[1]):
                self.population[x, y] = moranpycess.Individual(
                    ID=ID_counter, ind_label=self.init_grid[x, y]
                )
                ID_counter += 1

        # calculate entropy of the types distribution
        self.Entropy = 0
        self.UpdateEntropy()

        # assign the transition matrix between types
        if TransitionMatrix is not None:
            try:
                # check if the argument matrix shape match
                assert len(TransitionMatrix.shape) == 2
                assert (
                    TransitionMatrix.shape[0]
                    == TransitionMatrix.shape[1]
                    == len(label_list)
                )
                # check if the values are correct
                for v in np.sum(TransitionMatrix, axis=1):
                    assert v == 1.0
            except AssertionError as e:
                e.args += ("Invalid Transition Matrix",)
                raise
        self.TransitionMatrix = TransitionMatrix

    def UpdateEntropy(self):
        """Calculate entropy of Individual types for the population."""
        self.Entropy = 0
        for type_size in self.curr_size_list:
            fraction = float(type_size) / self.population.size
            if fraction != 0.0:
                self.Entropy -= fraction * np.log2(fraction)