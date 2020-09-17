# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Daniel Mireles
#               Jordan Nguyen
#               Tan Nguyen
#               Fern Moreno
# Section:      540
# Assignment:   4 - 2
# Date:         19 September 2019

from math import *

print('''This program was created to calculate the fee one has to pay after parking for a certain amount of time given prices''')

hour = float(input("Please input the number of hours you parked at our parking lot. Please round hours up to a whole number. Eg: 5 hours and twenty minutes would be inputted as 6 hours. If your ticket is lost, please input the number of hours parked as a negative value: "))
hours = ceil(hour)

pay = 0

#Charge if ticket is lost.
if hours < 0:
	hours = abs(hours)
	pay = 36

#Charge per day
if hours > 24:
	days = hours // 24
	pay += days * 24
	hours = (hours - days*24)
	
#Charge per hour
if hours > 0 and hours <= 2: 
	pay += 4
elif hours > 2 and hours <= 4: 
	pay += 7
elif hours > 4 and hours <= 21: 
	pay += 7
	hours -= 4
	pay += hours
elif hours > 21 and hours <= 24: 
	pay += 24
    
print()   
print("Your fee is: ",pay)