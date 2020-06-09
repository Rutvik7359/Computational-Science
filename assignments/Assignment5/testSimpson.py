# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:38:53 2020

@author: desai
"""
#Rutvik Desai
#100664467

import math
import numpy as np
import scipy as sp
from compositeSimpsons import compositeSimpsons
from compositeSimpsons import f

actual = sp.integrate.quad(lambda x:x*math.exp(-x**2),0,3)

M = 1
while(True):
    I = compositeSimpsons(f,0,3,M)
    err = abs(I-actual[0])
    if(err > 10**-12):
        M = M + 1
    
    else:
        break
    print("M: %d err: %e" %(M,err))