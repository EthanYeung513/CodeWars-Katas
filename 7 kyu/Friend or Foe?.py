#Kata name: Friend or Foe?

#Kata link: https://www.codewars.com/kata/55b42574ff091733d900002f/python

#Kata description: Make a program that filters a list of strings and returns a list with only your friends name in it.
#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

def friend(x):
    newList = []
    for y in x:
        if len(y) == 4:     #len gets amount of characters
           newList.append(y)    #If 4, then add it to the list 
    return newList
