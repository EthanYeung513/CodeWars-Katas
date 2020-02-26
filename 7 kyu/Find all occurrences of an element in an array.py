#Kata name: Find all occurrences of an element in an array

#Kata link: https://www.codewars.com/kata/59a9919107157a45220000e1/python

#Kata description: Given an array (a list in Python) of integers and an integer n, 
#find all occurrences of n in the given array and return another array containing all the index positions of n in the given array.
#If n is not in the given array, return an empty array [].
#Assume that n and all values in the given array will always be integers.


def find_all(array, n):
    arrayOfIndexes = []
    length = len(array)
    for x in range(length - 1):
        if array[x] == n:     #If array[x] is same as n, add index, in this case, x, to the list. 
           arrayOfIndexes.append(x)
    return arrayOfIndexes
