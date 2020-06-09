# -*- coding: utf-8 -*-
"""
Created on Sun Mar  18 18:04:26 2020

@author: desai
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as pl

#stores linear equation of x values as a matrix
def LinXMat(x):
    n=np.shape(x)[0]
    A=np.zeros((n,2))
    for i in range(n):
        for j in range(2):
            A[i][j]=x[i]**j
    return A

#This function solves the least squares polynomial equation at the input x values  
def lstsqr(x,coeff):
    y1=[]
    n=np.shape(x)[0]
    for i in range(n):
        total=0
        for j in range(2):
            total+=(x[i]**j)*coeff[j]
        y1.append(total)
    return np.array(y1)

def lstsqrError(y,y1):
    res=(y-y1)**2
    ErrSize=0
    for i in range(len(res)):
        ErrSize+=res[i]
    return ErrSize
    

#x values
x=np.array([-2,0.25,0.9,1])
#y values
y=np.array([2.23,4.29,5.12,6.3])


A=LinXMat(x)
print("The constraints represented as a matrix of system of linear equations is:")
print(A,'\n')

#algorithm that computes the coefficients of the least squares approximation
a=np.matmul(np.transpose(A),A)
b=np.matmul(np.transpose(A),y)
coeff=np.linalg.solve(a,b)


print("The coefficients of the linear least squares fit are:")
print(coeff, '\n')

y1=lstsqr(x,coeff)

print("The values of the least squares polynomial evaluated at the x values are:")
print(y1 , '\n')

ErrSize=lstsqrError(y,y1)

print("The size of the error is:")
print(ErrSize)

#compute the interpolant's value at various x values
interpX=np.linspace(x[0],x[len(x)-1],100)
interpY=lstsqr(interpX,coeff)

#plot original values and the new interpolant values
pl.scatter(x,y)
pl.plot(interpX,interpY)
pl.xlabel("x")
pl.ylabel("y")
pl.title("Least Squares Interpolant")
pl.show