#Kata name: Encrypt this!

#Kata link: https://www.codewars.com/kata/5848565e273af816fb000449

#Kata description: 

#Your message is a string containing space separated words.
#You need to encrypt each word in the message using the following rules:
#The first letter needs to be converted to its ASCII code.
#The second letter needs to be switched with the last letter
#Keepin' it simple: There are no special characters in input.

#encrypt_this("Hello") == "72olle"
#encrypt_this("good") == "103doo"
#encrypt_this("hello world") == "104olle 119drlo"




def encrypt_this(text):
    textArr = text.split(" ")   #Make string into array
    newString = ""    #What is to be returned
    lngText = len(textArr)   #Count of how many words
    for x in range(lngText):  #Go through array of words
        lngWord = len(textArr[x])  #Length of the individual word    
        if x != 0 and x != lngText:   #Add a space between letters if not the first or last word
            newString += " "
        for s in range(lngWord):      #Go through every letter in one word
           crntWord = textArr[x]  #Saves current word
           crntChr = crntWord[s]      #Saves current character
           if s > 1 and s != lngWord - 1:  #Means we're not at the first two nor the last letter
                newString += crntChr   #Add the letter normally
           elif s == 0:   #Means we're at the first letter
             newString += str(ord(crntChr))  #Append the ascii value
           elif s == 1:   #Means we're at the second letter
              newString += crntWord[-1]    #Makes second letter the last letter   
           elif s == lngWord - 1:   #Means we're at the end of the word
            newString += crntWord[1]   #Put the last letter as the original second letter
                   
    return newString      
                
