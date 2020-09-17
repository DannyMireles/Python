# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Mireles
# Section:      102-540
# Assignment:   Lab 7b - 1
# Date:         10/10/2019
#This program repeatedly reads in a word from a user, converts it to Pig Latin, 
#then prints both the original word and the Pig Latin version to the console until the user enters "stop"
#tell what program does
print("This program repeatedly reads in a word from a user, converts it to Pig Latin, then prints both the original word and the Pig Latin version to the console until the user enters stop")
print()
#ask user for word
word = input("Please input you word here!: ")
while (word != "stop"):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") #if the word begins with a vowel
    length = len(word)
    firstlet = word[0]
    
    if firstlet in vowels: #if the words begins with a vowel
        newword = word + "yay"
        print(newword)
    else:
        newword = word[1:] + firstlet + "ay"
        print(newword)
    word = input("Please input you word here!: ") #keep asking for other word unless stop is inputted