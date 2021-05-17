import math
from IntegralMethods.RectangleIntegration import leftrectangle, rightrectangle
from IntegralMethods.TrapezoidIntegration import trapezoid
from math import sin, exp, pi
import numpy as np
import matplotlib.pyplot as plt


leftrect = []
rightrect = []
trapez = []
sol = (2/13)+(3/13*np.e**(3/4*np.pi))
step = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5, 10**-6, 10**-7]


def f(x):
    return np.e**(3*x)*np.sin(2*x)


if __name__ == "__main__":

    for i in step:
        leftrect.append(abs(sol - leftrectangle(0, pi/4, i, f)))
        rightrect.append(abs(sol - rightrectangle(0, pi/4, i, f)))
        trapez.append(abs(sol - trapezoid(0, pi/4, i, f)))

    print(leftrect)
    print(rightrect)
    print(trapez)

    plt.loglog(step, leftrect)
    plt.loglog(step, rightrect)
    plt.loglog(step, trapez)
    plt.legend(["Left", "Right", "Trap"])

    plt.show()
