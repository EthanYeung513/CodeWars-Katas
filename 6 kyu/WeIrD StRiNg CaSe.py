#Kata name: WeIrD StRiNg CaSe

#Kata link: https://www.codewars.com/kata/52b757663a95b11b3d00062d/python

#Kata description: Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
#and returns the same string with all even indexed characters in each word upper cased,
#and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, 
#therefore that character should be upper cased.

#The passed in string will only consist of alphabetical characters and spaces(' ').
#Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').



def to_weird_case(string):
    newString = ""    
    change = 0      
    
    for x in string:
        if change % 2 == 0 and x != " " :   #Even, and not a space make it uppercase
           newString += x.upper()
           change += 1
        elif change % 2 != 0 and x != " ":  #Odd, and not a space, make it  lowercase
           newString += x.lower()
           change += 1
        else:
           newString += " "      #This means theres a new word
           change = 0            #"reset" it so first letter in word is uppercased. (0 % 2 == 0)
    return newString
         
