#Kata name: V A P O R C O D E

#Kata link: https://www.codewars.com/kata/5966eeb31b229e44eb00007a

#Kata description: Write a function that converts any sentence into a V A P O R W A V E sentence.
#a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character)
#to create this V A P O R W A V E effect.




def vaporcode(s):
    newstring = s.replace(" ", "")       #Makes string have no space
    newstring = newstring.upper()        #Converts everything to uppercase
    newstring = newstring.replace("", "  ")    #Adds 2 spaces between each character
    newstring = newstring.strip()        #Removes the whitespace before and after the strings
    return newstring
