# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 7b - 2
# Date:         10/10/2019

import math
print("This program lets a user enter two vectors, A and B, of arbitrary dimension and stores each vector as a Python list. It then calculates the magnitude of the vectors, their sum, their difference, and their dot product.")
#promt the user for the dimensions of the vector
dimension=int(input('Please input the dimension of the vector: '))
vector_A=[]
vector_B=[]
count=1
directions='Please Enter on value at a time of vector when promted'
while dimension>=2 and count<=dimension:

    print('Enter vector A',count)#prompts for the first component of vector A
    vector_1=int(input())
    vector_A.append(vector_1)
    print('Enter vector B', count)#prompts for the first component of vector B
    vector_2 = int(input())
    vector_B.append(vector_2)
    count = count + 1


mag_vecA=math.sqrt(sum(i**2 for i in vector_A))#calculates the magnitude of vector A
mag_vecB=math.sqrt(sum(i**2 for i in vector_B))#calculates the magnitude of vector B
print('\nMagnitude of vector A: ',mag_vecA)#prints the magnitude of vector A
print('Magnitude of vector B: ',mag_vecB)#prints the magnitude of vector B
print()

vec_add=[x+y for x,y in zip(vector_A,vector_B)]#calculates the sum of vector A and B
vec_sub=[x-y for x,y in zip(vector_A,vector_B)]#calculates the difference of vector A and B
print('A + B =',vec_add)#print the sum of vectors
print('A - B =',vec_sub)#print the difference of vectors
print()

dotproduct = sum(i*j for i,j in zip(vector_A,vector_B))#calculates the dot product
print('Dot product is : ' , dotproduct)