# Python function for Newton iteration

import math

def f(x):
    return 1/x - x/2 

def df(x):
    return math.log(x) - 1/2

def Newton(x0, kMax, epsX, epsF):
# Input: initial point, max nr. of iterations, tolerance for error and residual
    x=x0
    conv=0                         # flag for convergence
    for k in range(kMax):
        r=f(x)                 # current function value
        dx=-r/df(x)            # update step
        err = abs(dx)              # current error estimate
        res = abs(r)              # current residual
        print("k="+str(k)+" x="+str(x)+" res="+str(res)+" err="+str(err))        
        if err < epsX and res < epsF:       # If converged ...
            print("Converged!")
            conv=1
            break
        x=x+dx
    
    if conv==0:
        print("No convergence!")
    return x,res,err

Newton(1.0, 20, 1e-2, 10**-6)




