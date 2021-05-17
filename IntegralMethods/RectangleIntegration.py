from math import ceil


def leftrectangle(start, end, h, f):

    xi = start

    total = 0

    n = ceil((end-start)/h)

    for i in range(n):
        xi = xi+h
        total = total + f(xi)

    leftrectangleIntegral = h*total

    return  leftrectangleIntegral


def rightrectangle(start, end, h, f):

    xi = end

    total = 0

    n = ceil((end-start)/h)

    for i in range(n):
        xi = xi-h
        total = total + f(xi)

    rightrectangleIntegral = h*total
    return rightrectangleIntegral