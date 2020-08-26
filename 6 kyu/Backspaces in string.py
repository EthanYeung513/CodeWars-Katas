#Kata name: Backspaces in string

#Kata link: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

#Kata description: Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#Your task is to process a string with "#" symbols.

#"abc#d##c"      ==>  "ac"
#"abc##d######"  ==>  ""
#"#######"       ==>  ""
#""              ==>  ""


def clean_string(s):
    stack = []   #Make a stack
    for x in s:  #Go through every char in s
        if x == "#" and len(stack) != 0:   #If '#', delete last char added,
            stack.pop()    #Has to check if not empty otherwise there will be an error
        elif x != "#":   #If x is not '#'
            stack.append(x)  #Add to front of stack
    return "".join(stack)    #Makes the stack into a string with no spaces
