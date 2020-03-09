#Kata name: Consonant value

#Kata link: https://www.codewars.com/kata/59c633e7dcc4053512000073

#Kata description: Given a lowercase string that has alphabetic characters only and no spaces,
#return the highest value of consonant substrings. Consonants are any letters of the alpahabet except "aeiou". 


def solve(s): 
    Vowels = ["a","e","i","o","u"]
    tempMax = 0       
    greatest = 0
    for x in s:
        if x not in Vowels:
           tempMax += ord(x) - 96
           if tempMax >= greatest:
              greatest = tempMax
        else:        #If it's a vowel, reset tempMax
           tempMax = 0
    return greatest
