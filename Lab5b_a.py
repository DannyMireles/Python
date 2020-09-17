# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab Lab5a
# Date:         10/03/2019
#

#This program  takes in a positive integer from a user, and computes the Collatz
#sequence, printing out all the numbers in the sequence, followed by a line stating how many
#iterations it took to reach the value 1.

print("This program takes in a positive integer from a user and computes the Collatz sequence, printing out all the numbers in the sequence, followed by a line stating how many iterations it took to reach the value 1.")
x = int(input("Please input your positive integer here: "))

print()

num_guess = 1
while x>0:
    if x % 2 == 0:
        x = x/2
        num_guess += 1
    elif x>1:
        x = 3*x + 1
        num_guess += 1
    else:
        break
    print (x)
print()
print("The sequence took",num_guess,"iterations")

