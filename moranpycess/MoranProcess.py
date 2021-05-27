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
import matplotlib.pyplot as plt
import Individual
import exceptions


class MoranProcess:
    """General Moran Process with multiple types of individuals."""

    def __init__(
        self,
        size_list,
        label_list,
        BirthPayoffMatrix,
        DeathPayoffMatrix,
        TransitionMatrix=None,
    ):
        """Class initializer.

        Args:
            size_list (list of int): cardinalities of subpopulations.
            label_list (list of str): distinct labels of subpopulations.
            BirthPayoffMatrix (np.array): payoff matrix for the birth process.
            DeathPayoffMatrix (np.array): payoff matrix for the death process.
            TransitionMatrix (np.array, optional): transition probabilities
                between types. Defaults to None.

        Attributes:
            population (list of class:Individual): entire population.
            init_size_list (list of int): cardinalities of initial
            subpopulations.
            curr_size_list (list of int): cardinalities of current
            subpopulations.
            init_label_list (list of str): distinct labels of initial
            subpopulations.
            BirthPayoffMatrix (np.array): payoff matrix for the birth process.
            DeathPayoffMatrix (np.array): payoff matrix for the death process.
            w (float): selection pressure weight for the fitness calculation.
            AvgBirthPayoffDict (dict of str:float): current average birth
            payoffs for distinct subpopulations.
            AvgDeathPayoffDict (dict of str:float): current average death
            payoffs for distinct subpopulations.
            BirthFitnessDict (dict of str:float): current birth fitnesses
            for distinct subpopulations.
            DeathFitnessDict (dict of str:float): current death fitnesses
            for distinct subpopulations.
            Entropy (float): current entropy of the whole population.
            TransitionMatrix (np.array, optional): transition probabilities
            between types. Defaults to None.

        Raises:
            AssertionError: on invalid arguments.
            IncorrectValueError: on wrong values in the Transition Matrix.

        """

        # check if the argument lists length match
        try:
            assert len(size_list) == len(label_list)
        except AssertionError as e:
            e.args += ("Mismatch length of size and label lists",)
            raise

        # initialize a list of Individuals
        ID_counter = 0
        self.population = []
        for label_index, label in enumerate(label_list):
            for i in range(size_list[label_index]):
                self.population.append(
                    Individual.Individual(ID=ID_counter, label=label_list[label_index])
                )
                ID_counter += 1

        # keep record of the argument lists
        self.init_size_list = copy.deepcopy(size_list)
        self.curr_size_list = copy.deepcopy(size_list)
        self.init_label_list = copy.deepcopy(label_list)

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
        self.BirthPayoffMatrix = BirthPayoffMatrix.copy()
        self.DeathPayoffMatrix = DeathPayoffMatrix.copy()

        # introduce a payoff weight for the fitness calculation
        self.w = 0.5

        # calculate avg payoffs
        self.AvgBirthPayoffDict = {}
        self._UpdateAvgBirthPayoffForAll()
        self.AvgDeathPayoffDict = {}
        self._UpdateAvgDeathPayoffForAll()

        # calculate fitnesses
        self.BirthFitnessDict = {}
        self._UpdateBirthFitnessForAll()
        self.DeathFitnessDict = {}
        self._UpdateDeathFitnessForAll()

        # calculate entropy of the types distribution
        self.Entropy = 0
        self._UpdateEntropy()

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
            except AssertionError as e:
                e.args += ("Invalid Transition Matrix",)
                raise
            # check if the values are correct
            for v in np.sum(TransitionMatrix, axis=1):
                if v != 1.0:
                    raise exceptions.IncorrectValueError(
                        parameter="Transition Matrix",
                        message="Transition probabilities need to add up to 1.0.",
                    )
        self.TransitionMatrix = copy.deepcopy(TransitionMatrix)

    @property
    def population(self):
        """Python getter: population."""
        return self._population

    @population.setter
    def population(self, population):
        """Python setter: population."""
        self._population = population

    @property
    def init_size_list(self):
        """Python getter: init_size_list."""
        return self._init_size_list

    @init_size_list.setter
    def init_size_list(self, init_size_list):
        """Python setter: init_size_list."""
        self._init_size_list = init_size_list

    @property
    def curr_size_list(self):
        """Python getter: curr_size_list."""
        return self._curr_size_list

    @curr_size_list.setter
    def curr_size_list(self, curr_size_list):
        """Python setter: curr_size_list."""
        self._curr_size_list = curr_size_list

    @property
    def init_label_list(self):
        """Python getter: init_label_list."""
        return self._init_label_list

    @init_label_list.setter
    def init_label_list(self, init_label_list):
        """Python setter: init_label_list."""
        self._init_label_list = init_label_list

    @property
    def BirthPayoffMatrix(self):
        """Python getter: BirthPayoffMatrix."""
        return self._BirthPayoffMatrix

    @BirthPayoffMatrix.setter
    def BirthPayoffMatrix(self, BirthPayoffMatrix):
        """Python setter: BirthPayoffMatrix."""
        self._BirthPayoffMatrix = BirthPayoffMatrix

    @property
    def DeathPayoffMatrix(self):
        """Python getter: DeathPayoffMatrix."""
        return self._DeathPayoffMatrix

    @DeathPayoffMatrix.setter
    def DeathPayoffMatrix(self, DeathPayoffMatrix):
        """Python setter: DeathPayoffMatrix."""
        self._DeathPayoffMatrix = DeathPayoffMatrix

    @property
    def w(self):
        """Python getter: w."""
        return self._w

    @w.setter
    def w(self, w):
        """Python setter: w."""
        self._w = w

    @property
    def AvgBirthPayoffDict(self):
        """Python getter: AvgBirthPayoffDict."""
        return self._AvgBirthPayoffDict

    @AvgBirthPayoffDict.setter
    def AvgBirthPayoffDict(self, AvgBirthPayoffDict):
        """Python setter: AvgBirthPayoffDict."""
        self._AvgBirthPayoffDict = AvgBirthPayoffDict

    @property
    def AvgDeathPayoffDict(self):
        """Python getter: AvgDeathPayoffDict."""
        return self._AvgDeathPayoffDict

    @AvgDeathPayoffDict.setter
    def AvgDeathPayoffDict(self, AvgDeathPayoffDict):
        """Python setter: AvgDeathPayoffDict."""
        self._AvgDeathPayoffDict = AvgDeathPayoffDict

    @property
    def BirthFitnessDict(self):
        """Python getter: BirthFitnessDict."""
        return self._BirthFitnessDict

    @BirthFitnessDict.setter
    def BirthFitnessDict(self, BirthFitnessDict):
        """Python setter: BirthFitnessDict."""
        self._BirthFitnessDict = BirthFitnessDict

    @property
    def DeathFitnessDict(self):
        """Python getter: DeathFitnessDict."""
        return self._DeathFitnessDict

    @DeathFitnessDict.setter
    def DeathFitnessDict(self, DeathFitnessDict):
        """Python setter: DeathFitnessDict."""
        self._DeathFitnessDict = DeathFitnessDict

    @property
    def Entropy(self):
        """Python getter: Entropy."""
        return self._Entropy

    @Entropy.setter
    def Entropy(self, Entropy):
        """Python setter: Entropy."""
        self._Entropy = Entropy

    @property
    def TransitionMatrix(self):
        """Python getter: TransitionMatrix."""
        return self._TransitionMatrix

    @TransitionMatrix.setter
    def TransitionMatrix(self, TransitionMatrix):
        """Python setter: TransitionMatrix."""
        self._TransitionMatrix = TransitionMatrix

    def _UpdateAvgBirthPayoffForAll(self):
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

    def _UpdateAvgDeathPayoffForAll(self):
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

    def _UpdateBirthFitnessForAll(self):
        """Calculate Birth Fitness in the whole population."""
        # calculate fitness for distinct Individual types:
        for label in self.init_label_list:
            self.BirthFitnessDict[label] = (
                1 - self.w + self.w * self.AvgBirthPayoffDict[label]
            )
        # update attributes of all Individuals:
        for ind in self.population:
            ind.BirthFitness = self.BirthFitnessDict[ind.label]

    def _UpdateDeathFitnessForAll(self):
        """Calculate Death Fitness in the whole population."""
        # calculate fitness for distinct Individual types:
        for label in self.init_label_list:
            self.DeathFitnessDict[label] = (
                1 - self.w + self.w * self.AvgDeathPayoffDict[label]
            )
        # update attributes of all Individuals:
        for ind in self.population:
            ind.DeathFitness = self.DeathFitnessDict[ind.label]

    def _roulette_wheel_selection_Birth(self):
        """Select one individual according to the Birth Fitness.

        Returns:
            Individual: an individual selected from the population.

        """
        return self.__roulette_wheel_selection(attr="BirthFitness")

    def _roulette_wheel_selection_Death(self):
        """Select one individual according to the Death Fitness.

        Returns:
            Individual: an individual selected from the population.

        """
        return self.__roulette_wheel_selection(attr="DeathFitness")

    def __roulette_wheel_selection(self, attr):
        """A simple implementation of fitness proportional selection.

        Returns:
            Individual: an individual selected from the population.

        """
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
        """Simulate population evolution.

        Simulate population evolution: Birth-Death process with fitness-based
        selection of individuals.

        Args:
            generations (int): number of time steps.

        Returns:
            pd.DataFrame: table with simulation logs.

        """

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
            selectedBirth = self._roulette_wheel_selection_Birth()
            # create a copy
            new_individual = copy.deepcopy(selectedBirth)
            # select one individual to die
            selectedDeath = self._roulette_wheel_selection_Death()
            # add the new individual to the population
            self.population.append(new_individual)
            # remove the selected individual from the population
            self.population.remove(selectedDeath)
            # update the list with population info
            self.curr_size_list[self.init_label_list.index(selectedBirth.label)] += 1
            self.curr_size_list[self.init_label_list.index(selectedDeath.label)] -= 1

            # perform transitions (if TransitionMatrix was specified)
            if self.TransitionMatrix is not None:
                for ind in self.population:
                    row_index = self.init_label_list.index(ind.label)
                    new_label = np.random.choice(
                        a=self.init_label_list,
                        size=1,
                        p=self.TransitionMatrix[row_index,],
                    )[0]
                    old_label = ind.label
                    ind.label = new_label
                    # update the list with population info
                    self.curr_size_list[self.init_label_list.index(new_label)] += 1
                    self.curr_size_list[self.init_label_list.index(old_label)] -= 1

            # after each birth-death cycle:
            # re-evaluate the payoffs and fitnesses of all Individuals in the population
            self._UpdateAvgBirthPayoffForAll()
            self._UpdateAvgDeathPayoffForAll()
            self._UpdateBirthFitnessForAll()
            self._UpdateDeathFitnessForAll()
            # re-evaluate the population Entropy
            self._UpdateEntropy()

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

    def _UpdateEntropy(self):
        """Calculate entropy of Individual types in the population."""
        self.Entropy = 0
        for type_size in self.curr_size_list:
            fraction = float(type_size) / len(self.population)
            if fraction != 0.0:
                self.Entropy -= fraction * np.log2(fraction)

    def PlotSize(self, df, path):
        """Plot the sub-populations' sizes after a simulation.

        Args:
            df (pd.DataFrame): table with simulation logs.
            path (str): path for the plot.

        """
        plt.figure(figsize=(14, 6))
        ax = plt.gca()
        ax.tick_params(width=1)
        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(1)
        cmap = plt.get_cmap("coolwarm")
        columns = [l + "__size" for l in self.init_label_list]
        df_copy = df[columns].copy()
        df_copy.columns = self.init_label_list
        df_copy.plot(linewidth=1.5, ax=ax, cmap=cmap)
        population_size = len(self.population)
        ax.set_ylim([0, population_size])
        plt.xlabel("Generation", size=14)
        plt.ylabel("# Individuals", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)

    def PlotAvgBirthPayoff(self, df, path):
        """Plot the sub-populations' AvgBirthPayoff after a simulation.

        Args:
            df (pd.DataFrame): table with simulation logs.
            path (str): path for the plot.

        """
        plt.figure(figsize=(14, 6))
        ax = plt.gca()
        ax.tick_params(width=1)
        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(1)
        cmap = plt.get_cmap("coolwarm")
        columns = [l + "__AvgBirthPayoff" for l in self.init_label_list]
        df_copy = df[columns].copy()
        df_copy.columns = self.init_label_list
        df_copy.plot(linewidth=1.5, ax=ax, cmap=cmap)
        plt.xlabel("Generation", size=14)
        plt.ylabel("Average Birth Payoff", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)

    def PlotAvgDeathPayoff(self, df, path):
        """Plot the sub-populations' AvgDeathPayoff after a simulation.

        Args:
            df (pd.DataFrame): table with simulation logs.
            path (str): path for the plot.

        """
        plt.figure(figsize=(14, 6))
        ax = plt.gca()
        ax.tick_params(width=1)
        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(1)
        cmap = plt.get_cmap("coolwarm")
        columns = [l + "__AvgDeathPayoff" for l in self.init_label_list]
        df_copy = df[columns].copy()
        df_copy.columns = self.init_label_list
        df_copy.plot(linewidth=1.5, ax=ax, cmap=cmap)
        plt.xlabel("Generation", size=14)
        plt.ylabel("Average Death Payoff", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)

    def PlotBirthFitness(self, df, path):
        """Plot the sub-populations' BirthFitness after a simulation.

        Args:
            df (pd.DataFrame): table with simulation logs.
            path (str): path for the plot.

        """
        plt.figure(figsize=(14, 6))
        ax = plt.gca()
        ax.tick_params(width=1)
        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(1)
        cmap = plt.get_cmap("coolwarm")
        columns = [l + "__BirthFitness" for l in self.init_label_list]
        df_copy = df[columns].copy()
        df_copy.columns = self.init_label_list
        df_copy.plot(linewidth=1.5, ax=ax, cmap=cmap)
        plt.xlabel("Generation", size=14)
        plt.ylabel("Birth Fitness", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)

    def PlotDeathFitness(self, df, path):
        """Plot the sub-populations' DeathFitness after a simulation.

        Args:
            df (pd.DataFrame): table with simulation logs.
            path (str): path for the plot.

        """
        plt.figure(figsize=(14, 6))
        ax = plt.gca()
        ax.tick_params(width=1)
        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(1)
        cmap = plt.get_cmap("coolwarm")
        columns = [l + "__DeathFitness" for l in self.init_label_list]
        df_copy = df[columns].copy()
        df_copy.columns = self.init_label_list
        df_copy.plot(linewidth=1.5, ax=ax, cmap=cmap)
        plt.xlabel("Generation", size=14)
        plt.ylabel("Death Fitness", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)

    def PlotEntropy(self, df, path):
        """Plot the whole populations entropy after a simulation.

        Args:
            df (pd.DataFrame): table with simulation logs.
            path (str): path for the plot.

        """
        plt.figure(figsize=(14, 6))
        ax = plt.gca()
        ax.tick_params(width=1)
        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(1)
        df["Entropy"].plot(color="black", linewidth=1.5, ax=ax, label="Entropy")
        plt.xlabel("Generation", size=14)
        plt.ylabel("", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)
