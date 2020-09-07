#Kata name: Rot13

#Kata link: https://www.codewars.com/kata/530e15517bc88ac656000716

#Kata description: ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
#ROT13 is an example of the Caesar cipher.
#Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string,
#they should be returned as they are. 
#Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#Please note that using encode is considered cheating.




def rot13(message):
    result = ""    #Encrypted string
    for x in message:   #Go through every character in message
        if x.isalpha():   #If current char in alphabet
            if x.isupper():     #If its uppercase
                tempOrd = ord(x) + 13   
                if tempOrd > ord("Z"):   #If overflows
                    tempOrd -= 26   #26 because 26 chars in alphabet
                    result += chr(tempOrd)  #Append to result
                else:
                    result += chr(tempOrd)
            elif x.islower():
                tempOrd = ord(x) + 13
                if tempOrd > ord("z"):  #If overflows
                    tempOrd -= 26
                    result += chr(tempOrd)
                else:
                    result += chr(tempOrd)
        else:
            result += x
    return result 
