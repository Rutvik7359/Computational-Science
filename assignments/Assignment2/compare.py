import scipy
import time                              # For timing
import matplotlib.pyplot as plt          # For plotting
from tridag_matvec import *

wall1 = [] # Initialize the lists of wall times
wall2 = []
for k in range(2,15):                    # Loop over matrix sizes
    n = 2**k
    a = scipy.random.rand(n,1)           # Set up random tridiagonal matrix and right hand side
    b = scipy.random.rand(n-1,1)
    c = scipy.random.rand(n-2,1)
    x = scipy.random.rand(n,1)

    start=time.time()                    # Get start time
    y = tridag_matvec(a,b,c,x)           # Compute the product
    elapsed = time.time() - start        # Compute and store wall time
    wall1.append([n,elapsed])

    A = scipy.zeros((n,n))
    for i in range(0,n):
        A[i,i]=a[i]
    for i in range(0,n-1):
        A[i,i+1] = b[i]
    for i in range(0,n-2):
        A[i,i+2] = c[i]
    start=time.time()                    # Get start time
    y = scipy.dot(A,x)                   # Compute the product
    elapsed = time.time() - start        # Compute and store wall time
    wtimes2.append([n,elapsed])
wall1 = scipy.asarray(wall1)
wall2 = scipy.asarray(wall2)
plt.loglog(wall1[:,0],wall1[:,1],'-k*',wall1[:,0],1E-5*wall1[:,0],'r-')
plt.loglog(wall2[:,0],wall2[:,1],'-k*',wall2[:,0],1E-9*wall2[:,0]**2,'g-')
plt.xlabel('matrix size')
plt.ylabel('wall time of product')
plt.title('Red line indicates O(n), green is O(n^2)')
plt.show()

