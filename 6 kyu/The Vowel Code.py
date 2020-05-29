#Kata name: The Vowel Code
#Kata link:
#Kata description: 



vowels = {     #Dictionary look up speed is o(1)
    "a": 1,    #When "encoding", use this to get for the value of the vowel 
    "e": 2,    #and add it to the string
    "i": 3,
    "o": 4,
    "u": 5
}

vowels2 = {     
    "1": "a",
    "2": "e",
    "3": "i",
    "4": "o",
    "5": "u"
}


def encode(st):
    newString = ""
    
    for x in st:   #Go through entire string
        if x in vowels:  #If x is in vowels, or in other words, is a vowel
           newString += str(vowels[x])  #Add the value of the vowel
        else:
           newString += x  
    return newString
    
    
def decode(st):
    newString = ""
    print(st)
    for x in st:  #Go through entire string
        try:    #Try catch which will trigger an exception if int function is performed on a letter.
            int(x)   
            newString += str(vowels2[x])  
        except:
          newString += x           
    return newString
