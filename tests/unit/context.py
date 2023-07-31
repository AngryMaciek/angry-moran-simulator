"""PYTHONPATH modification to resolve the pkg modules during testing."""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

import moranpycess  # noqa
