# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 1b
# Date:         11/14/2019

#import libraries needed
import math

#Problem 1
#import definition of problem 1 as VolumeRemaining, assigning length, width,height,and redius
def VolumeRemaining(length,width,height,radius):
    Volume_Box = (length*width*height)
    Volume_Hole = math.pi*(radius**2)*height
    return Volume_Box - Volume_Hole
#end of VolumeRemaining

#Ask the user to input values needed
length=float(input("Enter length of the box:"))
width=float(input("Enter width of the box:"))
height=float(input("Enter height of the box:"))
radius=float(input("Enter radius of the hole:"))

#create a variable for the minimum lenght needed
min_length = min(length/2,width/2)

#assign a variable to the def. If the radius is less more than the minimum length, print out
#that it is invalid. If not, print out the remaining volume
volume = VolumeRemaining(length,width,height,radius)
print()
if radius > min_length:
    print("The radius is invalid!")
else:
    print("The ramaining volume is",volume)

#Problem #2
#Define the prof_find() function.
def prof_find(fac_names, fac_op_cost, fac_prod_value):
     list_len = len(fac_names) #Find the length of the lists
     min_fac_prof = fac_prod_value[0] - fac_op_cost[0]#Define the variables to store the name and the
     min_fac_name = fac_names[0] #profit of the least profitable facility.
     for i in range(1, list_len):
         cur_fac_prof = fac_prod_value[i] - fac_op_cost[i]
         if min_fac_prof > cur_fac_prof:
             min_fac_prof = cur_fac_prof
             min_fac_name = fac_names[i]
             return[min_fac_name, min_fac_prof]
#Define the main() function.
def main():
    fac_names = ["Facility 1", "Facility 2", "Facility 3"]
    fac_op_cost = [3000, 7500, 1500]
    fac_prod_value = [10000, 12000, 7000]
    name_prof = prof_find(fac_names, fac_op_cost, fac_prod_value)
    print("The name and the profit of the least profitable facility is as follows:")
    print("Name:   ", name_prof[0])
    print("Profit: ", name_prof[1])
main()
#Problem #3
def Person_Info(name,city,state,zip_code,address):
    print("The Person's address is :")
    print(name)
    print(zip_code)
    print(city)
    print(state)
    print(address)
Person_Info("Daniel", "College Station", "Tx", "77840", "301 Church Ave.")
Person_Info("Yamir", "College Station", "Tx", "77840", "Street St.")
#Problem #4*
# =============================================================================
# import csv
# file = open("file.csv", "w") #open the file you wish to use
# with open ("csvfile.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:  #change from csv to to tab-separated 
#         file.write("\t".join(row))
#         file.write("\n")
# =============================================================================
file.close()
#Problem #5
def Problem_5(lists): #define 
    print("Maximum is", max(lists)) #use tools to find min and max
    print("Minimum is", min(lists))
    print("Mean is", sum(lists)/len(lists)) #the mean is simply the sum of values over amount of values
Problem_5([1,2,3])

#Problem #6
def Velocity_Ave(time, distance): #define 
    vel_list = []
    for i in range(1,len(time)):
        vel_list.append((2*distance[i]/time[i])) #append the velocity to the list
    return vel_list
print("Average velocity is:",Velocity_Ave([1,2,3],[4,5,6]))