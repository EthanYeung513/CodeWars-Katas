#Kata name: Simple Pig Latin

#Kata link: https://www.codewars.com/kata/520b9d2ad5c005041100000f


#Kata description:Move the first letter of each word to the end of it, then add "ay" to the end of the word.
#Leave punctuation marks untouched.
#Examples:
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !



def pig_it(text):
    newArray = text.split(" ")       #Make text into array
    newString = ""                     
    for x in newArray:               
       if x.isalpha() == True:       #Says leave puncuation untouched, so check if it's in alphabet.
           temp = x[1:]              #Splice which = temp to everything in the string EXCEPT for the first character
           temp += x[0] + "ay"       #Append the first character and "ay" to the end of the word
           newString += temp + " "   #Add temp and a space to newString
       else:
           newString += x            #Happens when it's not in alphabet
    return newString.strip()         #Remove whitespace
