# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab Lab5c
# Date:         10/03/2019
#
from math import*
print("This program is to state what numbers between 2 and 100 are prime and print out the number of prime numbers between 2 and 100.")

print()

c = 0

#checking for numbers in the range
for num in range(2,100):
    p = 0 #sets the counter to 0
    for y in range(1,num): #checks to see that its in the range
        if (num % y == 0):
            p += 1
            
    if (p == 1):
        print(num,"is a prime number") #prints out the prime numbers
        c += 1
    else:
        print(num, "is not a prime number") #prints out th numbers which are not prime
print()
print("There are",c,"prime numbers between 2 and 100")

  
