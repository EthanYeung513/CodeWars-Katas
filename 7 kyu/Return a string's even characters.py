#Kata name: Return a string's even characters.

#Kata link: https://www.codewars.com/kata/566044325f8fddc1c000002c

#Kata description: Write a function that returns a sequence (index begins with 1) of all the even characters from a string.
If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".



def even_chars(st): 
    newList= [] #Make a list
    number = 1  #Will increment to check if even string
    if len(st) < 2 or len(st) > 100:  
        return "invalid string"
    for x in st:  #Go through every charactter
        if number % 2 == 0:   #If number is even
            newList.append(x)   #Add current character to list
        number += 1   #Increment list
    return newList
