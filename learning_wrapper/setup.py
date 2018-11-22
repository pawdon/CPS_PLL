#! /usr/bin/env python

# System imports
from distutils.core import *
from distutils      import sysconfig

# Third-party modules - we depend on numpy for everything
import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

# cpll extension module
_cpll = Extension("_cpll",
                   ["cpll.i","cpll.c"],
                   include_dirs = [numpy_include],
                   )

# cpll setup
setup(  name        = "PLL loop",
        description = "PLL loop. Arguments are 3 arrays: carrier*2, carrier*3 and data for synchronization [freq, last_theta]",
        author      = "Pawel Donath",
        version     = "1.0",
        ext_modules = [_cpll]
        )
