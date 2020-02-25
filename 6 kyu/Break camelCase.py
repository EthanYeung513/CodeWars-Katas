#Kata name: Break camelCase
#Kata link: https://www.codewars.com/kata/5208f99aee097e6552000148
#Kata description: Complete the solution so that the function will break up camel casing, using a space between words.


def solution(s):
    wordArray = list(s) #Make string into list
    finalString = "" #What to return 
    for x in wordArray: 
        if x.isupper() == True: 
           finalString += " " + x #If upper, add a space and the char
        else:
           finalString += x 
           
    return finalString
          
