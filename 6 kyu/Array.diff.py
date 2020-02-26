#Kata name: Array.diff

#Kata link: https://www.codewars.com/kata/523f5d21c841566fde000009/python

#Kata description: Your goal in this kata is to implement a difference function, 
#which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b.
#If a value is present in b, all of its occurrences must be removed from the other:


def array_diff(a, b):
    newList = []
    for x in a:  
        if x in b:   #Checks if x is in a, if yes, dont add it to newList
           pass
        else:
           newList.append(x)  #It's not in b, therefore add to newList
    return newList
