#Kata name: Borrower Speak

#Kata link: https://www.codewars.com/kata/57d2ba8095497e484e00002e/python

#Kata description: The young borrowers have begged their parents to stop using caps and punctuation.
#Change the input text 's' to new borrower speak. Help save the next generation!


def borrow(s):
    s = s.lower()       #Makes string lowercas
    s = s.replace(" ","")      #Replaces spaces with nothing
    newString = ""
    for x in s: 
        if x.isalpha():         #If it's in alphabet, put it in newString, so no symbols in new String
           newString += x
    return newString
