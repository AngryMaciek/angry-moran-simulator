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