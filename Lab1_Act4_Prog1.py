# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 1b - 1
# Date:         08/27/2019
#

#
# YOUR CODE HERE
from math import*
print ("I am a Mexican citizen who has lived 14 years in Texas and one in Germany.")
print()
#Calculate the Voltage across a conductor with resistance of 20 Ohms and 
#current of 5 Amperes. 
print ("The voltage across conductor is", 20*5, "V.")
print ()
#Calculate the kinetic energy of an object of mass of 100kg and velocity of 21 m/s
print ("The Kinetic energy of this object is", 0.5*100*(21**2), "J.")
print ()
#Calculate the Reynolds number for a for a fluid with velocity of 100m/s and kinematic viscocity of 1.2 (m^2/s) with a characteristic linear dimension of 2.5m.
print ("The Reynolds number for this this fluid if", 100*2.5/(1.2), ".")
print ()
#Calcuate the production of a of a well after 20 days, with an initial production of 100 barrels a day, an initial decline of 2 barrels a day, and hyperbolic constant of 0.8.
print ("The prodcution of the well after 20 days is", 100/((1+(0.8*2*20))**(1/0.8)), "barrels.")
print ()
#Calculate the shear stress when a normal stress of 20 lbf/in^2 is applied to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees.
print ("The shear stress is", 20*(tan(35*pi/180))+2, "lbf/in^2.")