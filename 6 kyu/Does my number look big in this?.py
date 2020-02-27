#Kata name: Does my number look big in this?

#Kata link: https://www.codewars.com/kata/5287e858c6b5a9678200083c

#Kata description: A Narcissistic Number is a number which is the sum of its own digits,
#each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
#For example, take 153 (3 digits):
#    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153     #(This is narcissistic because the sum is equal to the original number)



def narcissistic( value ):
    total = 0
    value = str(value)       #Typecast to string so you can iterate and get the length of value
    length = len(value)      #Used for the exponent
    for x in value:
        total += int(x)**length     #Add each digit^length to total
    if total != int(value):         #If total doesnt == original, return False
       return False
    else:
        return True
