# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Daniel Mireles 
#               Noah Chavez
#               Carlos Chavez
#               Lidan Demoulin
# Section:      504 
# Assignment:   Lab 2 - 3
# Date:         05/09/2019
#

from math import*
time1 = 30
time2 = 45
dist1 = 50
dist2 = 615
speed = (dist2-dist1)/(time2-time1)
Current_Time=37

Current_Dist = speed*(Current_Time - time1)+dist1
print(Current_Dist)

Current_Time_2 = 20*60
Current_Dist_2 = speed*(Current_Time_2 - time1)+dist1

circumference= 2*500*pi
z = Current_Dist_2%circumference 
print(z)