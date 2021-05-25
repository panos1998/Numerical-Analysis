# Numerical-Analysis
Numerical Analysis methods in Python by ***Theofilos Panagiotou 9164 & Panagiotis Petridis 9286***

### First Sector
We implemented four methods of ***Numerical Integration***:
1. ***Left rectangle***
2. ***Right rectangle***
3. ***Trapezoid***
4. ***Simpsons***

Inside file app1.py we run the functions from folder IntegralMethods and we print the errors and the result diagramm for each h.

The target function to estimate its integral using the above methods is ![](https://i.ibb.co/RDysxvD/image.png).
Especially we calculated the following integral ![](https://i.ibb.co/SQJ9L7f/image.png).

#### Error Diagramm
Below the diagramm presents the differforence between each method and the calculated  from the above integral  value.

![](https://i.ibb.co/sF1rPbB/image.png)

At the horizontal axis the step of discretation  h scales from ***1*** to ***10*** <sup>***-8***</sup>. 
At the vertical axis we see how the error is changing during h changes. Simpsons method seems to be the most efficient between others. In general as h is getting minimized the error also decreases. As we know from theory the trapezoid absolute error upper bound is given by:<br>
![](https://i.ibb.co/9rkHWyM/image.png).<br>So Error has an analogous relation with  h. Similar  analogous relation have also the other methods (left-right rectangle and simpsons). That is why we have the above  diagramm.

### Second Sector
In this section we implemented the euler method for system of differential equations. The two pair of plots is the results from running the method with dx=0.1 and the second pair with dx=0.01
![](https://i.ibb.co/TBD1Kkx/image.png) ![](https://i.ibb.co/tpWS0v1/image.png)
![](https://i.ibb.co/2MZdx1s/image.png)
![](https://i.ibb.co/8rP2Wpz/image.png)

Inside file app2.py we call euler function from Euler.py for each set of initial values for the foxes and rabbits. Then we print the results and phaseplot.

What we observe is that with lower dx the  number of rabbits and  foxes after instantly changing, then we have a period of time where both are zero and then come back to initiall state and then we have a revision. As with the numerical integration, decreasing the h length we take a  more presice solution. Since the error in euler has an quadratic analogous relation with h, we think that in the second try with h=0.01 we have less error.
