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
        self.population_info = {j: i for i, j in zip(size_list, label_list)}

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
        return __roulette_wheel_selection(attr="BirthFitness")

    def roulette_wheel_selection_Death(self):
        return __roulette_wheel_selection(attr="DeathFitness")

    def __roulette_wheel_selection(self, attr):
        """A simple implementation of fitness proportional selection"""
        max_value = sum(ind.eval(attr) for ind in self.population)
        pick = random.uniform(0, max_value)
        current = 0
        for ind in self.population:
            current += ind.eval(attr)
            if current > pick:
                return ind

    def simulate(self, generations):
        pass
        # modify the self. population, return df with scores

        # copy the initial population as population 0
        # population = copy.copy(init_population)
        # current_i = 0

        # prepare a dataframe for storing statistics
        # columns=["N","i","pi_H","pi_C","f_H","f_C","E","E_HC","P_i_i-1","P_i_i+1","gamma"]
        # fitness_log_df = pd.DataFrame(index=range(generations+1), columns=columns)
        # fitness_log_df.index.name = "generation"
        # fitness_log_df["N"] = N
        # fitness_log_df.at[0,"i"] = current_i
        # fitness_log_df.at[0,"pi_H"] = payoff[0]
        # fitness_log_df.at[0,"pi_C"] = payoff[1]
        # fitness_log_df.at[0,"f_H"] = fitness[0]
        # fitness_log_df.at[0,"f_C"] = fitness[1]
        # fitness_log_df.at[0,"E"] = calculate_full_entropy(population)
        # fitness_log_df.at[0,"E_HC"] = calculate_entropy_healthy_cancer(N,current_i)
        # fitness_log_df.at[0,"P_i_i-1"] = 0
        # fitness_log_df.at[0,"P_i_i+1"] = 0
        # fitness_log_df.at[0,"gamma"] = -1 # marks an invalid gamma value

        # one generation is a one birth-death cycle:
        # fitness-proportional random cell division + random apoptosis
        # for g in range(generations):
        # select one cell to divide
        # selected = toolbox.select_roulette(population)
        # create a copy
        # offspring = toolbox.clone(selected)
        # apply mutation on the offspring
        # offspring = toolbox.mutate(offspring)
        # add the new cell to the population
        # population.append(offspring)
        # select one cell to die
        # selected = toolbox.select_random(population)[0]
        # population.remove(selected)
        # after each generation the number of cancer cells 'i' might change
        # fitness of each cell depends on 'i'
        # that is why after each birth-death cycle we need to
        # re-evaluate the fitnesses of all cells in the population
        # current_i = estimate_cancer(population)
        # payoff, fitness, = prisoners_dilemma_fitness_evaluate(A, N, current_i, w)
        # for ind in population:
        #    if is_cancer(ind):
        #        ind.fitness = fitness[1]
        #    else:
        #        ind.fitness = fitness[0]
        # dump the population at generation g to a txtfile
        # dump_population_with_fitness(populations_dir,population,str(g+1)+"_population.txt")
        # update the log dataframe
        # fitness_log_df.at[g+1,"i"] = current_i
        # fitness_log_df.at[g+1,"pi_H"] = payoff[0]
        # fitness_log_df.at[g+1,"pi_C"] = payoff[1]
        # fitness_log_df.at[g+1,"f_H"] = fitness[0]
        # fitness_log_df.at[g+1,"f_C"] = fitness[1]
        # fitness_log_df.at[g+1,"E"] = calculate_full_entropy(population)
        # fitness_log_df.at[g+1,"E_HC"] = calculate_entropy_healthy_cancer(N,current_i)
        # fitness_log_df.at[g+1,"P_i_i-1"] = fitness[0]*(N-current_i)/(current_i*fitness[1]+fitness[0]*(N-current_i))*current_i/N
        # fitness_log_df.at[g+1,"P_i_i+1"] = current_i*fitness[1]/(current_i*fitness[1]+fitness[0]*(N-current_i))*(N-current_i)/N
        # if fitness_log_df.at[g+1,"P_i_i-1"]==0 and fitness_log_df.at[g+1,"P_i_i+1"]==0:
        #    fitness_log_df.at[g+1,"gamma"] = -1
        # else:
        #    fitness_log_df.at[g+1,"gamma"] = fitness_log_df.at[g+1,"P_i_i-1"] / fitness_log_df.at[g+1,"P_i_i+1"]
