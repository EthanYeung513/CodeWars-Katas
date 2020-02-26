#Kata name: Counting Duplicates

#Kata link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python

#Kata description: Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
#that occur more than once in the input string.
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.



def duplicate_count(text):
    duplicates = 0         #Integers to count duplicates
    text = text.lower()    #Since it's case sensitive, make all lower case
    for x in set(text):    #Set is like a list but only unique values, so no duplicates in set
        if text.count(x) > 1:    #Go through set, and count amount of times it appears in the "original" text
            duplicates += 1      #If more than 1, plus 1 to duplicates
    return duplicates
