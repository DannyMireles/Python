# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab3b_Act4_Prog2
# Date:         09/12/2019

#This program takes the points observed by the user and
#calculates the angle, in degrees, between those two points
from math import *
#input point of observer
x0 = float(input("Enter initial x coordinate: "))
y0 = float(input("Enter initial y coordinate: "))
z0 = float(input("Enter initial z coordinate: "))
x0 = float(x0)
y0 = float(y0)
z0 = float(z0)

#input first point observed 

x1 = float(input("Enter first observed x value: "))
y1 = float(input("Enter first observed y value: "))
z1 = float(input("Enter first observed z value: "))
x1 = float(x1)
y1 = float(y1)
z1 = float(z1)

# input second point observed

x2 = float(input("Enter second observed x value: "))
y2 = float(input("Enter second observed y value: "))
z2 = float(input("Enter second observed z value: "))
x2 = float(x2)
y2 = float(y2)
z2 = float(z2)

#assigning vectors

vec1= (x1-x0,y1-y0,z1-z0)
vec2= (x2-x0,y2-y0,z2-z0)

#dot product of vectors 

top = sum([vec1[i]*vec2[i] for i in range(3)])

bottom = math.sqrt(sum([vec1[i]*vec1[i] for i in range(3)])) * math.sqrt(sum([vec2[i]*vec2[i] for i in range(3)]))

angle=(math.degrees(math.acos(top/bottom)))
Decimal ="%6.2f" % angle
print()
print("The angle between the points is:",Decimal, "degrees")