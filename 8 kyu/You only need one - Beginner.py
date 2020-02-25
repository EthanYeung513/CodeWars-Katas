#Kata name: You only need one - Beginner

#Kata link: https://www.codewars.com/kata/57cc975ed542d3148f00015b

#Kata description: You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
#Array can contain numbers or strings. X can be either.
#Return true if the array contains the value, false if not.

def check(seq, elem):
    if elem in seq: #Checks if "elem" is in "seq", which can return True or False
       return True
    else:
       return False
