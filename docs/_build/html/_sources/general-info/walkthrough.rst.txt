#################
Quick Walkthrough
#################

*Moran Pycess* is a Python package with a general game-theoretical framework
for scientific simulations according to the Moran model. It is aimed to
capture dynamics of populations composed of individuals of distinct phenotypes
(which correspond to strategies in the language of game theory).
Individual's fitness is calcualted based on its average payoff, averaged over
interactions with other members of the group. The package is both simple in
use and robust, allowing any possible model of an antagonistic game to be
considered. It serves well as a research aid for evolutionary, computational
as well as cell biologists as it allows to simulate two-dimensional and
three-dimensional populations too.

General Moran Model
###################

From the user's perspective only one class is relevant: *MoranProcess*.

Initializer of this class has the follwing signature::

  def __init__(
    self,
    size_list,
    label_list,
    BirthPayoffMatrix,
    DeathPayoffMatrix,
    TransitionMatrix=None
  ):

  # size_list: list of integers which represent the cardinality of 
  # distinct sub-populations

  # label_list: list of strings which represent the labels of individuals
  # from distinct sub-populations

  # BirthPayoffMatrix: payoff matrix based on which individuals' Birth Fitness
  # is calculated. Used for the roulette-based selection of an individual to reproduce

  # DeathPayoffMatrix: payoff matrix based on which individuals' Death Fitness
  # is calculated. Used for the roulette-based selection of an individual to die

  # TransitionMatrix: an optional parameter: a matrix similar to Birth/Death
  # payoffs which specifies transition probabilities from a given
  # Strategy (rows) to another (columns). Row sums must equal to one.
  # If this parameter is specified at the end of each Birth-Death cycle each of
  # the individuals will randomly sample to switch Strategies.

Both individuals' selection for reproduction and death are proportional to
individuals' fitnesses calculated based on two separate payoff matrices
(Birth/Death). For a random selection please provide a *numpy* array
composed entirely of one-values.
**Payoffs always need to be non-negative.**

Example of creating a *MoranProcess* instance::

  import numpy as np
  import moranpycess

  size_list = [10, 10]
  label_list = ["a", "b"]
  BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
  DeathPayoffMatrix = np.array([[0.1, 0.2], [0.3, 0.4]])

  mp = moranpycess.MoranProcess(
    size_list=size_list,
    label_list=label_list,
    BirthPayoffMatrix=BirthPayoffMatrix,
    DeathPayoffMatrix=DeathPayoffMatrix,
  )

The key method of this object is a called :samp:`simulate(generations)`
and it takes an integer as an argument (simulation time specified as a number
of birth-death cycles). This function returns a *pandas* dataframe with
a per-cycle summary of the population's state.
The following code demonstrates the simulation::

  import pandas as pd
  df = mp.simulate(1000)

Information which are stored in the dataframe's columns include:

* per-sub-population sub-population's size
* per-sub-population Average Birth Payoff for a single individual of a given sub-population (averaged over interactions with all other individuals of the whole population)
* per-sub-population Average Death Payoff for a single individual of a given sub-population (averaged over interactions with all other individuals of the whole population)
* per-sub-population Birth Fitness of an individual from a given sub-popualtion
* per-sub-population Death Fitness of an individual from a given sub-popualtion
* Entropy of the distribution of Strategies in the whole population

The class is equipped with several plotting methods to visualise results of the simulation:

* :samp:`PlotSize`
* :samp:`PlotAvgBirthPayoff`
* :samp:`PlotAvgDeathPayoff`
* :samp:`PlotBirthFitness`
* :samp:`PlotDeathFitness`
* :samp:`PlotEntropy`

Each of which with the same signature::

  def FUNCTION(self, df, path):

  # df: simulation results - pandas dataframe returned by the method .simulate()
  # path: path for the output plot in png format

Following the previous simulation one may generate the plots with::

  mp.PlotSize(df, "Size.png")
  mp.PlotAvgBirthPayoff(df, "AvgBirthPayoff.png")
  mp.PlotAvgDeathPayoff(df, "AvgDeathPayoff.png")
  mp.PlotBirthFitness(df, "BirthFitness.png")
  mp.PlotDeathFitness(df, "DeathFitness.png")
  mp.PlotEntropy(df, "Entropy.png")

Moran Model based on 2D neighbourhood
#####################################

From the user's perspective only one class is relevant: *MoranProcess2D*.

Initializer of this class has the follwing signature::

  def __init__(
    self,
    size_list,
    label_list,
    grid,
    BirthPayoffMatrix,
    DeathPayoffMatrix,
    TransitionMatrix=None
  ):

  # All arguments are the same as for the class MoranProcess except the additional one:
  #
  # grid: 2-dimensional numpy array filled with strings from the "label_list"
  # according to their cardinality in "size_list". This argument essentially
  # specifies the initial spatial state of the population.

