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
import random
import numpy as np
import moran_simulator as ms


class TestClass:
    def test_classMoranProcessInit(self):
        size_list = [10, 90]
        label_list = ["A", "B"]
        BirthPayoffMatrix = np.array([[10, 20], [30, 40]])
        DeathPayoffMatrix = np.array([[1, 2], [3, 4]])
        mp = ms.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        assert mp.init_size_list == size_list
        assert mp.curr_size_list == size_list
        assert mp.init_label_list == label_list
        assert len(mp.population) == sum(size_list)
        assert mp.w == 0.5

        population_info = {j: i for i, j in zip(size_list, label_list)}
        assert mp.population_info == population_info

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
        size_list = [4, 1]
        label_list = ["abc", "def"]
        BirthPayoffMatrix = np.array([[100, 100], [1, 1]])
        DeathPayoffMatrix = np.array([[1, 1], [1, 1]])
        mp = ms.MoranProcess(
            size_list=size_list,
            label_list=label_list,
            BirthPayoffMatrix=BirthPayoffMatrix,
            DeathPayoffMatrix=DeathPayoffMatrix,
        )
        random.seed(0)
        ind = mp.roulette_wheel_selection_Birth()
        assert ind.ID == 3
        assert ind.label == "abc"



    #def roulette_wheel_selection_Death(self):
    #    return __roulette_wheel_selection(attr="DeathFitness")