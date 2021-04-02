"""
##############################################################################
#
#   Unit tests for the 3D population evolution
#
#   AUTHOR: Maciej_Bak
#   AFFILIATION: University_of_Basel
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: wsciekly.maciek@gmail.com
#   CREATED: 15-08-2020
#   LICENSE: MIT
#
##############################################################################
"""

# imports
import numpy as np
import pytest
import random
from context import moranpycess


class TestClass:
    """Test class for pytest package."""

    def test_classMoranProcess3DInit(self):
        """Test the initializer."""
        # initialize an instance of MoranProcess3D:
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["A", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        mp = moranpycess.MoranProcess3D(
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

    def test_classMoranProcess3DWrongInit(self):
        """Test assertion errors in the initializer."""
        # test improper lists error
        size_list = [7, 1]
        label_list = ["A", "B", "C"]
        grid = np.array([[["A", "A"], ["A", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(AssertionError):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Birth Payoff Matrix
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["A", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[10, 20, 20], [30, 40, 40], [1, 1, 1]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(AssertionError):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Death Payoff Matrix
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["A", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20, 20], [30, 40, 40], [1, 1, 1]])
        with pytest.raises(AssertionError):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper population grid 1
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["C", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(AssertionError):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper population grid 2
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["B", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        with pytest.raises(AssertionError):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
            )
        # test improper Transition Matrix
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["A", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20], [30, 40]])
        TransitionMatrix = np.array([[0.0], [0.0]])
        with pytest.raises(AssertionError):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
                TransitionMatrix=TransitionMatrix,
            )
        # test improper values in Transition Matrix
        size_list = [7, 1]
        label_list = ["A", "B"]
        grid = np.array([[["A", "A"], ["A", "B"]], [["A", "A"], ["A", "A"]]])
        BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
        DeathPayoffMatrix = np.array([[10, 20], [30, 40]])
        TransitionMatrix = np.array([[0.5, 0.4], [0.5, 0.5]])
        expected_error_msg = "Incorrect value for Transition Matrix."
        expected_error_msg += " "
        expected_error_msg += "Transition probabilities need to add up to 1.0."
        with pytest.raises(moranpycess.IncorrectValueError, match=expected_error_msg):
            moranpycess.MoranProcess3D(
                size_list=size_list,
                label_list=label_list,
                grid=grid,
                BirthPayoffMatrix=BirthPayoffMatrix,
                DeathPayoffMatrix=DeathPayoffMatrix,
                TransitionMatrix=TransitionMatrix,
            )

    def test_classMoranProcess3DUpdateBirthPayoff(self):
        """Test the UpdateBirthPayoff function."""
        # initialize an instance of MoranProcess3D:
        size_list = [47, 11, 5, 1]
        label_list = ["A", "B", "C", "D"]
        grid = np.array(
            [
                [
                    ["A", "B", "A", "B"],
                    ["B", "A", "C", "C"],
                    ["C", "D", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "A"],
                    ["A", "A", "B", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["A", "B", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "B", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["C", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "C", "A", "A"],
                ],
            ]
        )

        BirthPayoffMatrix = np.array(
            [
                [1, 7, 11, 29],
                [0.1, 0.5, 0.22, 0.99],
                [0.001, 0.005, 0.0022, 0.0099],
                [1000, 7000, 1234, 0],
            ]
        )
        DeathPayoffMatrix = np.array(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[3, 0, 3].AvgBirthPayoff, 3) == 0.175
        assert round(mp.population[1, 1, 3].AvgBirthPayoff, 3) == 3.077
        assert round(mp.population[1, 2, 1].AvgBirthPayoff, 3) == 3.769

    def test_classMoranProcess3DUpdateDeathPayoff(self):
        """Test the UpdateDeathPayoff function."""
        # initialize an instance of MoranProcess3D:
        size_list = [47, 11, 5, 1]
        label_list = ["A", "B", "C", "D"]
        grid = np.array(
            [
                [
                    ["A", "B", "A", "B"],
                    ["B", "A", "C", "C"],
                    ["C", "D", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "A"],
                    ["A", "A", "B", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["A", "B", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "B", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["C", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "C", "A", "A"],
                ],
            ]
        )

        BirthPayoffMatrix = np.array(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        DeathPayoffMatrix = np.array(
            [
                [1, 7, 11, 29],
                [0.1, 0.5, 0.22, 0.99],
                [0.001, 0.005, 0.0022, 0.0099],
                [1000, 7000, 1234, 0],
            ]
        )
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[3, 0, 3].AvgDeathPayoff, 3) == 0.175
        assert round(mp.population[1, 1, 3].AvgDeathPayoff, 3) == 3.077
        assert round(mp.population[1, 2, 1].AvgDeathPayoff, 3) == 3.769

    def test_classMoranProcess3DUpdateBirthFitness(self):
        """Test the UpdateBirthFitness function."""
        # initialize an instance of MoranProcess3D:
        size_list = [47, 11, 5, 1]
        label_list = ["A", "B", "C", "D"]
        grid = np.array(
            [
                [
                    ["A", "B", "A", "B"],
                    ["B", "A", "C", "C"],
                    ["C", "D", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "A"],
                    ["A", "A", "B", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["A", "B", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "B", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["C", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "C", "A", "A"],
                ],
            ]
        )

        BirthPayoffMatrix = np.array(
            [
                [1, 7, 11, 29],
                [0.1, 0.5, 0.22, 0.99],
                [0.001, 0.005, 0.0022, 0.0099],
                [1000, 7000, 1234, 0],
            ]
        )
        DeathPayoffMatrix = np.array(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[3, 0, 3].BirthFitness, 3) == 0.588
        assert round(mp.population[1, 1, 3].BirthFitness, 3) == 2.038
        assert round(mp.population[1, 2, 1].BirthFitness, 3) == 2.385

    def test_classMoranProcess3DUpdateDeathFitness(self):
        """Test the UpdateDeathFitness function."""
        # initialize an instance of MoranProcess3D:
        size_list = [47, 11, 5, 1]
        label_list = ["A", "B", "C", "D"]
        grid = np.array(
            [
                [
                    ["A", "B", "A", "B"],
                    ["B", "A", "C", "C"],
                    ["C", "D", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "A"],
                    ["A", "A", "B", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["A", "B", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "B", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["C", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "C", "A", "A"],
                ],
            ]
        )

        BirthPayoffMatrix = np.array(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        DeathPayoffMatrix = np.array(
            [
                [1, 7, 11, 29],
                [0.1, 0.5, 0.22, 0.99],
                [0.001, 0.005, 0.0022, 0.0099],
                [1000, 7000, 1234, 0],
            ]
        )
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert round(mp.population[3, 0, 3].DeathFitness, 3) == 0.588
        assert round(mp.population[1, 1, 3].DeathFitness, 3) == 2.038
        assert round(mp.population[1, 2, 1].DeathFitness, 3) == 2.385

    def test_classMoranProcess3D_roulette_wheel_selection_Birth(self):
        """Test the roulette wheel selection method for Birth."""
        # initialize an instance of MoranProcess3D:
        size_list = [26, 1]
        label_list = ["A", "B"]
        grid = np.array(
            [
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
                [["A", "A", "A"], ["A", "B", "A"], ["A", "A", "A"],],
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
            ]
        )

        BirthPayoffMatrix = np.array([[1, 1], [1000, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the selection:
        random.seed(0)
        (x, y, z) = mp.roulette_wheel_selection_Birth()
        ind = mp.population[x, y, z]
        assert ind.ID == 13
        assert ind.label == "B"

    def test_classMoranProcess3D_roulette_wheel_selection_Death(self):
        """Test the roulette wheel selection method for Death."""
        # initialize an instance of MoranProcess3D:
        size_list = [26, 1]
        label_list = ["A", "B"]
        grid = np.array(
            [
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
                [["A", "A", "A"], ["A", "B", "A"], ["A", "A", "A"],],
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
            ]
        )

        BirthPayoffMatrix = np.array([[1, 1], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1000, 1]])
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the selection:
        random.seed(0)
        (x, y, z) = mp.roulette_wheel_selection_Death(0, 0, 0)
        ind = mp.population[x, y, z]
        assert ind.ID == 13
        assert ind.label == "B"

    def test_classMoranProcess3D_simulate(self):
        """Test the simulation process."""
        # initialize an instance of MoranProcess3D:
        size_list = [47, 11, 5, 1]
        label_list = ["A", "B", "C", "D"]
        grid = np.array(
            [
                [
                    ["A", "B", "A", "B"],
                    ["B", "A", "C", "C"],
                    ["C", "D", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "A"],
                    ["A", "A", "B", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["A", "B", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "B", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["C", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "C", "A", "A"],
                ],
            ]
        )
        BirthPayoffMatrix = np.array(
            [
                [1, 7, 11, 29],
                [0.1, 0.5, 0.22, 0.99],
                [0.001, 0.005, 0.0022, 0.0099],
                [1000, 7000, 1234, 0],
            ]
        )
        DeathPayoffMatrix = np.array(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the simulation:
        random.seed(0)
        simulation = mp.simulate(generations=10)
        assert mp.curr_size_list == [42, 10, 4, 8]
        assert simulation.shape == (11, 5)

    def test_plots3D(self):
        """Test the plotting functions."""
        # initialize an instance of MoranProcess3D:
        size_list = [47, 11, 5, 1]
        label_list = ["A", "B", "C", "D"]
        grid = np.array(
            [
                [
                    ["A", "B", "A", "B"],
                    ["B", "A", "C", "C"],
                    ["C", "D", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "A"],
                    ["A", "A", "B", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["A", "B", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "A", "B", "A"],
                ],
                [
                    ["A", "B", "A", "B"],
                    ["C", "A", "A", "A"],
                    ["A", "A", "A", "A"],
                    ["A", "C", "A", "A"],
                ],
            ]
        )
        BirthPayoffMatrix = np.array(
            [
                [1, 7, 11, 29],
                [0.1, 0.5, 0.22, 0.99],
                [0.001, 0.005, 0.0022, 0.0099],
                [1000, 7000, 1234, 0],
            ]
        )
        DeathPayoffMatrix = np.array(
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        )
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        # test the simulation:
        random.seed(0)
        simulation = mp.simulate(generations=10)
        # test the plotting:
        mp.PlotSize3D(simulation, "./tests/output/3D_size.png")
        mp.PlotEntropy3D(simulation, "./tests/output/3D_Entropy.png")
        assert True  # mark that no error was raised before

    def test_MoranProcess3DWithTransitionMatrix(self):
        """Test the 3D simulation with a Transition Matrix."""
        # initialize an instance of MoranProcess3D:
        size_list = [27, 0]
        label_list = ["A", "B"]
        grid = np.array(
            [
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
                [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"],],
            ]
        )

        BirthPayoffMatrix = np.array([[1, 1], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        TransitionMatrix = np.array([[0.0, 1.0], [0.0, 1.0]])
        mp = moranpycess.MoranProcess3D(
            size_list=size_list,
            label_list=label_list,
            grid=grid,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
            TransitionMatrix=TransitionMatrix,
        )

        comparison = mp.TransitionMatrix == TransitionMatrix
        assert comparison.all()

        # run the simulation:
        random.seed(0)
        mp.simulate(generations=1)
        assert mp.curr_size_list == [0, 27]
