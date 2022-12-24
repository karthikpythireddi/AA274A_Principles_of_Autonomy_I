#!/usr/bin/env python3
#import the required libraries
from ast import In
from cmath import pi
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


#Defined a sin function using NumPy
def sin(x):
    return math.sin(x)




#minimum of the sin function using SciPy
#initial guess
x_0 = 0
min = minimize(sin, x_0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print("The minimum of the sin function using scipy is: '{}' " .format(min.fun))


#integrate the function from [0,1] using scipy
from scipy.integrate import quad
result = quad(sin, 0, 1)
print("Integral of Sinx from 0 to 1 '{}'".format(result[0]))


#plot the function using matplotlib from [0,2*pi]
x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.title("Sine function using Line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
plt.scatter(x,y)
plt.title("Sine function using Scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


