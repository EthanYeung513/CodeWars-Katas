#Kata name: Beginner - Lost Without a Map

#Kata link: https://www.codewars.com/kata/57f781872e3d8ca2a000007e

#Kata description: Given an array of integers, return a new array with each value doubled.

def maps(a):
    newArray = []
    for x in a:      #Go through the list
        num = x * 2      #For every value, times it by 2 and then add it to the list
        newArray.append(num)
    return newArray
