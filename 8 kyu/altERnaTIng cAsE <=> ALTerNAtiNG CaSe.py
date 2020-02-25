#Kata name: altERnaTIng cAsE <=> ALTerNAtiNG CaSe

#Kata link: https://www.codewars.com/kata/56efc695740d30f963000557

#Kata description: Define String.prototype.toAlternatingCase such that
#each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.



def to_alternating_case(string):
    newString = ""
    for x in string:    #Go through every character
        if x.isupper() == True and x.isalpha() == True: #if uppercase , turn to lower  and add to new String
           x = x.lower()
           newString += x
        elif x.islower() == True and x.isalpha() == True:
           x = x.upper()
           newString += x
        else:
           newString += x
    return newString
