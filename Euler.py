import numpy as np

# x00 = 20
# x10 = 1


def euler(f, x0, t0, tmax, dt):

    t = np.arange(t0, tmax, dt)

    x = np.zeros((len(t), len(x0)))
    x[0, :] = x0
    for n in range(len(t)-1):
        x[n+1, :] = x[n, :] + dt*f(t[n], x[n, :])

    return t, x
