from IntegralMethods.RectangleIntegration import leftrectangle, rightrectangle
from IntegralMethods.TrapezoidIntegration import trapezoid
from math import sin, exp, pi
import numpy as np

sol = (2/13)+(3/13*np.e**(3/4*np.pi))
def f(x):
    return np.e**(3*x)*np.sin(2*x)



if __name__ == "__main__":
    print("left error: "+str(abs(sol-  leftrectangle(0,pi/4, 10**-5 ,f))))
    print("right error: " + str(abs(sol -  rightrectangle(0,pi/4, 10**-5 ,f))))
    print("trap error: " + str(abs(sol - trapezoid(0, pi/4,10**-5 , f ) )))