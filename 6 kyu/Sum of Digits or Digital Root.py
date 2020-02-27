#Kata name: Sum of Digits / Digital Root

#Kata link: https://www.codewars.com/kata/541c8630095125aba6000c00

#Kata description: A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
#This is only applicable to the natural numbers.

#Here's how it works:
#digital_root(16)
#=> 1 + 6
#=> 7

#digital_root(942)
#=> 9 + 4 + 2
#=> 15 ...
#=> 1 + 5
#=> 6



def digital_root(n):
    total = 0
    n = str(n)
    while len(n) != 1:    #Loop until n is only 1 digit
         temp = 0        
         for x in n:
             temp += int(x)     #Add all digits in n to a temp variable
         n = str(temp)          #Typecast to string so len is usable 
    return int(n)               #When len == 1, return it
