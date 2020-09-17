# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 2b
# Date:         09/03/2019
#

from math import*
print ()
print ("Daniel Mireles, 230002497, ENGR 102 - 540")
print ()
print ("I am interested in music production and have been producing music for 7 years.")
print ()
#Calculate the Voltage across a conductor with resistance of 20 Ohms and current of 5 Amperes.
Resistance = 20 # Ohms
Current = 5 # Amps
Voltage = Resistance * Current # Volts
print ("The voltage across conductor is", Voltage, "V.") #Voltage across a conductor in V
print ()  
#Calculate the kinetic energy of an object of mass of 100kg and velocity of 21 m/s
Mass = 100 # kg
Velocity = 21 # m/s
kinetic_energy = 0.5 * Mass * (Velocity**2) # Joules
print ("The kinetic energy of this object is", kinetic_energy, "J.") #The kinetic energy of this object in m/s
print ()
#Calculate the Reynolds number for a for a fluid with velocity of 100m/s and kinematic viscocity of 1.2 (m^2/s) with a characteristic linear dimension of 2.5m.
Velocity = 100 # m/s
Kinematic_Viscocity = 1.2 # m**2/s
Linear_Dimension = 2.5 # m
Reynolds_Number = (Velocity*Linear_Dimension)/(Kinematic_Viscocity)
print ("The Reynolds number for this this fluid if", Reynolds_Number, ".")
print ()
#Calcuate the production of a of a well after 20 days, with an initial production of 100 barrels a day, an initial decline of 2 barrels a day, and hyperbolic constant of 0.8.
Initial_Production_Rate = 100 #barrels/day
Initial_Decline_Rate = 2 #barrels/day
Hyperbolic_Constant = 0.8
Time = 20 #days
Arps_Equation = Initial_Production_Rate/((1+(Hyperbolic_Constant*Initial_Decline_Rate*Time))**(1/Hyperbolic_Constant))
print ("The prodcution of the well after 20 days is", Arps_Equation, "barrels.")
print ()
#Calculate the shear stress when a normal stress of 20 lbf/in^2 is applied to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees.
Normal_Stress = 20 #lbf/in**2
Cohesion = 2 #lbf/in**2
Angle = 35#degrees
Shear_Stress = Normal_Stress*(tan(Angle*pi/180)+Cohesion)
print ("The shear stress is", 20*(tan(35*pi/180))+2, "lbf/in^2.")