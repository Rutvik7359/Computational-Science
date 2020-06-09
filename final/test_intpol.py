import numpy
import numpy.linalg
import matplotlib.pyplot as plt


# creating interpolant function
def Intpl(xs,ys):
    n = numpy.shape(xs)[0] - 1                          #intial size of n             
    V = numpy.zeros((n+1,n+1))                          #allocation for vandermonde matrix
    
    for i in range(0,n+1):                              #computing matrix elements
        V[i,0] = 1.0                                    #set 1st column of matrix to 1s
        for j in range(1,n+1):                      
            V[i,j] = V[i,j-1] * xs[i]

    a = numpy.linalg.solve(V, ys)                       #solving for coefficients
    print("Vandermonde Matrix =")                       #printing vandermonde matrix
    print(V)
    print("\ncoeff(a) =")                               #printing coefficients
    print(a)
    return a
 
xi = numpy.array([-1.2,0.5,2.2,3.1])
yi = numpy.array([-0.4,1.2,5.5,10.2])  
c = Intpl(xi,yi)

x = numpy.linspace(-1.7,3.6,1000)                      #1000 number samples from -1.7 to 3.6
y = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3              #y values for each sample


#plt.plot(xi,yi,'*')
#plt.plot(x,y,'-')                           	       #plotting interpolant and table points
#plt.title("Interpolant and Points")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()
