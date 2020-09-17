# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Daniel Mireles
#               Jordan Nguyen
#               Tan Nguyen
#               Fern Moreno
# Section:      540
# Assignment:   4 - 3
# Date:         19 September 2019

#Part 1: prompt user to input either true or false
Bool1 = input("Please enter first value (True or False): ")
if Bool1 == "True" or Bool1 == "t" or Bool1 == "T":
    Bool1 = True
elif Bool1 == "False" or Bool1 == "f" or Bool1 == "F":
    Bool1 = False
Bool2 = input("Please enter second value (True or False): ")
if Bool2 == "True" or Bool2 == "t" or Bool2 == "T":
    Bool2 = True
elif Bool2 == "False" or Bool2 == "f" or Bool2 == "F":
    Bool2 = False
Bool3 = input("Please enter third value (True or False): ")
if Bool3 == "True" or Bool3 == "t" or Bool3 == "T":
    Bool3 = True
elif Bool3 == "False" or Bool3 == "f" or Bool3 == "F":
    Bool3 = False

#Part2: Evaluate Booleans

print()
print(Bool1 and Bool2 and Bool3)
print()
print(Bool1 or Bool2 or Bool3)

#Part3 (1): Writing Boolean expressions

Bool4 = True
Bool5 = True

if (Bool4 == True and Bool5 == True):
    print("False")
elif (Bool4 == True and Bool5 == False):
    print("True")
elif (Bool4 == False and Bool5 == True):
    print("True")
elif (Bool4 == False and Bool5 == False):
    print("False")

#Part3: 2: 1 and 3 Trues make a True, all else makes a False

boola = True
boolb = False
boolc = True

t3 = boola and boolb and boolc

c = not boolc
aCb = boola or boolb or c
t1c = not aCb

a = not boola
Acb = boolc or boolb or a
t1a = not Acb

b = not boolb
acB = boolc or boola or b
t1b = not acB

t1 = t1a or t1b or t1c

print(t3 or t1)