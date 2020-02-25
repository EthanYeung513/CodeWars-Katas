#Kata name: Where my anagrams at?

#Kata link: https://www.codewars.com/kata/523a86aa4230ebb5420001e1

#Kata Description: Write a function that will find all the anagrams of a word from a list.
#You will be given two inputs a word and an array with words.
#You should return an array of all the anagrams or an empty array if there are none. 
#What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.

def anagrams(word, words):
    sortedOrig = sorted(word) #Sort because if same letters, it will appear the same when sorted
    anagramArray= []
    for x in words:
        if sorted(x) == sortedOrig: 
           anagramArray.append(x)
    return anagramArray 
