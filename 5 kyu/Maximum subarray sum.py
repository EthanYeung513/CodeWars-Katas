#Kata name: Maximum subarray sum

#Kata link: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

#Kata description: The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence
#in an array or list of integers:

#maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]



def maxSequence(arr):
    sum,max = 0,0
    for x in arr:
        sum += x       #Adding to sum as you go along arr
        if sum < 0:    #If goes negative, reset sum to 0
            sum = 0        
        if sum > max:    #Change max to highest number currently from variable "sum"
            max = sum
    return max
