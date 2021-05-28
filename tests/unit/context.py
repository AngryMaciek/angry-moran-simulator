import os
import sys

# python path modification to resolve the package modules properly during testing
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "moranpycess")),
)

import Individual
import MoranProcess
import MoranProcess2D
import MoranProcess3D
import CustomExceptions
