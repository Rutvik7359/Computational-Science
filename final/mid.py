import math 

def f(x):
	return math.cos(1+x**2)
	
def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

print(midpoint(f,-1.0,1.0,50))