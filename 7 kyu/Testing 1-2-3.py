#Kata name: Testing 1-2-3

#Kata link: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/python

#Kata description: Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
#Write a function which takes a list of strings and returns each line prepended by the correct number.
#The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]


def number(lines):
   newArray = []    
   length = len(lines)      #Used for the index and to append to the array
   for x in range(length):     
       newArray.append(str(x + 1) + ": " + str(lines[x]))   #Need to +1 to x as range starts from 0 
   return newArray
