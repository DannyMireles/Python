# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 10b - 2
# Date:         11/04/2019

#Found Panda Online. Import libraries to help
import matplotlib.pyplot as plt

print("This program will export four graphs demonstrating different relationships.")
#read the csv file in
FileID = open("WeatherDataWindows(1).csv", "r")
Header = FileID.readline()

#Create empty lists to use later
Pressure_Ave = []
Temp_Ave = []
Temp_Low = []
Temp_High = []
Date = []
precip = []
Ave_Dew = []

#Append date into the empty lists
for line in FileID:
    list = line.split(",")
    Date.append(list[0])
    Pressure_Ave.append(float(list[11]))
    Temp_Ave.append(float(list[2]))
    Temp_High.append(float(list[1]))
    Temp_Low.append(float(list[3]))
    precip.append(float(list[13]))
    Ave_Dew.append(float(list[5]))

plt.xlabel("Date")
plt.ylabel("Average Temperature and Pressure")
plt.title("Pressure vs. Temperature averages")
plt.plot(Pressure_Ave, label="Pressure")
plt.plot(Temp_Ave,label="Temperature")
plt.legend(loc="upper left")
plt.show()

#Problem #2
#First make a reasonable data set
x=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0]
plt.hist(precip,bins=x,rwidth=0.6,label="Precipitation(in.)")
plt.title("Amount of Precipitation over days")
plt.xlabel("Range of precipitation")
plt.ylabel("Number of Days")
plt.legend(loc="upper right")
plt.show()

#Problem #3
plt.scatter(Ave_Dew,Temp_Ave,color="purple",label="Relationship")
plt.title("Relationships between average temperature and average dew")
plt.xlabel("Average Dew Point", fontsize = 12)
plt.ylabel("Average Temperature", fontsize = 12)
plt.legend(loc="upper left")
plt.show()

#Problem #4
#need to import numpy for this program
import numpy as np
mon = ["Junuary", "Feb", "March","April","May","June","July","August","Sept","Oct","Nov","Dec"]
plt.bar(Temp_Ave,color="purple",label="Temp Ave")
plt.bar(Temp_Low,color="red",label="Temp Low")
plt.bar(Temp_High,color="green",label="Temp High")
plt.title("Temperature averages over a year")
plt.xlabel("Mon", fontsize = 12)
plt.ylabel("Temperatures", fontsize = 12)
plt.legend(loc="upper left")
plt.show()

