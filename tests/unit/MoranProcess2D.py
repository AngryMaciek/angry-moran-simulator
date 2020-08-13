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
        # initialize an instance of MoranProcess2D:
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

    def test_classMoranProcess2DWrongInit(self):
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

    def test_classMoranProcess2DUpdateBirthPayoff(self):
        """Test the UpdateBirthPayoff function."""
        # initialize an instance of MoranProcess2D:
        size_list = [5, 6, 1]
        label_list = ["A", "B", "C"]
        grid = np.array(
            [["A", "B", "B", "B"], ["A", "C", "A", "B"], ["A", "B", "A", "B"],]
        )

        BirthPayoffMatrix = np.array([[1, 5, 25], [0.1, 7, 0.02], [0.99, 9.52, 0.111]])
        DeathPayoffMatrix = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[0, 0].AvgBirthPayoff, 3) == 6.500
        assert round(mp.population[1, 1].AvgBirthPayoff, 3) == 4.189

    def test_classMoranProcess2DUpdateDeathPayoff(self):
        """Test the UpdateDeathPayoff function."""
        # initialize an instance of MoranProcess2D:
        size_list = [5, 6, 1]
        label_list = ["A", "B", "C"]
        grid = np.array(
            [["A", "B", "B", "B"], ["A", "C", "A", "B"], ["A", "B", "A", "B"],]
        )

        BirthPayoffMatrix = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        DeathPayoffMatrix = np.array([[1, 5, 25], [0.1, 7, 0.02], [0.99, 9.52, 0.111]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[0, 0].AvgDeathPayoff, 3) == 6.500
        assert round(mp.population[1, 1].AvgDeathPayoff, 3) == 4.189

    def test_classMoranProcess2DUpdateBirthFitness(self):
        """Test the UpdateBirthFitness function."""
        # initialize an instance of MoranProcess2D:
        size_list = [5, 6, 1]
        label_list = ["A", "B", "C"]
        grid = np.array(
            [["A", "B", "B", "B"], ["A", "C", "A", "B"], ["A", "B", "A", "B"],]
        )
        BirthPayoffMatrix = np.array([[1, 5, 25], [0.1, 7, 0.02], [0.99, 9.52, 0.111]])
        DeathPayoffMatrix = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[0, 0].BirthFitness, 3) == 3.750
        assert round(mp.population[1, 1].BirthFitness, 3) == 2.594

    def test_classMoranProcess2DUpdateDeathFitness(self):
        """Test the UpdateDeathFitness function."""
        # initialize an instance of MoranProcess2D:
        size_list = [5, 6, 1]
        label_list = ["A", "B", "C"]
        grid = np.array(
            [["A", "B", "B", "B"], ["A", "C", "A", "B"], ["A", "B", "A", "B"],]
        )

        BirthPayoffMatrix = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        DeathPayoffMatrix = np.array([[1, 5, 25], [0.1, 7, 0.02], [0.99, 9.52, 0.111]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[0, 0].DeathFitness, 3) == 3.750
        assert round(mp.population[1, 1].DeathFitness, 3) == 2.594

    def test_classMoranProcess2D_roulette_wheel_selection_Birth(self):
        """Test the roulette wheel selection method for Birth."""
        # initialize an instance of MoranProcess2D:
        size_list = [3, 1]
        label_list = ["A", "B"]
        grid = np.array([["A", "A"], ["A", "B"]])
        BirthPayoffMatrix = np.array([[1, 1], [100, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the selection:
        random.seed(0)
        (x, y) = mp.roulette_wheel_selection_Birth()
        ind = mp.population[x, y]
        assert ind.ID == 3
        assert ind.label == "B"

    def test_classMoranProcess2D_roulette_wheel_selection_Death(self):
        """Test the roulette wheel selection method for Death."""
        # initialize an instance of MoranProcess2D:
        size_list = [1, 8]
        label_list = ["A", "B"]
        grid = np.array([["A", "B", "B"], ["B", "B", "B"], ["B", "B", "B"],])
        BirthPayoffMatrix = np.array([[1, 1], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 100], [1, 1]])
        mp = moranpycess.MoranProcess2D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the selection:
        random.seed(0)
        (x, y) = mp.roulette_wheel_selection_Death(1, 1)
        ind = mp.population[x, y]
        assert ind.ID == 0
        assert ind.label == "A"
