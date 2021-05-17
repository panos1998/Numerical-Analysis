from IntegralMethods.RectangleIntegration import leftrectangle, rightrectangle
from IntegralMethods.TrapezoidIntegration import trapezoid
from math import sin, exp, pi
import numpy as np



def f(x):
    return np.e**(3*x)*np.sin(2*x)



if __name__ == "__main__":
    leftrectangle(0,pi/4, 10**-3 ,f)
    rightrectangle(0,pi/4, 10**-2 ,f)
    trapezoid(0, pi/4,10**-5 , f,(2/13)+(3/13*np.e**(3/4*np.pi)) )