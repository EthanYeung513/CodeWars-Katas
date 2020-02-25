#Kata name: Valid Parentheses

#Kata link: https://www.codewars.com/kata/52774a314c2333f0a7000688

#Kata description: Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
#The function should return true if the string is valid, and false if it's invalid.


def valid_parentheses(string):
    myStack = []
    for s in string:
        if s == "(":
            myStack.append(s)
        elif s == ")":
            try:
                myStack.pop() 
            except:    #If error, that means stack is empty with no "(". So return False
                return False 

    if not myStack: #If stack is empty, 
        return True
    else:
        return False
