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
import pytest
import random
from .context import MoranProcess, exceptions


class TestClass:
    """Test class for pytest package."""

    def test_classMoranProcessInit(self):
        """Test the initializer."""
        # initialize an instance of MoranProcess:
        size_list = [10, 90]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        mp = MoranProcess.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test all the attributes:
        assert mp.init_size_list == size_list
        assert mp.curr_size_list == size_list
        assert mp.init_label_list == label_list
        assert len(mp.population) == sum(size_list)
        assert mp.w == 0.5
        assert mp.TransitionMatrix is None

        comparison = mp.BirthPayoffMatrix == BirthPayoffMatrix
        assert comparison.all()
        comparison = mp.DeathPayoffMatrix == DeathPayoffMatrix
        assert comparison.all()

        assert round(mp.AvgBirthPayoffDict["A"], 3) == 19.091
        assert round(mp.AvgBirthPayoffDict["B"], 3) == 38.990

        assert (
            round(mp.population[10].AvgBirthPayoff, 3) == 19.091
            or round(mp.population[10].AvgBirthPayoff, 3) == 38.990
        )
        assert (
            round(mp.population[20].AvgBirthPayoff, 3) == 19.091
            or round(mp.population[20].AvgBirthPayoff, 3) == 38.990
        )
        assert (
            round(mp.population[30].AvgBirthPayoff, 3) == 19.091
            or round(mp.population[30].AvgBirthPayoff, 3) == 38.990
        )
        assert (
            round(mp.population[40].AvgBirthPayoff, 3) == 19.091
            or round(mp.population[40].AvgBirthPayoff, 3) == 38.990
        )
        assert (
            round(mp.population[50].AvgBirthPayoff, 3) == 19.091
            or round(mp.population[50].AvgBirthPayoff, 3) == 38.990
        )

        assert round(mp.AvgDeathPayoffDict["A"], 3) == 1.909
        assert round(mp.AvgDeathPayoffDict["B"], 3) == 3.899

        assert (
            round(mp.population[10].AvgDeathPayoff, 3) == 1.909
            or round(mp.population[10].AvgDeathPayoff, 3) == 3.899
        )
        assert (
            round(mp.population[20].AvgDeathPayoff, 3) == 1.909
            or round(mp.population[20].AvgDeathPayoff, 3) == 3.899
        )
        assert (
            round(mp.population[30].AvgDeathPayoff, 3) == 1.909
            or round(mp.population[30].AvgDeathPayoff, 3) == 3.899
        )
        assert (
            round(mp.population[40].AvgDeathPayoff, 3) == 1.909
            or round(mp.population[40].AvgDeathPayoff, 3) == 3.899
        )
        assert (
            round(mp.population[50].AvgDeathPayoff, 3) == 1.909
            or round(mp.population[50].AvgDeathPayoff, 3) == 3.899
        )

        assert round(mp.BirthFitnessDict["A"], 3) == 10.045
        assert round(mp.BirthFitnessDict["B"], 3) == 19.995

        assert (
            round(mp.population[10].BirthFitness, 3) == 10.045
            or round(mp.population[10].BirthFitness, 3) == 19.995
        )
        assert (
            round(mp.population[20].BirthFitness, 3) == 10.045
            or round(mp.population[20].BirthFitness, 3) == 19.995
        )
        assert (
            round(mp.population[30].BirthFitness, 3) == 10.045
            or round(mp.population[30].BirthFitness, 3) == 19.995
        )
        assert (
            round(mp.population[40].BirthFitness, 3) == 10.045
            or round(mp.population[40].BirthFitness, 3) == 19.995
        )
        assert (
            round(mp.population[50].BirthFitness, 3) == 10.045
            or round(mp.population[50].BirthFitness, 3) == 19.995
        )

        assert round(mp.DeathFitnessDict["A"], 3) == 1.455
        assert round(mp.DeathFitnessDict["B"], 3) == 2.449

        assert (
            round(mp.population[10].DeathFitness, 3) == 1.455
            or round(mp.population[10].DeathFitness, 3) == 2.449
        )
        assert (
            round(mp.population[20].DeathFitness, 3) == 1.455
            or round(mp.population[20].DeathFitness, 3) == 2.449
        )
        assert (
            round(mp.population[30].DeathFitness, 3) == 1.455
            or round(mp.population[30].DeathFitness, 3) == 2.449
        )
        assert (
            round(mp.population[40].DeathFitness, 3) == 1.455
            or round(mp.population[40].DeathFitness, 3) == 2.449
        )
        assert (
            round(mp.population[50].DeathFitness, 3) == 1.455
            or round(mp.population[50].DeathFitness, 3) == 2.449
        )

    def test_classMoranProcess_roulette_wheel_selection_Birth(self):
        """Test the roulette wheel selection method for Birth."""
        # initialize an instance of MoranProcess:
        size_list = [4, 1]
        label_list = ["abc", "def"]
        BirthPayoffMatrix = np.array([[100, 100], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        mp = MoranProcess.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the selection:
        random.seed(0)
        ind = mp._roulette_wheel_selection_Birth()
        assert ind.ID == 3
        assert ind.label == "abc"

    def test_classMoranProcess_roulette_wheel_selection_Death(self):
        """Test the roulette wheel selection method for Death."""
        # initialize an instance of MoranProcess:
        size_list = [15, 15]
        label_list = ["XYZ", "ZYX"]
        BirthPayoffMatrix = np.array([[1, 1], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [100, 100]])
        mp = MoranProcess.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the selection:
        random.seed(0)
        ind = mp._roulette_wheel_selection_Death()
        assert ind.ID == 27
        assert ind.label == "ZYX"

    def test_classMoranProcess_simulate(self):
        """Test the simulation process."""
        # initialize an instance of MoranProcess:
        size_list = [10, 10]
        label_list = ["a", "b"]
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[0.1, 0.2], [0.3, 0.4]])
        mp = MoranProcess.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the simulation:
        random.seed(0)
        simulation = mp.simulate(generations=10)
        assert round(mp.AvgBirthPayoffDict["a"], 3) == 1.737
        assert round(mp.AvgBirthPayoffDict["b"], 3) == 3.684
        assert round(mp.AvgDeathPayoffDict["a"], 3) == 0.174
        assert round(mp.AvgDeathPayoffDict["b"], 3) == 0.368
        assert mp.curr_size_list == [6, 14]
        assert simulation.shape == (11, 11)

    def test_classMoranProcessWrongInit(self):
        """Test assertion errors in the initializer."""
        # test improper lists error
        size_list = [10, 90]
        label_list = ["A", "B", "C"]
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(AssertionError):
            MoranProcess.MoranProcess(
                size_list=size_list,
                label_list=label_list,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Birth Payoff Matrix
        size_list = [10, 90]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[10, 20, 20], [30, 40, 40], [1, 1, 1]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(AssertionError):
            MoranProcess.MoranProcess(
                size_list=size_list,
                label_list=label_list,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Death Payoff Matrix
        size_list = [10, 90]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20, 20], [30, 40, 40], [1, 1, 1]])
        with pytest.raises(AssertionError):
            MoranProcess.MoranProcess(
                size_list=size_list,
                label_list=label_list,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Transition Matrix
        size_list = [10, 90]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20], [30, 40]])
        TransitionMatrix = np.array([[0.0], [0.0]])
        with pytest.raises(AssertionError):
            MoranProcess.MoranProcess(
                size_list=size_list,
                label_list=label_list,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
                TransitionMatrix=TransitionMatrix,
            )
        # test improper values in Transition Matrix
        size_list = [10, 90]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20], [30, 40]])
        TransitionMatrix = np.array([[0.5, 0.4], [0.5, 0.5]])
        expected_error_msg = "Incorrect value for Transition Matrix."
        expected_error_msg += " "
        expected_error_msg += "Transition probabilities need to add up to 1.0."
        with pytest.raises(exceptions.IncorrectValueError, match=expected_error_msg):
            MoranProcess.MoranProcess(
                size_list=size_list,
                label_list=label_list,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
                TransitionMatrix=TransitionMatrix,
            )

    def test_plots(self):
        """Test the plotting functions."""
        # initialize an instance of MoranProcess (PD):
        size_list = [990, 10]
        label_list = ["cooperate", "defect"]
        BirthPayoffMatrix = np.array([[3, 0], [5, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        mp = MoranProcess.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # run the simulation:
        random.seed(0)
        simulation = mp.simulate(generations=25000)
        # test the plotting:
        mp.PlotSize(simulation, "./tests/output/PD_size.png")
        mp.PlotAvgBirthPayoff(simulation, "./tests/output/PD_AvgBirthPayoff.png")
        mp.PlotAvgDeathPayoff(simulation, "./tests/output/PD_AvgDeathPayoff.png")
        mp.PlotBirthFitness(simulation, "./tests/output/PD_BirthFitness.png")
        mp.PlotDeathFitness(simulation, "./tests/output/PD_DeathFitness.png")
        mp.PlotEntropy(simulation, "./tests/output/PD_Entropy.png")
        assert True  # mark that no error was raised before

    def test_MoranProcessWithTransitionMatrix(self):
        """Test the simulation with a Transition Matrix."""

        # initialize an instance of MoranProcess:
        size_list = [10, 0]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[1, 1], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        TransitionMatrix = np.array([[0.5, 0.5], [0.0, 1.0]])
        mp = MoranProcess.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
            TransitionMatrix=TransitionMatrix,
        )

        comparison = mp.TransitionMatrix == TransitionMatrix
        assert comparison.all()

        # run the simulation:
        random.seed(0)
        mp.simulate(generations=10)
        assert mp.curr_size_list == [0, 10]
