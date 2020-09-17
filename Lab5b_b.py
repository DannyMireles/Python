# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab Lab5b
# Date:         10/03/2019
#

print("This code will retrieve a positive integer from the keyboard and find the sum of all integers from 0 to the number entered, including the number entered, as well as find the product of all integers from 1 to the number entered, including the number entered.")
n = int(input("Please input your positive integer here: "))


#Calculate the sum using a while loop
sum = 0

for x in range(0,n+1):
    sum = sum+x
print()
print("The sum of the numbers entered is:", sum )


#Calculate the product using a for loop
sum = 1

for x in range(1,n+1):
    sum = sum*x
print()
print("The product of the numbers entered is:", sum )


#Calculate the sum using a while loop
sum = 0

while (x >= 0):
    sum += x
    x-=1
print()
print("The sum of the numbers entered is:", sum )

product = 1

#Calculate the product using a while loop
while (n > 0):
    product *= n
    n-=1
print()
print("The product of the numbers entered is:", product)



# =============================================================================
