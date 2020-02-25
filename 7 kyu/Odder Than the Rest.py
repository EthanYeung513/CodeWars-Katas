#Kata name: Odder Than the Rest

#Kata link: https://www.codewars.com/kata/5983cba828b2f1fd55000114

#Kata description: Create a method that takes an array/list as an input, and outputs the index at which the sole odd number is located.
#This method should work with arrays with negative numbers. If there are no odd numbers in the array, then the method should output -1.

def odd_one(arr):
    for x in arr:
        if x % 2 != 0:  #Checks if number is odd
           return arr.index(x)  #Returns odd
    return -1  #If program goes here, it found no odd since if it did it would have returned the index.
               #(When returning it stops the function). Therefore, return -1


