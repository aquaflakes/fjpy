# from __future__ import absolute_import

# import pandas as pd
# import numpy as np

# from . import tester

# Also importable from root
from .tester import printme


__all__ = [s for s in dir() if not s.startswith("_")]
__version__ = '2.2.0'