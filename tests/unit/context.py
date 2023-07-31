import os
import sys

# pythonpath modification to resolve the pkg modules properly during testing
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

import moranpycess  # noqa
