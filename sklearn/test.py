# coding=UTF-8
from __future__ import division
__author__ = 'krilo'

import sklearn
print sklearn.__version__



xbar = (6 + 8 + 10 + 14 + 18) / 5
variance = ((6 - xbar)**2 + (8 - xbar)**2 + (10 - xbar)**2 + (14 - xbar)**2 + (18 - xbar)**2) / 4
print variance

