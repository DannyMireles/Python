# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 7b - 3
# Date:         10/10/2019
#start of part A
import statistics
l = input("please enter your list here, with inputs separated by a single space: ")
l1 = [int(x) for x in l.split(" ")]#must be split by a single space or the code will not work
print()
print(statistics.median(l1))
#end of part A
#start of part B
l3 = input("please enter your list here, with inputs separated by a single space: ")
l4 = [int(x) for x in l3.split(" ")]#must be split by a single space or the code will not work
print()
firstnum = l4[0]
secondnum = l4[1]
while firstnum and secondnum in l4:
    while firstnum > secondnum:
        l4.remove(firstnum)
        l4.append(firstnum)
        firstnum = [0]
        secondnum = [1]
    else:
        l4.append(secondnum)
        l4.remove(secondnum)
        firstnum = l4[0]
        secondnum = l4[1]
        print(l4)
        break