Similarly as in the previous case:  
Both individuals' selection for reproduction and death are proportional to
individuals' fitnesses calculated based on two separate payoff matrices (Birth/Death).  
However, the average payoffs (and therefore fitnesses) of each individual is
calculated based only on its direct neighbourhood in the population (8 neighbours).
For individuals at boundaries we apply periodic boundary conditions.  
For a random selection please provide a *numpy* array composed entirely of one-values.  
**Payoffs always need to be non-negative.**

Example of creating a *MoranProcess2D* instance::

  import numpy as np
  import moranpycess

  size_list = [3, 1]
  label_list = ["A", "B"]
  grid = np.array([["A", "A"], ["A", "B"]])
  BirthPayoffMatrix = np.array([[10, 10], [15, 1]])
  DeathPayoffMatrix = np.array([[1, 1], [1, 1]])

  mp = moranpycess.MoranProcess2D(
    size_list=size_list,
    label_list=label_list,
    grid=grid,
    BirthPayoffMatrix=BirthPayoffMatrix,
    DeathPayoffMatrix=DeathPayoffMatrix,
  )


Similarly as in the previous case:  
the key method of this object is a called :samp:`simulate(generations)` and it
takes an integer as an argument (simulation time specified as a number of
birth-death cycles). This function returns a `pandas` dataframe with a per-cycle
summary of the population's state.
The following code demonstrates the simulation::

  import pandas as pd
  df = mp.simulate(10)

In case of the simulation in 2D each Birth-Death cycle consist of the following steps:

1. Select an individual for reproduction (fitness-proportional selection)
2. Out of its neigbours: select an individual to die (fitness-proportional selection)
3. Copy the selected individual from (1) in place of the one from (2)
4. Perform Transitions for each individual (in case :samp:`TransitionMatrix` was specified)
5. Update Payoffs and Fitnesses

Information which are stored in the dataframe's columns include:

* per-sub-population sub-population's size
* Entropy of the distribution of Strategies in the whole population

The class is equipped with three plotting methods to visualise results of the simulation:

* :samp:`PlotSize2D`
* :samp:`PlotEntropy2D`
* :samp:`PlotPopulationSnapshot2D`

With :samp:`PlotSize2D` and :samp:`PlotEntropy2D` having the same signatures
as their previous analogues. The latter, :samp:`PlotPopulationSnapshot2D`,
may produce a heatmap-like snapshot of a population at it's current state. ::

  def PlotPopulationSnapshot2D(self, path):

  # path: path for the output plot in png format

Following the previous simulation one may generate the plots with::

  mp.PlotSize2D(df, "Size2D.png")
  mp.PlotEntropy2D(df, "Entropy2D.png")
  mp.PlotPopulationSnapshot2D("PopulationSnapshot2D.png")


Moran Model based on 3D neighbourhood
#####################################

From the user's perspective only one class is relevant: *MoranProcess3D*.

Initializer of this class has the follwing signature::

  def __init__(
    self,
    size_list,
    label_list,
    grid,
    BirthPayoffMatrix,
    DeathPayoffMatrix,
    TransitionMatrix=None
  ):


All arguments are the same as for the class *MoranProcess2D* with the note
that this time :samp:`grid` is a 3-dimensional array.

Similarly as in the previous case:  
both individuals' selection for reproduction and death are proportional to
individuals' fitnesses calculated based on two separate payoff matrices (Birth/Death).  
However, the average payoffs (and therefore fitnesses) of each individual is
calculated based only on its direct neighbourhood in the population (26 neighbours).
For individuals at boundaries we apply periodic boundary conditions.  
For a random selection please provide a *numpy* array composed entirely of one-values.  
**Payoffs always need to be non-negative.**

Example of creating a *MoranProcess3D* instance::

  import numpy as np
  import moranpycess

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


Similarly as in the previous cases:  
the key method of this object is a called :samp:`simulate(generations)` and it
takes an integer as an argument (simulation time specified as a number of
birth-death cycles). This function returns a *pandas* dataframe with a per-cycle
summary of the population's state.
The following code demonstrates the simulation::

  import pandas as pd
  df = mp.simulate(10)

In case of the simulation in 3D each Birth-Death cycle consist of the following steps:

1. Select an individual for reproduction (fitness-proportional selection)
2. Out of its neigbours: select an individual to die (fitness-proportional selection)
3. Copy the selected individual from (1) in place of the one from (2)
4. Perform Transitions for each individual (in case :samp:`TransitionMatrix` was specified)
5. Update Payoffs and Fitnesses

Information which are stored in the dataframe's columns include:

* per-sub-population sub-population's size
* Entropy of the distribution of Strategies in the whole population

The class is equipped with two plotting methods to visualise results of the simulation:

* :samp:`PlotSize3D`
* :samp:`PlotEntropy3D`

The functions have the same signatures as their previous analogues.  
Following the previous simulation one may generate the plots with::

  mp.PlotSize3D(df, "Size3D.png")
  mp.PlotEntropy3D(df, "Entropy3D.png")
