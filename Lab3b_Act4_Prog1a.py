# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab3b_Act4_Prog1a
# Date:         09/12/2019
#

from math import*
#Calculate the Voltage across a conductor with resistance in Ohms and current in Amperes.
print("This program calculates voltage given resistance in ohms and current in amperes ")
Resistance = float(input("Please input the amount of resistance in Ohms: ")) #Ohms
Current = float(input("Please input the amount of current in Amps: ")) #Amperes
Volts = (Resistance*Current)
MyString = "%6.4f" % Volts
print("The amount of Volts is equal to", MyString, "V.")
