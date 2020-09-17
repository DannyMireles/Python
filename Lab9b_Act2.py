# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 9b - 2
# Date:         10/24/2019
#
#Ask user for file name to save the data
file_name = input("Please input a file name to save the data here: ")
file_path = file_name+".csv"
csv_data=[("Month","Total Interest Accrued","Remaining Loan Amount")]

#Ask user for P,N, and i (as a decimal not percentage)
P = int(input("Please input your loan amount here: $"))
N = int(input("Please input the number of months here : "))
i = float(input("Please input the annual interest rate (as a decimal point) here: "))
J = i/12
M = P*(J/(1-((1+J)**(-N))))

months = N
Ac_Int = 0
Monthly_Interest = 0
Month = 0

#Calculate the accrued interest, final balance, and month
for months in range(0,N):
    print("-")
    Ac_Int += P*J
    print("%.2f" % Ac_Int)
    Monthly_Interest = P*J
    P = P - M + Monthly_Interest
    print("%.2f" % P)
    Month += 1
    print(Month)
    csv_data.append((Month,Ac_Int,P))


    

f = open(file_path, "w")
for x in csv_data:
    line = str(x[0])+","+str(x[1])+","+str(x[2])+"\n"
    f.write(line)
f.close()

