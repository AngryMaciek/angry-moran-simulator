"""
##############################################################################
#
#   Implementation of the 3D population evolution
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
import random
import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Individual import Individual
from CustomExceptions import IncorrectValueError


class MoranProcess3D:
    """3D Moran Process with multiple types of individuals."""

    def __init__(
        self,
        size_list,
        label_list,
        grid,
        BirthPayoffMatrix,
        DeathPayoffMatrix,
        TransitionMatrix=None,
    ):
        """Class initializer.

        Args:
            size_list (list of int): cardinalities of subpopulations.
            label_list (list of str): distinct labels of subpopulations.
            grid (np.array): subpopulations' position in 3D.
            BirthPayoffMatrix (np.array): payoff matrix for the birth process.
            DeathPayoffMatrix (np.array): payoff matrix for the death process.
            TransitionMatrix (np.array, optional): transition probabilities
                between types. Defaults to None.

        Attributes:
            population (list of Individual): entire population.
            init_size_list (list of int): cardinalities of initial
                subpopulations.
            curr_size_list (list of int): cardinalities of current
                subpopulations.
            init_label_list (list of str): distinct labels of initial
                subpopulations.
            BirthPayoffMatrix (np.array): payoff matrix for the birth process.
            DeathPayoffMatrix (np.array): payoff matrix for the death process.
            w (float): selection pressure weight for the fitness calculation.
            Entropy (float): current entropy of the whole population.
            TransitionMatrix (np.array, optional): transition probabilities
                between types. Defaults to None.
            init_grid (np.array): subpopulations' initial position in 3D.
            curr_grid (np.array): subpopulations' initial position in 3D.

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

        # keep record of the argument lists
        self.init_size_list = copy.deepcopy(size_list)
        self.curr_size_list = copy.deepcopy(size_list)
        self.init_label_list = copy.deepcopy(label_list)
        self.init_grid = copy.deepcopy(grid)
        self.curr_grid = copy.deepcopy(grid)

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

        # check if the grid argument is correct
        try:
            unique, counts = np.unique(grid, return_counts=True)
            grid_dict = dict(zip(unique, counts))
            for l in unique:
                assert l in self.init_label_list
            for i in range(len(unique)):
                assert self.init_size_list[i] == grid_dict[self.init_label_list[i]]
        except AssertionError as e:
            e.args += ("Invalid Population Grid",)
            raise

        # initialize a 3D array of Individuals
        ID_counter = 0
        self.population = np.empty(
            (self.init_grid.shape[0], self.init_grid.shape[1], self.init_grid.shape[2]),
            dtype=Individual,
        )
        for x in range(self.init_grid.shape[0]):
            for y in range(self.init_grid.shape[1]):
                for z in range(self.init_grid.shape[2]):
                    self.population[x, y, z] = Individual(
                        ID=ID_counter, label=self.init_grid[x, y, z]
                    )
                    ID_counter += 1

        # iterate over the whole 3D population and update payoffs
        for x in range(self.population.shape[0]):
            for y in range(self.population.shape[1]):
                for z in range(self.init_grid.shape[2]):
                    self._UpdateBirthPayoff(x, y, z)
                    self._UpdateDeathPayoff(x, y, z)
                    self._UpdateBirthFitness(x, y, z)
                    self._UpdateDeathFitness(x, y, z)

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
                    raise IncorrectValueError(
                        parameter="Transition Matrix",
                        message="Transition probabilities need to add up to 1.0.",
                    )
        self.TransitionMatrix = copy.deepcopy(TransitionMatrix)

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
    def init_grid(self):
        """Python getter."""
        return self._init_grid

    @init_grid.setter
    def init_grid(self, init_grid):
        """Python setter."""
        self._init_grid = init_grid

    @property
    def curr_grid(self):
        """Python getter."""
        return self._curr_grid

    @curr_grid.setter
    def curr_grid(self, curr_grid):
        """Python setter."""
        self._curr_grid = curr_grid

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
    def Entropy(self):
        """Python getter."""
        return self._Entropy

    @Entropy.setter
    def Entropy(self, Entropy):
        """Python setter."""
        self._Entropy = Entropy

    @property
    def TransitionMatrix(self):
        """Python getter."""
        return self._TransitionMatrix

    @TransitionMatrix.setter
    def TransitionMatrix(self, TransitionMatrix):
        """Python setter."""
        self._TransitionMatrix = TransitionMatrix

    def _UpdateBirthPayoff(self, x, y, z):
        """Calculate Birth Payoff for a given Individual.

        Args:
            x (int): x-coordinate of the Individual.
            y (int): y-coordinate of the Individual.
            z (int): z-coordinate of the Individual.

        """

        this_label = self.population[x, y, z].label
        this_label_index = self._init_label_list.index(this_label)

        pop_x = self.population.shape[0]
        pop_y = self.population.shape[1]
        pop_z = self.population.shape[2]

        # Select direct neighbours in the grid with periodical boundary conditions:
        neighbours_labels = [
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, z % pop_z].label,
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].label,
            self.population[(x - 1) % pop_x, y % pop_y, (z - 1) % pop_z].label,
            self.population[(x - 1) % pop_x, y % pop_y, z % pop_z].label,
            self.population[(x - 1) % pop_x, y % pop_y, (z + 1) % pop_z].label,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, z % pop_z].label,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].label,
            self.population[x % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].label,
            self.population[x % pop_x, (y - 1) % pop_y, z % pop_z].label,
            self.population[x % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].label,
            self.population[x % pop_x, y % pop_y, (z - 1) % pop_z].label,
            self.population[x % pop_x, y % pop_y, (z + 1) % pop_z].label,
            self.population[x % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].label,
            self.population[x % pop_x, (y + 1) % pop_y, z % pop_z].label,
            self.population[x % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, z % pop_z].label,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].label,
            self.population[(x + 1) % pop_x, y % pop_y, (z - 1) % pop_z].label,
            self.population[(x + 1) % pop_x, y % pop_y, z % pop_z].label,
            self.population[(x + 1) % pop_x, y % pop_y, (z + 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, z % pop_z].label,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].label,
        ]

        payoff = 0
        for neighbour_label in set(neighbours_labels):
            c = self._init_label_list.index(neighbour_label)
            payoff += (
                neighbours_labels.count(neighbour_label)
                * self.BirthPayoffMatrix[this_label_index, c]
            )
        payoff = payoff / 26.0
        self.population[x, y, z].AvgBirthPayoff = payoff

    def _UpdateDeathPayoff(self, x, y, z):
        """Calculate Death Payoff for a given Individual.

        Args:
            x (int): x-coordinate of the Individual.
            y (int): y-coordinate of the Individual.
            z (int): z-coordinate of the Individual.

        """

        this_label = self.population[x, y, z].label
        this_label_index = self._init_label_list.index(this_label)

        pop_x = self.population.shape[0]
        pop_y = self.population.shape[1]
        pop_z = self.population.shape[2]

        # Select direct neighbours in the grid with periodical boundary conditions:
        neighbours_labels = [
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, z % pop_z].label,
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].label,
            self.population[(x - 1) % pop_x, y % pop_y, (z - 1) % pop_z].label,
            self.population[(x - 1) % pop_x, y % pop_y, z % pop_z].label,
            self.population[(x - 1) % pop_x, y % pop_y, (z + 1) % pop_z].label,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, z % pop_z].label,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].label,
            self.population[x % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].label,
            self.population[x % pop_x, (y - 1) % pop_y, z % pop_z].label,
            self.population[x % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].label,
            self.population[x % pop_x, y % pop_y, (z - 1) % pop_z].label,
            self.population[x % pop_x, y % pop_y, (z + 1) % pop_z].label,
            self.population[x % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].label,
            self.population[x % pop_x, (y + 1) % pop_y, z % pop_z].label,
            self.population[x % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, z % pop_z].label,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].label,
            self.population[(x + 1) % pop_x, y % pop_y, (z - 1) % pop_z].label,
            self.population[(x + 1) % pop_x, y % pop_y, z % pop_z].label,
            self.population[(x + 1) % pop_x, y % pop_y, (z + 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].label,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, z % pop_z].label,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].label,
        ]

        payoff = 0
        for neighbour_label in set(neighbours_labels):
            c = self._init_label_list.index(neighbour_label)
            payoff += (
                neighbours_labels.count(neighbour_label)
                * self.DeathPayoffMatrix[this_label_index, c]
            )
        payoff = payoff / 26.0
        self.population[x, y, z].AvgDeathPayoff = payoff

    def _UpdateBirthFitness(self, x, y, z):
        """Calculate Birth Fitness for a given Individual.

        Args:
            x (int): x-coordinate of the Individual.
            y (int): y-coordinate of the Individual.
            z (int): z-coordinate of the Individual.

        """
        self.population[x, y, z].BirthFitness = (
            1 - self.w + self.w * self.population[x, y, z].AvgBirthPayoff
        )

    def _UpdateDeathFitness(self, x, y, z):
        """Calculate Death Fitness for a given Individual.

        Args:
            x (int): x-coordinate of the Individual.
            y (int): y-coordinate of the Individual.
            z (int): z-coordinate of the Individual.

        """
        self.population[x, y, z].DeathFitness = (
            1 - self.w + self.w * self.population[x, y, z].AvgDeathPayoff
        )

    def _UpdateEntropy(self):
        """Calculate entropy of Individual types in the population."""
        self.Entropy = 0
        for type_size in self.curr_size_list:
            fraction = float(type_size) / self.population.size
            if fraction != 0.0:
                self.Entropy -= fraction * np.log2(fraction)

    def _roulette_wheel_selection_Birth(self):
        """Select one individual according to the Birth Fitness.

        Returns:
            tuple: (x, y, z) - coordinates of the selected Individual.

        """
        max_value = 0
        for x in range(self.init_grid.shape[0]):
            for y in range(self.init_grid.shape[1]):
                for z in range(self.init_grid.shape[2]):
                    max_value += self.population[x, y, z].BirthFitness
        pick = random.uniform(0, max_value)
        current = 0
        for x in range(self.init_grid.shape[0]):
            for y in range(self.init_grid.shape[1]):
                for z in range(self.init_grid.shape[2]):
                    current += self.population[x, y, z].BirthFitness
                    if current > pick:
                        return (x, y, z)

    def _roulette_wheel_selection_Death(self, x, y, z):
        """Select one individual according to the Death Fitness.

        Note:
            Select from direct neighbours of the Individual in argument.

        Args:
            x (int): x-coordinate of an Individual.
            y (int): y-coordinate of an Individual.
            z (int): z-coordinate of an Individual.

        Returns:
            tuple: (X, Y, Z) - coordinates of the selected Individual.

        """
        pop_x = self.population.shape[0]
        pop_y = self.population.shape[1]
        pop_z = self.population.shape[2]
        neighbours_scores = [
            self.population[
                (x - 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z
            ].DeathFitness,
            self.population[(x - 1) % pop_x, (y - 1) % pop_y, z % pop_z].DeathFitness,
            self.population[
                (x - 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z
            ].DeathFitness,
            self.population[(x - 1) % pop_x, y % pop_y, (z - 1) % pop_z].DeathFitness,
            self.population[(x - 1) % pop_x, y % pop_y, z % pop_z].DeathFitness,
            self.population[(x - 1) % pop_x, y % pop_y, (z + 1) % pop_z].DeathFitness,
            self.population[
                (x - 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z
            ].DeathFitness,
            self.population[(x - 1) % pop_x, (y + 1) % pop_y, z % pop_z].DeathFitness,
            self.population[
                (x - 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z
            ].DeathFitness,
            self.population[x % pop_x, (y - 1) % pop_y, (z - 1) % pop_z].DeathFitness,
            self.population[x % pop_x, (y - 1) % pop_y, z % pop_z].DeathFitness,
            self.population[x % pop_x, (y - 1) % pop_y, (z + 1) % pop_z].DeathFitness,
            self.population[x % pop_x, y % pop_y, (z - 1) % pop_z].DeathFitness,
            self.population[x % pop_x, y % pop_y, (z + 1) % pop_z].DeathFitness,
            self.population[x % pop_x, (y + 1) % pop_y, (z - 1) % pop_z].DeathFitness,
            self.population[x % pop_x, (y + 1) % pop_y, z % pop_z].DeathFitness,
            self.population[x % pop_x, (y + 1) % pop_y, (z + 1) % pop_z].DeathFitness,
            self.population[
                (x + 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z
            ].DeathFitness,
            self.population[(x + 1) % pop_x, (y - 1) % pop_y, z % pop_z].DeathFitness,
            self.population[
                (x + 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z
            ].DeathFitness,
            self.population[(x + 1) % pop_x, y % pop_y, (z - 1) % pop_z].DeathFitness,
            self.population[(x + 1) % pop_x, y % pop_y, z % pop_z].DeathFitness,
            self.population[(x + 1) % pop_x, y % pop_y, (z + 1) % pop_z].DeathFitness,
            self.population[
                (x + 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z
            ].DeathFitness,
            self.population[(x + 1) % pop_x, (y + 1) % pop_y, z % pop_z].DeathFitness,
            self.population[
                (x + 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z
            ].DeathFitness,
        ]
        max_value = sum(neighbours_scores)
        pick = random.uniform(0, max_value)
        current = 0
        indices_list = [
            ((x - 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z),
            ((x - 1) % pop_x, (y - 1) % pop_y, z % pop_z),
            ((x - 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z),
            ((x - 1) % pop_x, y % pop_y, (z - 1) % pop_z),
            ((x - 1) % pop_x, y % pop_y, z % pop_z),
            ((x - 1) % pop_x, y % pop_y, (z + 1) % pop_z),
            ((x - 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z),
            ((x - 1) % pop_x, (y + 1) % pop_y, z % pop_z),
            ((x - 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z),
            (x % pop_x, (y - 1) % pop_y, (z - 1) % pop_z),
            (x % pop_x, (y - 1) % pop_y, z % pop_z),
            (x % pop_x, (y - 1) % pop_y, (z + 1) % pop_z),
            (x % pop_x, y % pop_y, (z - 1) % pop_z),
            (x % pop_x, y % pop_y, (z + 1) % pop_z),
            (x % pop_x, (y + 1) % pop_y, (z - 1) % pop_z),
            (x % pop_x, (y + 1) % pop_y, z % pop_z),
            (x % pop_x, (y + 1) % pop_y, (z + 1) % pop_z),
            ((x + 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z),
            ((x + 1) % pop_x, (y - 1) % pop_y, z % pop_z),
            ((x + 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z),
            ((x + 1) % pop_x, y % pop_y, (z - 1) % pop_z),
            ((x + 1) % pop_x, y % pop_y, z % pop_z),
            ((x + 1) % pop_x, y % pop_y, (z + 1) % pop_z),
            ((x + 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z),
            ((x + 1) % pop_x, (y + 1) % pop_y, z % pop_z),
            ((x + 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z),
        ]
        for score, indices in zip(neighbours_scores, indices_list):
            current += score
            if current > pick:
                return indices

    def simulate(self, generations):
        """Simulate 3D population evolution.

        Simulate 3D population evolution: Birth-Death process with
        fitness-based selection of individuals.

        Args:
            generations (int): number of time steps.

        Returns:
            pd.DataFrame: table with simulation logs.

        """
        pop_x = self.population.shape[0]
        pop_y = self.population.shape[1]
        pop_z = self.population.shape[2]

        # prepare a dataframe to store the logs
        colnames = [l + "__size" for l in self.init_label_list] + ["Entropy"]
        log_df = pd.DataFrame(index=range(generations + 1), columns=colnames)
        log_df.index.name = "generation"

        # update the dataframe with features of the initial population
        for l in range(len(self.init_label_list)):
            label = self.init_label_list[l]
            log_df.at[0, label + "__size"] = self.init_size_list[l]
            log_df.at[0, "Entropy"] = self.Entropy

        for g in range(generations):

            # select one individual to multiply
            (x, y, z) = self._roulette_wheel_selection_Birth()
            selectedBirth = self.population[x, y, z]
            # create a copy
            new_individual = copy.deepcopy(selectedBirth)
            # select one individual to die
            (x, y, z) = self._roulette_wheel_selection_Death(x, y, z)
            selectedDeath = copy.deepcopy(self.population[x, y, z])
            # swap the individuals
            self.population[x, y, z] = new_individual
            # update the list with population info
            self.curr_size_list[self.init_label_list.index(selectedBirth.label)] += 1
            self.curr_size_list[self.init_label_list.index(selectedDeath.label)] -= 1

            # perform transitions (if TransitionMatrix was specified)
            if self.TransitionMatrix is not None:
                for x_ in range(pop_x):
                    for y_ in range(pop_y):
                        for z_ in range(pop_z):
                            ind = self.population[x_, y_, z_]
                            row_index = self.init_label_list.index(ind.label)
                            new_label = np.random.choice(
                                a=self.init_label_list,
                                size=1,
                                p=self.TransitionMatrix[row_index,],
                            )[0]
                            old_label = ind.label
                            ind.label = new_label
                            # update the list with population info
                            self.curr_size_list[
                                self.init_label_list.index(new_label)
                            ] += 1
                            self.curr_size_list[
                                self.init_label_list.index(old_label)
                            ] -= 1

            # after each birth-death cycle:

            # update scores for all individuals (if TransitionMatrix was specified)
            if self.TransitionMatrix is not None:
                for x_ in range(self.population.shape[0]):
                    for y_ in range(self.population.shape[1]):
                        for z_ in range(self.init_grid.shape[2]):
                            self._UpdateBirthPayoff(x_, y_, z_)
                            self._UpdateDeathPayoff(x_, y_, z_)
                            self._UpdateBirthFitness(x_, y_, z_)
                            self._UpdateDeathFitness(x_, y_, z_)
            # in other case:
            # re-evaluate the payoffs and fitnesses of only
            # the affected neigbours Individuals in the population
            else:
                # re-evaluate the payoffs and fitnesses of the affected Individuals in the population
                indices_list = [
                    ((x - 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z),
                    ((x - 1) % pop_x, (y - 1) % pop_y, z % pop_z),
                    ((x - 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z),
                    ((x - 1) % pop_x, y % pop_y, (z - 1) % pop_z),
                    ((x - 1) % pop_x, y % pop_y, z % pop_z),
                    ((x - 1) % pop_x, y % pop_y, (z + 1) % pop_z),
                    ((x - 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z),
                    ((x - 1) % pop_x, (y + 1) % pop_y, z % pop_z),
                    ((x - 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z),
                    (x % pop_x, (y - 1) % pop_y, (z - 1) % pop_z),
                    (x % pop_x, (y - 1) % pop_y, z % pop_z),
                    (x % pop_x, (y - 1) % pop_y, (z + 1) % pop_z),
                    (x % pop_x, y % pop_y, (z - 1) % pop_z),
                    (x % pop_x, y % pop_y, z % pop_z),
                    (x % pop_x, y % pop_y, (z + 1) % pop_z),
                    (x % pop_x, (y + 1) % pop_y, (z - 1) % pop_z),
                    (x % pop_x, (y + 1) % pop_y, z % pop_z),
                    (x % pop_x, (y + 1) % pop_y, (z + 1) % pop_z),
                    ((x + 1) % pop_x, (y - 1) % pop_y, (z - 1) % pop_z),
                    ((x + 1) % pop_x, (y - 1) % pop_y, z % pop_z),
                    ((x + 1) % pop_x, (y - 1) % pop_y, (z + 1) % pop_z),
                    ((x + 1) % pop_x, y % pop_y, (z - 1) % pop_z),
                    ((x + 1) % pop_x, y % pop_y, z % pop_z),
                    ((x + 1) % pop_x, y % pop_y, (z + 1) % pop_z),
                    ((x + 1) % pop_x, (y + 1) % pop_y, (z - 1) % pop_z),
                    ((x + 1) % pop_x, (y + 1) % pop_y, z % pop_z),
                    ((x + 1) % pop_x, (y + 1) % pop_y, (z + 1) % pop_z),
                ]
                for indices in indices_list:
                    self._UpdateBirthPayoff(indices[0], indices[1], indices[2])
                    self._UpdateDeathPayoff(indices[0], indices[1], indices[2])
                    self._UpdateBirthFitness(indices[0], indices[1], indices[2])
                    self._UpdateDeathFitness(indices[0], indices[1], indices[2])

            # update the grid
            for x_ in range(self.curr_grid.shape[0]):
                for y_ in range(self.curr_grid.shape[1]):
                    for z_ in range(self.curr_grid.shape[2]):
                        self.curr_grid[x_, y_, z_] = self.population[x_, y_, z_].label

            # re-evaluate the population Entropy
            self._UpdateEntropy()

            # update the log dataframe
            for l in range(len(self.init_label_list)):
                label = self.init_label_list[l]
                log_df.at[g + 1, label + "__size"] = self.curr_size_list[l]
                log_df.at[g + 1, "Entropy"] = self.Entropy

        return log_df

    def PlotSize3D(self, df, path):
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
        population_size = self.population.size
        ax.set_ylim([0, population_size])
        plt.xlabel("Generation", size=14)
        plt.ylabel("# Individuals", size=14)
        ax.tick_params(axis="both", which="major", labelsize=12)
        ax.legend(loc=4, fontsize=20)
        plt.savefig(fname=path, dpi=300)

    def PlotEntropy3D(self, df, path):
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
