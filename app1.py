import math
from IntegralMethods.RectangleIntegration import leftrectangle, rightrectangle
from IntegralMethods.TrapezoidIntegration import trapezoid
from IntegralMethods.SimpsonIntegration import simpson
from math import sin, exp, pi
import numpy as np
import matplotlib.pyplot as plt


leftrect = []
rightrect = []
trapez = []
simps = []
sol = (2/13)+(3/13*np.e**(3/4*np.pi))
step = [10**0,10**-1,10**-2,10**-3,10**-4, 10**-5,10**-6,10**-7,10**-8]


def f(x):
    return np.e**(3*x)*np.sin(2*x)


if __name__ == "__main__":

    for i in step:
        leftrect.append(abs(sol - leftrectangle(0, pi/4, i, f)))
        rightrect.append(abs(sol - rightrectangle(0, pi/4, i, f)))
        trapez.append(abs(sol - trapezoid(0, pi/4, i, f)))
        simps.append(abs(sol-simpson(0, pi/4, i, f)))


    print(leftrect)
    print(rightrect)
    print(trapez)
    print(simps)

    plt.loglog(step, leftrect)
    plt.loglog(step, rightrect)
    plt.loglog(step, trapez)
    plt.loglog(step, simps)
    plt.legend(["Left", "Right", "Trap","Simpson"])
    plt.ylim([10**-9,10])
    plt.xlabel("h")
    plt.ylabel("Error")
    plt.xlim([10,10**-8])
    plt.show()
