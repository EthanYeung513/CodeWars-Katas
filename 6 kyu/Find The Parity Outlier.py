#Kata name: Find The Parity Outlier

#Kata link: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python

#Kata description: You are given an array (which will have a length of at least 3, but could be very large) containing integers.
#The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
#Write a method that takes the array as an argument and returns this "outlier" N.



def find_outlier(integers):
    even = 0
    odd = 0
    for x in range(3):   #Check first 3 items, to see if odd is even is the outlier.
       if integers[x] % 2 == 0: 
           even += 1   
       else:
           odd += 1
           
    if even < odd:   #Means there are less evens than odds. So even is the outlier
       for x in integers:  #Find the even number and return it
           if x % 2 == 0: #Checks if even, then return it.
              return x
    elif even > odd:   #Means more evens than odds, therefore odd is outlier
        for x in integers: #Find the odd number and return it
           if x % 2 != 0 :
              return x
         
