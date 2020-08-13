#Kata name: Alternate case

#Kata link: https://www.codewars.com/kata/57a62154cf1fa5b25200031e

#Kata description: Write function alternateCase which switch every letter in string from upper to lower and from lower to upper. E.g: Hello World -> hELLO wORLD


def alternateCase(s):
    newString = ""
    for x in s:
        if x.isupper() == True:  #Is current character uppercase
            newString += x.lower()   #Make string lowercase and append to newString
        else:
            newString += x.upper()
    return newString
            
