from Euler import euler
import numpy as np
import matplotlib.pyplot as plt


F = lambda t, x: np.array([1.1 * x[0] - 0.4 * x[0] * x[1], 0.4 * x[0] * x[1] - 0.1 * x[1]])
x0 = [20, 1]
t0 = 0
tmax = 200
dt = [0.1,0.01]
for dt in dt:
 t, x = euler(F, x0, t0, tmax, dt)

 print(t,x)

 plt.figure(1)
 plt.plot(t,x[:, 0],"b-",t,x[:, 1],"r--")
 plt.grid()
 plt.title("Time Evolution of Foxes Population and Rabbits Population")
 plt.legend(["Rabbits","Foxes"])
 plt.xlabel("time")
 plt.ylabel("No. of Rabbits and No. of Foxes")
 plt.show()

 plt.figure(2)
 plt.plot(x[:, 0], x[:, 1], "k--")
 plt.grid()
 plt.title("Phase Plot")
 plt.xlabel("X")
 plt.ylabel("Y")

 plt.show()
