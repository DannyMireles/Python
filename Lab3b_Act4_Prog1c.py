# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab3b_Act4_Prog1c
# Date:         09/12/2019
#

from math import*
#Calculate the shear stress (lbf/in^2) for a given normal stress (lbf/in^2) that is applied to a 
#material with a given cohesion (lbf/in^2) and angle of internal friction (degrees)
print("This program calculates the shear stress of an object given normal stress in lbf/in^2, cohesion in lbf/in^2, and angle of internal friction in degrees.")
Normal_Stress = float(input("Please input the normal stress in lbf/in^2: ")) #lbf/in^2
Cohesion = float(input("Please input the cohesion in lbf/in^2: ")) #lbf/in^2
Angle = float(input("Please input the angle of internal friction in degrees: "))
Shear_Stress = Normal_Stress*(tan(Angle*pi/180)+Cohesion)
MyString = "%6.4f" % Shear_Stress
print("The shear stress is", MyString, "lbf/in^2.")