# Numerical-Analysis
Numerical Analysis methods in Python

### First Sector
We implemented four methods of ***Numerical Integration***:
1. ***Left rectangle***
2. ***Right rectangle***
3. ***Trapezoid***
4. ***Simpsons***

The target function to estimate its integral using the above methods is ![](https://i.ibb.co/RDysxvD/image.png).
Especially we calculated the following integral ![](https://i.ibb.co/SQJ9L7f/image.png).

#### Error Diagramm
Below the diagramm presents the difference between each method and the calculated  from the above integral  value.

![](https://i.ibb.co/sF1rPbB/image.png)

At the horizontal axis the step of discretation  h scales from ***1*** to ***10*** <sup>***-10***</sup>. 
At the vertical axis we see how the error is changing during h changes. Simpsons method seems to be the most efficient between others. In general as h is getting minimized the error also decreases. As we know from theory the trapezoid absolute error upper bound is given by ![](https://i.ibb.co/9rkHWyM/image.png). 
So Error has an analogous relation with  h. Similar  analogous relation have also the other methods (left-right rectangle and simpsons). That is why we have the above  diagramm
