# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 1b - 2
# Date:         08/29/2019
#

#
from math import*
# Evaluate 5x / (x-2) at x = 2
print ("This shows the evaluation of fx=sin*x/x as it approaches 0")
print ("My guess is fx=1")
print (sin(1)/(1))
print (sin(.1)/(.1))
print (sin(.01)/(.01))
print (sin(.001)/(.001))
print (sin(.0001)/(.0001))
print (sin(.00001)/(.00001))
print (sin(.000001)/(.000001))
print (sin(.0000001)/(.0000001))
print()
print ("This shows the evaluation of fx=(1-cos*x)/(x**2) as it approaches 0")
print ("My guess is fx=-1,000,000")
print (1-(cos(1))/(1**2))
print (1-(cos(.1))/(.1**2))
print (1-(cos(.01))/(.01**2))
print (1-(cos(.001))/(.001**2))
print (1-(cos(.0001))/(.0001**2))
print (1-(cos(.00001))/(.00001**2))
print (1-(cos(.000001))/(.000001**2))
print (1-(cos(.0000001))/(.0000001**2))
print ()
print ("This shows the evaluation of fx=((1+(1/x))**x) as it approaches infinity")
print ("My guess is fx=3")
print ((1+(1/1))**1)
print ((1+(1/10))**10)
print ((1+(1/100))**100)
print ((1+(1/1000))**1000)
print ((1+(1/10000))**10000)
print ((1+(1/100000))**100000)
print ((1+(1/1000000))**1000000)
print ((1+(1/10000000))**10000000)