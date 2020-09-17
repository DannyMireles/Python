# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Daniel Mireles
#               Jordan Nguyen
#               Tan Nguyen
#               Fern Moreno
# Section:      540
# Assignment:   4 - 1
# Date:         19 September 2019
#

from math import*
#Part 1 of activity 1. We are running the first code as instructed. The value of b is one.
a = 1/7
print(a)
b = a*7
print(b)
print()
#For part 2 we are running the code and seeing if the value of 'e' is one. In this case it is not one.
# define tolerance
TOL = 1e-10
a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print("b and e are equal within tolerance of", TOL)
else:
    print("b and e are NOT equal within tolerance of",TOL)
print()
#For the third part we are seeing if the value of y and z are one. 
#In this case, those value of y is one but z is not. 
TOL_1 = 1e-11
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
# check if y and z are equal within specified tolerance
if abs(y-z) < TOL_1:
    print("y and z are equal within tolerance of", TOL_1)
else:
    print("y and z are NOT equal within tolerance of",TOL_1)