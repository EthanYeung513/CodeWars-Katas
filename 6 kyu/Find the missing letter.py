#Kata name: Find the missing letter

#Kata link: https://www.codewars.com/kata/5839edaa6754d6fec10000a2/python

#Kata description: Find the missing letter
#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
#You will always get an valid array. And it will be always exactly one letter be missing.
#The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example: ["a","b","c","d","f"] -> "e"
#["O","Q","R","S"] -> "P"


def find_missing_letter(chars):
    alphaCurrent = ord(chars[0])    #Get starting letter ord value
    firstLetter = chars[0]         
    for x in chars:
      if x != firstLetter:         #Don't compare first letter 
         alphaCurrent += 1         #Add 1 to alphaCurrent, which is like the alphabet going up
         temp = chr(alphaCurrent)     #Make a character out of alphaCurrent
         if temp != x:             #If x doesnt = temp, they it has skipped a character in alphabet
            return temp
