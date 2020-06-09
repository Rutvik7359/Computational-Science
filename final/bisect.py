# Python function for bisection

import math
import scipy as sc


def bisection(l, r, f(x), kmax, epsX, epsF):
    for i in range(kmax):
        m = (l+r)/2
        err = abs(l-r)/2
        res = abs(f(m))
        print("k=",i," l=",l," r=",r," err=",err)
        if err < epsX:
            print("Bisection Converged.")
            break       
        if f(l)*f(m) > 0:
            l = m
        else:
            r = m
        
        if i+1 == kmax:
            print("No Convergence")

    return m, err

print(bisection(0.0, 2.0, ((1/x) - (x/2)), 50, 10**-6, 1e-12))