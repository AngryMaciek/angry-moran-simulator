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
import matplotlib.pyplot as plt


class MoranProcess:
    """General Moran Process with multiple types of individuals."""

    def __init__(self, size_list, label_list, BirthPayoffMatrix, DeathPayoffMatrix):
        """Class initializer."""

        # check if the argument lists length match
        try:
            assert len(size_list) == len(label_list)
        except AssertionError as e:
            e.args += ("Mismatch length of size and label lists",)
            raise

        # initialize a list of Individuals
        ID_counter = 0
        self.population = []
        for label_index in range(len(label_list)):
            for i in range(size_list[label_index]):
                self.population.append(
                    ms.Individual(ID=ID_counter, ind_label=label_list[label_index])
                )
                ID_counter += 1

        # keep record of the argument lists
        self.init_size_list = size_list
        self.curr_size_list = size_list
        self.init_label_list = label_list

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

        # calculate avg payoffs
        self.AvgBirthPayoffDict = {}
        self.UpdateAvgBirthPayoffForAll()
        self.AvgDeathPayoffDict = {}
        self.UpdateAvgDeathPayoffForAll()

        # calculate fitnesses
        self.BirthFitnessDict = {}
        self.UpdateBirthFitnessForAll()
        self.DeathFitnessDict = {}
        self.UpdateDeathFitnessForAll()

        # calculate entropy of the types distribution
        self.Entropy = 0
        self.UpdateEntropy()

    @property
    def population(self):
        """Python getter."""
        return self._population

    @population.setter
    def population(self, population):
        """Python setter."""
        self._population = population

    @property
    def init_size_list(self):
        """Python getter."""
        return self._init_size_list

    @init_size_list.setter
    def init_size_list(self, init_size_list):
        """Python setter."""
        self._init_size_list = init_size_list

    @property
    def curr_size_list(self):
        """Python getter."""
        return self._curr_size_list

    @curr_size_list.setter
    def curr_size_list(self, curr_size_list):
        """Python setter."""
        self._curr_size_list = curr_size_list

    @property
    def init_label_list(self):
        """Python getter."""
        return self._init_label_list

    @init_label_list.setter
    def init_label_list(self, init_label_list):
        """Python setter."""
        self._init_label_list = init_label_list

    @property
    def BirthPayoffMatrix(self):
        """Python getter."""
        return self._BirthPayoffMatrix

    @BirthPayoffMatrix.setter
    def BirthPayoffMatrix(self, BirthPayoffMatrix):
        """Python setter."""
        self._BirthPayoffMatrix = BirthPayoffMatrix

    @property
    def DeathPayoffMatrix(self):
        """Python getter."""
        return self._DeathPayoffMatrix

    @DeathPayoffMatrix.setter
    def DeathPayoffMatrix(self, DeathPayoffMatrix):
        """Python setter."""
        self._DeathPayoffMatrix = DeathPayoffMatrix

    @property
    def w(self):
        """Python getter."""
        return self._w

    @w.setter
    def w(self, w):
        """Python setter."""
        self._w = w

    @property
    def AvgBirthPayoffDict(self):
        """Python getter."""
        return self._AvgBirthPayoffDict

    @AvgBirthPayoffDict.setter
    def AvgBirthPayoffDict(self, AvgBirthPayoffDict):
        """Python setter."""
        self._AvgBirthPayoffDict = AvgBirthPayoffDict

    @property
    def AvgDeathPayoffDict(self):
        """Python getter."""
        return self._AvgDeathPayoffDict

    @AvgDeathPayoffDict.setter
    def AvgDeathPayoffDict(self, AvgDeathPayoffDict):
        """Python setter."""
        self._AvgDeathPayoffDict = AvgDeathPayoffDict

    @property
    def BirthFitnessDict(self):
        """Python getter."""
        return self._BirthFitnessDict

    @BirthFitnessDict.setter
    def BirthFitnessDict(self, BirthFitnessDict):
        """Python setter."""
        self._BirthFitnessDict = BirthFitnessDict

    @property
    def DeathFitnessDict(self):
        """Python getter."""
        return self._DeathFitnessDict

    @DeathFitnessDict.setter
    def DeathFitnessDict(self, DeathFitnessDict):
        """Python setter."""
        self._DeathFitnessDict = DeathFitnessDict

    @property
    def Entropy(self):
        """Python getter."""
        return self._Entropy

    @Entropy.setter
    def Entropy(self, Entropy):
        """Python setter."""
        self._Entropy = Entropy

    def UpdateAvgBirthPayoffForAll(self):
        """Calculate avg Birth Payoffs in the whole population."""
        nrows = np.shape(self.BirthPayoffMatrix)[0]
        ncols = np.shape(self.BirthPayoffMatrix)[1]
        # calculate avg payoff for distinct Individual types:
        for r in range(nrows):
            payoff = 0
            for c in range(ncols):
                payoff += self.BirthPayoffMatrix[r, c] * (
                    self.curr_size_list[c] - int(r == c)
                )
            payoff = payoff / (sum(self.curr_size_list) - 1)
            self.AvgBirthPayoffDict[self.init_label_list[r]] = payoff
        # update attributes of all Individuals:
        for ind in self.population:
            ind.AvgBirthPayoff = self.AvgBirthPayoffDict[ind.label]

    def UpdateAvgDeathPayoffForAll(self):
        """Calculate avg Death Payoffs in the whole population."""
        nrows = np.shape(self.DeathPayoffMatrix)[0]
        ncols = np.shape(self.DeathPayoffMatrix)[1]
        # calculate avg payoff for distinct Individual types:
        for r in range(nrows):
            payoff = 0
            for c in range(ncols):
                payoff += self.DeathPayoffMatrix[r, c] * (
                    self.curr_size_list[c] - int(r == c)
                )
            payoff = payoff / (sum(self.curr_size_list) - 1)
            self.AvgDeathPayoffDict[self.init_label_list[r]] = payoff
        # update attributes of all Individuals:
        for ind in self.population:
            ind.AvgDeathPayoff = self.AvgDeathPayoffDict[ind.label]

    def UpdateBirthFitnessForAll(self):
        """Calculate Birth Fitness in the whole population."""
        # calculate fitness for distinct Individual types:
        for label in self.init_label_list:
            self.BirthFitnessDict[label] = (
                1 - self.w + self.w * self.AvgBirthPayoffDict[label]
            )
        # update attributes of all Individuals:
        for ind in self.population:
            ind.BirthFitness = self.BirthFitnessDict[ind.label]

    def UpdateDeathFitnessForAll(self):
        """Calculate Death Fitness in the whole population."""
        # calculate fitness for distinct Individual types:
        for label in self.init_label_list:
            self.DeathFitnessDict[label] = (
                1 - self.w + self.w * self.AvgDeathPayoffDict[label]
            )
        # update attributes of all Individuals:
        for ind in self.population:
            ind.DeathFitness = self.DeathFitnessDict[ind.label]

    def roulette_wheel_selection_Birth(self):
        """Select an individual according to the Birth Fitness."""
        return self.__roulette_wheel_selection(attr="BirthFitness")

    def roulette_wheel_selection_Death(self):
        """Select an individual according to the Death Fitness."""
        return self.__roulette_wheel_selection(attr="DeathFitness")

    def __roulette_wheel_selection(self, attr):
        """A simple implementation of fitness proportional selection."""
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
        """Simulate population evolution: Birth-Death process with fitness-based selection."""

        # prepare a dataframe to store the logs
        colnames = (
            [l + "__size" for l in self.init_label_list]
            + [l + "__AvgBirthPayoff" for l in self.init_label_list]
            + [l + "__AvgDeathPayoff" for l in self.init_label_list]
            + [l + "__BirthFitness" for l in self.init_label_list]
            + [l + "__DeathFitness" for l in self.init_label_list]
            + ["Entropy"]
        )
        log_df = pd.DataFrame(index=range(generations + 1), columns=colnames)
        log_df.index.name = "generation"

        # update the dataframe with features of the initial population
        for l in range(len(self.init_label_list)):
            label = self.init_label_list[l]
            log_df.at[0, label + "__size"] = self.init_size_list[l]
            log_df.at[0, label + "__AvgBirthPayoff"] = self.AvgBirthPayoffDict[label]
            log_df.at[0, label + "__AvgDeathPayoff"] = self.AvgDeathPayoffDict[label]
            log_df.at[0, label + "__BirthFitness"] = self.BirthFitnessDict[label]
            log_df.at[0, label + "__DeathFitness"] = self.DeathFitnessDict[label]
            log_df.at[0, "Entropy"] = self.Entropy

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
            # update the list with population info
            self.curr_size_list[self.init_label_list.index(selectedBirth.label)] += 1
            self.curr_size_list[self.init_label_list.index(selectedDeath.label)] -= 1
            # after each birth-death cycle:
            # re-evaluate the payoffs and fitnesses of all Individuals in the population
            self.UpdateAvgBirthPayoffForAll()
            self.UpdateAvgDeathPayoffForAll()
            self.UpdateBirthFitnessForAll()
            self.UpdateDeathFitnessForAll()
            # re-evaluate the population Entropy
            self.UpdateEntropy()

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
                log_df.at[g + 1, "Entropy"] = self.Entropy

        return log_df

    def UpdateEntropy(self):
        """Calculate entropy of Individual types for the population."""
        self.Entropy = 0
        for type_size in self.curr_size_list:
            fraction = float(type_size) / len(self.population)
            self.Entropy -= fraction * np.log2(fraction)


def PlotSize(mp, df, path):
    """Plot the sub-populations' sizes after a simulation of a given Moran Process."""
    plt.figure(figsize=(14, 6))
    ax = plt.gca()
    ax.tick_params(width=1)
    for axis in ["top", "bottom", "left", "right"]:
        ax.spines[axis].set_linewidth(1)
    for l in mp.init_label_list:
        column = l + "__size"
        df[column].plot(linewidth=1.5, ax=ax, label=l)
    population_size = len(mp.population)
    ax.set_ylim([0, population_size])
    plt.xlabel("Generation", size=14)
    plt.ylabel("# Individuals", size=14)
    ax.tick_params(axis="both", which="major", labelsize=12)
    ax.legend(loc=4, fontsize=20)
    plt.savefig(fname=path, dpi=300)
