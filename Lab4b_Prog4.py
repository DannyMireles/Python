# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 4b
# Date:         09/19/2019
#

from math import sqrt

print("Solving equation ax^2 + bx + c \n")

a = int(input('Please enter value of a here: '))
b = int(input('Please enter value of b here: '))
c = int(input('Please enter value of c here: '))

determinant = b*b - 4*a*c;

if (a == 0 and b == 0) :
    print("There are infinite solutions.")
    
elif(a == 0 and b != 0) :
    print("There is just one root.")
    root = c/b
    print("Root: ", root)
    
elif (determinant < 0) :
    print("There are no real roots")
    x = sqrt(-determinant)/(2*a)
    print("Root1: %d + %.2fi" % (-b, x))
    print("Root2: %d + %.2fi" % (-b, -x))
    
else :
    root1 = (-b + sqrt(determinant))/(2*a)
    root2 = (-b - sqrt(determinant))/(2*a)
    print("Root1:", root1)
    print("Root2:", root2)