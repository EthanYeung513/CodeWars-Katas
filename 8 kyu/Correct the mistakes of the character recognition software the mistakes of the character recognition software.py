#Kata name: Correct the mistakes of the character recognition software

#Kata link: https://www.codewars.com/kata/577bd026df78c19bca0002c0

#Kata description: #Fix the errors
#S is misinterpreted as 5
#O is misinterpreted as 0
#I is misinterpreted as 1


def correct(string):
    newString = string.replace("5","S")
    newString = newString.replace("0","O")
    newString = newString.replace("1","I")
    return newString
