# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:06:03 2020

@author: desai
"""
#Rutvik Desai
#100664467
import math
import numpy as np
import scipy as sp

def f(x):
    return math.exp(-x**3)

def compositeSimpsons(f,a,b,M):
    x = sp.linspace(a,b,M+1)
    h = (b-a)/float(M)
    I = 0.0 
    
    for i in range(1,M+1):
        I += (h/6.0) * (f(x[i-1]) + 4 * f((x[i-1] + x[i])/2.0) + f(x[i])) 
    return I

print(compositeSimpsons(f,0.0,1.0,4))