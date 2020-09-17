# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab3b_Act4_Prog1d
# Date:         09/12/2019
#

#Calculate the production of a well (barrels/day) after a given number of days, for a given initial
#production rate (barrels/day), initial decline rate (barrels/day), and hyperbolic constant (no
#dimensions).
print("This program calculates the production of a well (barrels/day) after a given number of days for a given initial production rate (barrels/day), initial decline rate (barrels/day), and hyperbolic constant.")
Initial_Production_Rate = float(input("Please input the initial production rate in barrels/day: ")) #barrels/day
Initial_Decline_Rate = float(input("Please inpute the initial decline rate in barrels/day: ")) #barrels/day
Hyperbolic_Constant = float(input("Please insert the hyperbolic constant: ")) #NoConstants
Arps_Equation = Initial_Production_Rate/((1+(Hyperbolic_Constant*Initial_Decline_Rate*Time))**(1/Hyperbolic_Constant))
Decimal = "%6.4f" % Arps_Equation
print ("The prodcution of the well is", Decimal, "barrels/day.")
