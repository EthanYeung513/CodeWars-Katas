#Kata name: First non-repeating character

#Kata link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python

#Kata description: Write a function named first_non_repeating_letter that takes a string input,
#and returns the first character that is not repeated anywhere in the string.


def first_non_repeating_letter(string):
    newList = [x.lower() for x in string] #Make a list from the string and lowercase everything
    length = len(newList)
    for i in range(length):
        if newList.count(newList[i]) == 1:
            return string[i]     #Need to use string because in list, it's lowercased, and
    return ""                    #original could be uppercase
