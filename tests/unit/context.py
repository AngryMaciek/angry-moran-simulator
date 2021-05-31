import os
import sys

# python path modification to resolve the package modules properly during testing
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

import moranpycess
