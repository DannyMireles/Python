# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 4b
# Date:         09/19/2019
#

days = int(input("Please input the number of days since prodction began here: ")) #days

print()

if days >= 0 and days <= 10:
    print("The widgets produced after",days,"days is: ", days)
    
elif days >= 11 and days <= 60:
    print("The widgets produced after",days,"days is: ", ((days-10)*40 + 100))

elif(60 < days <= 100):
    print(100 + 2000 + 780 - (99-days)*(100-days)/2 )
    
else:
    print(100 + 2000 + 780)
