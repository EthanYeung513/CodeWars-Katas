#Kata name: Summing a number's digits

#kata link: https://www.codewars.com/kata/52f3149496de55aded000410

#Kata description: Write a function named sumDigits which takes a number as input
#and returns the sum of the absolute value of each of the number's decimal digits. For example:
#  sum_digits(10)  # Returns 1
#  sum_digits(99)  # Returns 18
#  sum_digits(-32) # Returns 5


def sum_digits(number):
    total = 0
    stringNum = str(number)          #Typecast to string so you can loop through it
    stringNum = stringNum.replace("-" , "")     #Replace negative sign with nothing, as it is not needed and will give 
    for x in stringNum:                         #an error when trying to turn into int.
        total += int(x)
    return total
