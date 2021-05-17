import numpy as np
from math import sin, exp, pi, ceil

def f(x):
    return exp(3*x)*sin(2*x)

def simpson(start, end, h, f):
    points = ceil((end - start) / h)
    x = np.linspace(start, end, 2*points + 1)  # N+1 points make N subintervals
    y = f(x)
    coefficient=[]
    for i in range(0,len(x),1):
        if (i == 0 or i == 2*points):
           coefficient.append(1)
        elif (i % 2):
            coefficient.append(4)
        else:
            coefficient.append(2)
    y_coeff=y*coefficient
    simpsonIntegral = h/6*(np.sum(y_coeff))
    return simpsonIntegral


