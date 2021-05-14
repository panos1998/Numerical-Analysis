from IntegralMethods.RectangleIntegration import leftrectangle, rightrectangle
from math import sin, exp, pi


def f(x):
    return exp(3*x)*sin(2*x)


if __name__ == "__main__":
    leftrectangle(0,pi/4, 10**-3 ,f)
    rightrectangle(0,pi/4, 10**-2 ,f)