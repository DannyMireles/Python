# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab3b_Act4_Prog1b
# Date:         09/12/2019
#

from math import*
#Calculate the Kinetic Energy of an object with mas in kilograms and velocity in m/s
print("This program calculates kinetic energy of an object given mass in kilograms and velocity in m/s.")
mass = float(input("Please input the mass in kilograms: ")) #kilograms
velocity = float(input("Please input the velocity in m/s: ")) #m/s
Kin_En = (0.5*mass*velocity**2)
MyString = "%6.4f" % Kin_En
print("The amount of Kinetic Energy is equal to", MyString, "J.")