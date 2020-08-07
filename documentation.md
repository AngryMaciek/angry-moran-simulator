Our software is written as a Python package.  
From the user's perspective only one class is relevant: *MoranProcess*.

Initializer of the *MoranProcess* has the follwing sygnature:
```python
def __init__(self, size_list, label_list, BirthPayoffMatrix, DeathPayoffMatrix):
```

With the following arguments:
```python
size_list # list of integers which represent the cardinality of distinct sub-populations

label_list # list of strings which represent the labels of individuals from distinct sub-populations

BirthPayoffMatrix # payoff matrix based on which individuals' Birth Fitness is calculated. Used for the roulette-based selection of an individual to reproduce

DeathPayoffMatrix # payoff matrix based on which individuals' Death Fitness is calculated. Used for the roulette-based selection of an individual to die
```

Both individuals' selection for reproduction and death are proportional to individuals' fitnesses calculated based on two separate payoff matrices (Birth/Death). For a *random* selection please provide a `numpy` array composed entirely of single values.  
**Payoffs always need to be non-negative**

Example of creating a *MoranProcess* instance:  
(assuming working in an environment where the package is installed)

```python
import numpy as np
import moran_simulator as ms

size_list = [10, 10]
label_list = ["a", "b"]
BirthPayoffMatrix = np.array([[1, 2], [3, 4]])
DeathPayoffMatrix = np.array([[0.1, 0.2], [0.3, 0.4]])

mp = ms.MoranProcess(
    size_list=size_list,
    label_list=label_list,
    BirthPayoffMatrix=BirthPayoffMatrix,
    DeathPayoffMatrix=DeathPayoffMatrix,
)
```

The key method of this object is a called `simulate(generations)` and it takes an integer as an argument (simulation time specified as a number of birth-death cycles). This function returns a `pandas` dataframe with a per-cycle summary of the population's state.
The following code demonstrated the simulation:
```python
import pandas as pd

df = mp.simulate(1000)
```

Information which are stored in the dataframe's columns include:
* per-sub-population sub-population's size
* per-sub-population Average Birth Payoff for a single individual of a given sub-population (averaged over interactions with all other individuals of the whole population)
* per-sub-population Average Death Payoff for a single individual of a given sub-population (averaged over interactions with all other individuals of the whole population)
* per-sub-population Birth Fitness of an individual from a given sub-popualtion
* per-sub-population Death Fitness of an individual from a given sub-popualtion
