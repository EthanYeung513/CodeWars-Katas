#Kata name: Reverse every other word in the string

#Kata link: https://www.codewars.com/kata/58d76854024c72c3e20000de/python

#Kata description: Reverse every other word in a given string, then return the string.
#Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word.
#Punctuation marks should be treated as if they are apart of the word in this kata.




def reverse_alternate(string):
  newList = string.split()      #String into list
  newString = ""
  counter = 1                   #To alternate
  for x in newList:
      if counter % 2 == 0:           #For example, (1 % 2 != 2), (2 % 2 == 0) , (3 % 2 != 0) , (4 % 2 == 0) and so on. 
         newString += x[::-1] + " "          #Extended slice to reverse string, and add a space 
      else:
         newString += x + " "
      counter += 1    #Increment counter to alternate
  newString = newString.strip()      #Remove whitespace before and after string
  return newString     
