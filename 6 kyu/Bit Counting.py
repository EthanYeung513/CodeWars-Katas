#Kata name: Bit Counting

#Kata link: https://www.codewars.com/kata/526571aae218b8ee490006f4

#Kata description: Write a function that takes an integer as input,
#and returns the number of bits that are equal to one in the binary representation of that number.
#You can guarantee that input is non-negative.


def countBits(n):
    bitCount = 0
    bit =  '{0:08b}'.format(n) #Turn to binary
    for item in bit:    
        if item == "1":     #Loop through every item and increment everytime there's a 1
           bitCount += 1
           
    return bitCount
