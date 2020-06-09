# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:06:39 2018

@author: Ahmed Nadeem
"""

import numpy as np
import numpy.linalg as la

C = np.matrix([[1.2,45.3,-2.],[-0.2,0.1,65.0],[-0.5,2.3,75.]])
print(la.cond(C,2))
