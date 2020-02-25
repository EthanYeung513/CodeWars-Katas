#Kata name: Odd or Even?

#Kata link: https://www.codewars.com/kata/5949481f86420f59480000e7/python

#Kata description: Add elements in array, return even or odd of the sum.



def oddOrEven(arr):
    if sum(arr) % 2 == 0: #Sum is a built in function which adds up all values in an array.                   
       return "even"      #The "%" is the modulo operator that returns the remainder after dividing
    else:                 #Every even number that is % by 2 gives a 0, since all even numbers are in #the 2 times table.
       return "odd"
    
