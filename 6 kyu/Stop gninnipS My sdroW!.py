#Kata name: Stop gninnipS My sdroW!

#Kata link: https://www.codewars.com/kata/5264d2b162488dc400000001

#Kata description: Write a function that takes in a string of one or more words, and returns the same string,
#but with all five or more letter words reversed (Just like the name of this Kata).
#Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


def spin_words(sentence):
    words = sentence.split(" ")      #Make array from the sentence 
    newSentence = ""
    for x in words: 
        if len(x) < 5:                #If less than 5, don't reverse and append to newSentence
            newSentence += x + " "
        elif len(x) >= 5:             #>= 5 , reverse string and append to newSentence
             reverseString = x[::-1]          #Reverse with extended splice
             newSentence += reverseString + " "
             
    return newSentence.strip()    #Need to strip which gets rid of whitespace because I added spaces to the end
