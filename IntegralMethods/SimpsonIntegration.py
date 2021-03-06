import numpy as np
from math import sin, exp, pi, ceil

def f(x):
    return exp(3*x)*sin(2*x)

def simpson(start, end, h, f):
    points = ceil((end - start)*2/ h)
    x = np.linspace(start, end, points + 1)  # N+1 points make N subintervals
    y = f(x)
    coefficient = []
    for i in range(0,len(x),1):
        if (i == 0 or i == (len(x)-1)):
           coefficient.append(1)
        elif (i % 2):
            coefficient.append(4)
        else:
            coefficient.append(2)
    print("this is points:" +str(points))
    print(len(x))
    print(len(y))
    y_coeff = coefficient * y
    simpsonIntegral = h/6*(np.sum(y_coeff))
    return simpsonIntegral


