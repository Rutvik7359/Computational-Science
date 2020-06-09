import scipy

def tridag_matvec(a,b,c,x):
    n = scipy.size(x)
    y = scipy.zeros((n,1))
    for i in range(0,n-2):
        y[i,0]=a[i]*x[i]+b[i]*x[i+1]+c[i]*x[i+2]
    y[n-2,0]=a[n-2]*x[n-2]+b[n-2]*x[n-1]
    y[n-1,0]=a[n-1]*x[n-1]
    return y


