# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 4b
# Date:         09/19/2019
#
#This program prompts the user to input three numbers and outputs the largest of the three numbers.
number_1 = input("Please input your first number here: ")
number_2 = input("Please input your second number here: ")
number_3 = input("Please input your third number here: ")

if number_1 > number_2 and number_1 > number_3:
    print(number_1)

elif number_2 > number_1 and number_2 > number_3:
    print(number_2)

elif number_3 > number_1 and number_3 > number_2:
    print(number_3)

