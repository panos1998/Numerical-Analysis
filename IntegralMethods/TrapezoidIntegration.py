import numpy as np
from math import sin, exp, pi, ceil


def f(x):
    return exp(3*x)*sin(2*x)

def trapezoid(start,end,h,f,SOL):
    points= ceil((end - start) / h)
    x = np.linspace(start, end, points+1)  # N+1 points make N subintervals
    y = f(x)
    T =(h / 2) * (y[0]+y[points]+np.sum(2*y[1:-1])) #approximation result
    print('This is trapezoid  method: '+ str(T))
    print('This is exact solution: '+ str(SOL))
    print('This is the error: '+ str(abs(T-SOL)))
    return T

