# Newton-Raphson code, written in lecture 12.
import numpy as np

def NR(x0,f,Df,epsx,epsf,itmx):
    x = np.copy(x0)
    for k in range(itmx):
        r = - f(x)
        J = Df(x)
        dx = np.linalg.solve(J,r)
        x += dx
        err = np.linalg.norm(dx,2)
        res = np.linalg.norm(r,2)
        print("%d err=%e res=%e" %(k,err,res))
        if err < epsx and res < epsf:
            print("Converged!")
            return x,err,res
    print("Warning: no convergence!")
    return x,err,res
