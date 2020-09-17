# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 9b - 1
# Date:         10/24/2019

#open file in read mode or create it if it doesn't exist 
c = open("Celsius.txt" , "r")
#Now open file in write mode 
f = open("Fahrenheit.txt" , "w")
#read the file contents
x = c.read()
#read file line by line using .split 
for C in c:
    x = float(C)  #Write formula as Python code
    x = x * (9/5) + 32
  #write Fahrenheit conversions into the file. Add a new line after each
    f.write(str(x) + '\n' )

#close the files 
c.close()
f.close()

