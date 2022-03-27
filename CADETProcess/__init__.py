"""
CADET-Process
========

CADET-Process is a Python package for modelling, simulating and optimizing
advanced chromatographic systems. It serves as an inteface for CADET, but also
for other solvers.

See https://cadet-process.readthedocs.io for complete documentation.
"""
# Version information
name = 'CADET-Process'
__version__ = '0.5.2'

# Imports
from .CADETProcessError import *

from . import settings
from . import log
from . import dataStructure
from . import plotting
from . import dynamicEvents
from . import processModel
from . import solution
from . import reference
from .simulationResults import SimulationResults
from . import metric
from . import performance
from . import optimization
from . import comparison
from . import stationarity
from . import simulator
from . import fractionation
from . import equilibria
from . import modelBuilder

