#Kata name: Square Every Digit

#Kata link: https://www.codewars.com/kata/546e2562b03326a88e000020/python

#Kata description: Welcome. In this kata, you are asked to square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#Note: The function accepts an integer and returns an integer



def square_digits(num):
    newString = "" 
    num = str(num)  #Turn num into a string so it's iterable
    for x in num:   #Go through every item in string
        newString += str(int(x) ** 2)   #Typecast x into num so you can square, but then after
    return int(newString)               #turn it into a string so you can concatonate to "newString"
