#Kata name: Highest Scoring Word

#Kata link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python

#Kata description: Given a string of words, you need to find the highest scoring word.
#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#You need to return the highest scoring word as a string.
#If two words score the same, return the word that appears earliest in the original string.
#All letters will be lowercase and all inputs will be valid.



def high(x):
    newList = x.split(" ")         #Makes string an array 
    length = len(newList)          #So we can loop through 1 word at a time
    listOfScores = []              #Where scores for each word are going to be appended
    
    for x in range(length):        
        sum = 0
        for y in newList[x]:       #Loop through each word
            sum += ord(y) - 96     #Change to unicode value. A = 97 so you need to -96 to get it's position in alphabet
        listOfScores.append(sum)   #Append the word score to a list
 
    indexOfHighest = listOfScores.index(max(listOfScores))        #Get index with max and index function
    theHighest = newList[indexOfHighest]            #Get the highest word with the index above
    return theHighest
     
