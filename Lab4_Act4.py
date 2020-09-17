# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Daniel Mireles
#               Jordan Nguyen
#               Tan Nguyen
#               Fern Moreno
# Section:      540
# Assignment:   4b - 4
# Date:         19 September 2019

#This program outputs the root(s) of the quadratic equation given inputs from the user.

import cmath

A = float(input("Please input your A value here: "))
B = float(input("Please input your B value here: "))
C = float(input("Please input your C value here: "))

D = (B**2) - (4*A*C)

root_1 = (-B-cmath.sqrt(D))/(2*A)
root_2 = (-B+cmath.sqrt(D))/(2*A)
print()
print("The roots are", root_1, "and", root_2)