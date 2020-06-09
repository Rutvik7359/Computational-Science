import math 

def f(x):
	return math.cos(1+x**2)
	
def trapezoidal(f, a, b, n):
	h = float(b-a)/n
	result = 0.5*f(a) + 0.5*f(b)
    	for i in range(1, n):
        	result += f(a + i*h)
    	result *= h
    	return result

print(trapezoidal(f,-1.0,1.0,50))