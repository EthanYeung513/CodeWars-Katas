#Kata name: Convert boolean values to strings 'Yes' or 'No'.

#Kata link: https://www.codewars.com/kata/53369039d7ab3ac506000467/python

#Kata description: Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    if boolean == True:
       return "Yes"
    elif boolean == False:
       return "No"
    
