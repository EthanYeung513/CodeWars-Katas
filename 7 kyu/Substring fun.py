#Kata name: Substring fun

#Kata link: https://www.codewars.com/kata/565b112d09c1adfdd500019c/python

#Kata description: You must concatenate the nth letter from each word to construct a new word which should be returned as a string, 
#where n is the position of the word in the list.
#For example:
#["yoda", "best", "has"]  -->  "yes"
#   ^        ^        ^
#  n=0     n=1     n=2


def nth_char(words):
   newString = ""
   length = len(words) 
   counter = 0         #Counter is used to get the letter of the string we want
   for x in range(length):
      temp = words[x]        #Gets the word into a tempoary variable
      newString += temp[counter]    #Gets a letter, with the counter variable, for example, in "test", temp[0] would give "t"
      counter += 1           #Increment counter
   return newString
    
