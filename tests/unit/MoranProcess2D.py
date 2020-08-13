"""
##############################################################################
#
#   Unit tests for the 2D population evolution
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
import numpy as np
import moranpycess
import pytest


class TestClass:
    """Test class for pytest package."""

    def test_classMoranProcess2DInit(self):
        """Test the initializer."""
        # initialize an instance of MoranProcess:
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test all the attributes:
        assert mp.init_size_list == size_list
        assert mp.curr_size_list == size_list
        assert mp.init_label_list == label_list
        assert mp.population.shape == grid.shape
        assert mp.w == 0.5
        assert mp.TransitionMatrix is None

        comparison = mp.init_grid == grid
        assert comparison.all()
        comparison = mp.curr_grid == grid
        assert comparison.all()

        comparison = mp.BirthPayoffMatrix == BirthPayoffMatrix
        assert comparison.all()
        comparison = mp.DeathPayoffMatrix == DeathPayoffMatrix
        assert comparison.all()

    def test_classMoranProcessWrongInit(self):
        """Test assertion errors in the initializer."""
        # test improper lists error
        size_list = [3, 1]
        label_list = ["A", "B", "C"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Birth Payoff Matrix
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[10, 20, 20], [30, 40, 40], [1, 1, 1]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Death Payoff Matrix
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20, 20], [30, 40, 40], [1, 1, 1]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper population grid 1
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["C", "B"]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper population grid 2
        size_list = [2, 2]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Transition Matrix
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20], [30, 40]])
        TransitionMatrix = np.array([[0.0], [0.0]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
                TransitionMatrix=TransitionMatrix,
            )
        # test improper values in Transition Matrix
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20], [30, 40]])
        TransitionMatrix = np.array([[0.5, 0.4], [0.5, 0.5]])
        with pytest.raises(Exception):
            mp = moranpycess.MoranProcess2D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
                TransitionMatrix=TransitionMatrix,
            )
