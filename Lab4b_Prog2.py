# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 4b
# Date:         09/19/2019
#
#Writing a program to determine if a flow is laminar, fully turbulent, or in transition
V = float(input("Please input the characteristic velocity of the flow in meters per second here: ")) #m/s
d = float(input("Please input the pipe diameter in meters here: ")) #meters
v = float(input("Please input the fluid kinematic viscocity in m^2/s here: ")) #m^2/s

rn = float(V*d/v)

if rn > 2900 :
    print("The flow is fully turbulent.")
    
elif rn <= 2900 and rn >= 2300:
    print("The flow is in transition.")
    
elif rn < 2300:
    print("The flow is laminar.")