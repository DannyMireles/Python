# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 10b - 1
# Date:         11/04/2019
#

#import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

print("This program will export four graphs demonstrating different relationships.")
#import matrices
M = np.array([1.00583, -0.087156, 0.087156, 1.00583]).reshape(2,2)
v = np.array([[1,0]])

#define x,y, and p in order to use in the future
y = np.array([0])
x = np.array([1])
p = v.transpose() 

#create plot by appending points to the axes and repeating 200 times
for i in range(0,201):
    n = np.dot(M,p)
    y = np.append(y, n[1][0])
    x = np.append(x, n[0][0])
    p = n
    
#create the plot using plt 
plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Points Plotted Create a Spiral")
plt.show()