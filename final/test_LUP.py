# Test script for linear solving with LUP decomposition. L. van Veen, Ontario Tech U, 2020.
import numpy as np
from LUP import *
# Set test matrix and right hand side:
A = np.array( [[1.2,4.1,-2.0],[-0.2,0.1,6.0],[-0.5,2.3,5.3]])
y = np.array([[-4.2],[1.5],[-0.2]])
# Compute the factors L and U:
L,U,P,par,ok = LUP(A)
if ok==0:
    print("The example matrix was nearly singular.")
print(L)
print(U)
print(P)
print("If the elements of the following matrix are not zero up to round-off error, there is something wrong:")
print(np.dot(L,U)-np.dot(P,A))
# Now find the solution to A x = y.
# First solve L z = y:
z = ForwardSub(L,P,y)
# Then solve U x = z:
x = BackwardSub(U,z)
print("forward(y1,y2,y3) =")
print(z)
print("backward(x1,x2,x3) =")
print(x)
print("If the elements of the following vector are not zero up to round-off error, there is something wrong:")
print(np.dot(A,x) - y)
