import numpy as np
from math import sin, exp, pi, ceil


def f(x):
    return exp(3*x)*sin(2*x)

def trapezoid(start,end,h,f):
#    In=h/2[f(x0)+f(xn)]+np.sum(

    n = ceil((end - start) / h)

    x = np.linspace(start, end, n+1)  # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (end - start)/n
    T = (dx/2) * (np.sum(y_right + y_left))
    return T


print(trapezoid(0, pi/4, 10**(-3), f))
