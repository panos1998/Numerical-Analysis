import numpy as np
from math import sin, exp, pi, ceil



def f(x):
    return exp(3*x)*sin(2*x)

def trapezoid( start, end, h, f) :
    points= ceil((end - start) / h)
    x = np.linspace(start, end, points+1)  # N+1 points make N subintervals
    y = f(x)
    trapezoidIntegral = (h / 2) * (y[0]+y[points]+np.sum(2*y[1:-1])) #approximation result
    return trapezoidIntegral

