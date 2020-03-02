#Kata name: Convert string to camel case

#Kata link: https://www.codewars.com/kata/517abf86da9663f1d2000003/python

#Kata description: Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#The first word within the output should be capitalized only if the original word was capitalized
#(known as Upper Camel Case, also often referred to as Pascal case).

#Examples
#to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"



def to_camel_case(text):
    newString = ""
    text = text.replace("-", "_")     #Input can have "-" or "_" so change all to "_"
    newArray = text.split("_")        #Make array split by "_"
       
    for x in newArray:
       if x != newArray[0]:          #Don't uppercase first word
          newString += x[0].upper()      #Uppercase first letter in word
          newString += x[1:]             #Add every letter except first one using splice
       else:
          newString += x                 #If string is first word, just add it normally
    return newString
