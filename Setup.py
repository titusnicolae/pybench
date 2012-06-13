#!/usr/bin/env python

# Setup file for pybench
#
# This file has to import all tests to be run; it is executed as
# Python source file, so you can do all kinds of manipulations here
# rather than having to edit the tests themselves.
#
# Note: Please keep this module compatible to Python 1.5.2.
#
# Tests may include features in later Python versions, but these
# should then be embedded in try-except clauses in this configuration
# module.

# import sage.all before anything else
# this makes sure Sage is initialized as intended and we don't run
# into any unexpected segfaults
import sage.all

# Defaults
Number_of_rounds = 10
Warp_factor = 1

# Import tests

from tests import *
