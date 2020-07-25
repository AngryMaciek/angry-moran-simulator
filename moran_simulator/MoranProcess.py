"""
##############################################################################
#
#   Implementation of the population evolution
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
import copy
import numpy as np
import pandas as pd
import moran_simulator as ms


class MoranProcess:
    """
    General Moran Process with multiple types of individuals
    """

    def __init__(self, size_list, label_list, BirthPayoffMatrix, DeathPayoffMatrix):

        try:
            assert len(size_list) == len(label_list)
        except AssertionError as e:
            e.args += "Mismatch length of size and label lists"
            raise

        ID_counter = 0
        self.population = []
        for label_index in range(len(label_list)):
            for i in range(size_list[label_index]):
                self.population.append(
                    ms.Individual(ID=ID_counter, ind_label=label_list[label_index])
                )
                ID_counter += 1

        self.init_size_list = size_list
        self.curr_size_list = size_list
        self.init_label_list = label_list

        try:
            assert len(BirthPayoffMatrix.shape) == 2
            assert (
                BirthPayoffMatrix.shape[0]
                == BirthPayoffMatrix.shape[1]
                == len(label_list)
            )
        except AssertionError as e:
            e.args += "."
            raise

        try:
            assert len(DeathPayoffMatrix.shape) == 2
            assert (
                DeathPayoffMatrix.shape[0]
                == DeathPayoffMatrix.shape[1]
                == len(label_list)
            )
        except AssertionError as e:
            e.args += "."
            raise

        self.BirthPayoffMatrix = BirthPayoffMatrix
        self.DeathPayoffMatrix = DeathPayoffMatrix
        self.w = 0.5

        self.AvgBirthPayoffDict = {}
        self.UpdateAvgBirthPayoffForAll()

        self.AvgDeathPayoffDict = {}
        self.UpdateAvgDeathPayoffForAll()

        self.BirthFitnessDict = {}
        self.UpdateBirthFitnessForAll()

        self.DeathFitnessDict = {}
        self.UpdateDeathFitnessForAll()

    def UpdateAvgBirthPayoffForAll(self):
        nrows = np.shape(self.BirthPayoffMatrix)[0]
        ncols = np.shape(self.BirthPayoffMatrix)[1]
        for r in range(nrows):
            payoff = 0
            for c in range(ncols):
                payoff += self.BirthPayoffMatrix[r, c] * (
                    self.curr_size_list[c] - int(r == c)
                )
            payoff = payoff / (sum(self.curr_size_list) - 1)
            self.AvgBirthPayoffDict[self.init_label_list[r]] = payoff
        # Update attributes of individuals
        for ind in self.population:
            ind.AvgBirthPayoff = self.AvgBirthPayoffDict[ind.label]

    def UpdateAvgDeathPayoffForAll(self):
        nrows = np.shape(self.DeathPayoffMatrix)[0]
        ncols = np.shape(self.DeathPayoffMatrix)[1]
        for r in range(nrows):
            payoff = 0
            for c in range(ncols):
                payoff += self.DeathPayoffMatrix[r, c] * (
                    self.curr_size_list[c] - int(r == c)
                )
            payoff = payoff / (sum(self.curr_size_list) - 1)
            self.AvgDeathPayoffDict[self.init_label_list[r]] = payoff
        # Update attributes of individuals
        for ind in self.population:
            ind.AvgDeathPayoff = self.AvgDeathPayoffDict[ind.label]

    def UpdateBirthFitnessForAll(self):
        for label in self.init_label_list:
            self.BirthFitnessDict[label] = (
                1 - self.w + self.w * self.AvgBirthPayoffDict[label]
            )
        for ind in self.population:
            ind.BirthFitness = self.BirthFitnessDict[ind.label]

    def UpdateDeathFitnessForAll(self):
        for label in self.init_label_list:
            self.DeathFitnessDict[label] = (
                1 - self.w + self.w * self.AvgDeathPayoffDict[label]
            )
        for ind in self.population:
            ind.DeathFitness = self.DeathFitnessDict[ind.label]

    def roulette_wheel_selection_Birth(self):
        return self.__roulette_wheel_selection(attr="BirthFitness")

    def roulette_wheel_selection_Death(self):
        return self.__roulette_wheel_selection(attr="DeathFitness")

    def __roulette_wheel_selection(self, attr):
        """A simple implementation of fitness proportional selection"""
        if attr == "BirthFitness":
            max_value = sum(ind.BirthFitness for ind in self.population)
        elif attr == "DeathFitness":
            max_value = sum(ind.DeathFitness for ind in self.population)
        pick = random.uniform(0, max_value)
        current = 0
        for ind in self.population:
            if attr == "BirthFitness":
                current += ind.BirthFitness
            elif attr == "DeathFitness":
                current += ind.DeathFitness
            if current > pick:
                return ind

    def simulate(self, generations):
        # modify the self. population, return df with scores
        # one generation is a one birth-death cycle:
        # fitness-proportional cell division + fitness-proportional apoptosis

        # prepare a dataframe to store the results
        colnames = (
            [l + "__size" for l in self.init_label_list]
            + [l + "__AvgBirthPayoff" for l in self.init_label_list]
            + [l + "__AvgDeathPayoff" for l in self.init_label_list]
            + [l + "__BirthFitness" for l in self.init_label_list]
            + [l + "__DeathFitness" for l in self.init_label_list]
        )
        log_df = pd.DataFrame(index=range(generations + 1), columns=colnames)
        log_df.index.name = "generation"

        # update the dataframe with the features of the initial population
        for l in range(len(self.init_label_list)):
            label = self.init_label_list[l]
            log_df.at[0, label + "__size"] = self.init_size_list[l]
            log_df.at[0, label + "__AvgBirthPayoff"] = self.AvgBirthPayoffDict[label]
            log_df.at[0, label + "__AvgDeathPayoff"] = self.AvgDeathPayoffDict[label]
            log_df.at[0, label + "__BirthFitness"] = self.BirthFitnessDict[label]
            log_df.at[0, label + "__DeathFitness"] = self.DeathFitnessDict[label]

        for g in range(generations):
            # select one individual to multiply
            selectedBirth = self.roulette_wheel_selection_Birth()
            # create a copy
            new_individual = copy.deepcopy(selectedBirth)
            # select one individual to die
            selectedDeath = self.roulette_wheel_selection_Death()
            # add the new individual to the population
            self.population.append(new_individual)
            # remove the selected individual from the population
            self.population.remove(selectedDeath)
            # update curr size list!
            self.curr_size_list[self.init_label_list.index(selectedBirth.label)] += 1
            self.curr_size_list[self.init_label_list.index(selectedDeath.label)] -= 1
            # after each birth-death cycle we need to
            # re-evaluate the payoffs and fitnesses of all cells in the population
            self.UpdateAvgBirthPayoffForAll()
            self.UpdateAvgDeathPayoffForAll()
            self.UpdateBirthFitnessForAll()
            self.UpdateDeathFitnessForAll()

            # update the log dataframe
            for l in range(len(self.init_label_list)):
                label = self.init_label_list[l]
                log_df.at[g + 1, label + "__size"] = self.curr_size_list[l]
                log_df.at[g + 1, label + "__AvgBirthPayoff"] = self.AvgBirthPayoffDict[
                    label
                ]
                log_df.at[g + 1, label + "__AvgDeathPayoff"] = self.AvgDeathPayoffDict[
                    label
                ]
                log_df.at[g + 1, label + "__BirthFitness"] = self.BirthFitnessDict[
                    label
                ]
                log_df.at[g + 1, label + "__DeathFitness"] = self.DeathFitnessDict[
                    label
                ]

        return log_df
