#Kata name: The Hashtag Generator

#Kata link: https://www.codewars.com/kata/52449b062fb80683ec000024/python

#Kata description: The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!

#Here's the deal:

#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.



def generate_hashtag(s):
   length = len(s)
   s = s.strip()     #Remove whitespace
   s = s.replace("  "," ")      #Deal with double space
   if length > 140 or length == 0:     #Invalid input
      return False
   newString = "#"      #Adds # first
   AllStrings = s.split(" ")    #Make s into array by space
   for x in AllStrings:        
       newString += x[0].upper()       #Gets first character, adds it to newString and makes it uppercase
       newString += x[1:].lower()      #Get everything except first character
   return newString
   
   
