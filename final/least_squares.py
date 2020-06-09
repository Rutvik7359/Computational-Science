# Example solution for A4 Q2. By L. van Veen, Ontario Tech U, 2020.
import numpy as np

# Values from the table:
#x values
xs=np.array([-2.00,0.25,0.90,1.50,2.00])
#y values
ys=np.array([0.99,1.44,1.59,2.35,3.24])

# Compute the Vandermonde matrix:
n = np.shape(xs)[0]-1                    # Extract the n from the input.
V = np.zeros([n+1,2])                    # Allocate the Vandermonde matrix.
for i in range(0,n+1):                   # Fill the Vandermonde matrix V.
    V[i,0] = 1.0
    for j in range(1,2):
        V[i,j] = V[i,j-1] * xs[i]

# Find the least-squares solution and print the error:
a,err = np.linalg.lstsq(V,np.reshape(ys,n+1,1))[0:2]         # Find the least-squares solution to the overdetermined system V a = Y
print("The least-squares error is %f." % (err))

# Define the interpolant for plotting:
def P(z):                                # The polynomial approximant.
    return a[0] + a[1] * z

# Evaluate the interpolant on a fine grid of x-values and plot the result along with the data:
M = 10                                   # Number of points for plotting.
l = xs[0]   - 0.5                        # Set plot range.
r = xs[n-1] + 0.5
dx = (r-l)/float(M)
xp = np.zeros([M,1])
yp = np.zeros([M,1])
for k in range(0,M):                     # Evaluate the approximant on M points.
    xp[k] = l+float(k)*dx
    yp[k] = P(xp[k])

