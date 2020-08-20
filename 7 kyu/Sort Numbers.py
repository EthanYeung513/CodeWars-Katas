#Kata name: Sort Numbers

#Kata link: https://www.codewars.com/kata/5174a4c0f2769dd8b1000003

#Kata description: Finish the solution so that it sorts the passed in array of numbers.
#If the function passes in an empty array or null/nil value then it should return an empty array.

#For example:

#solution([1,2,3,10,5]) # should return [1,2,3,5,10]
#solution(None) # should return []




def solution(nums):
    try:      #Makes it so if there's an error, it goes to the except 
        if len(nums) != 0 :   #If not empty, return sorted
            return sorted(nums)
        else:    
            return []
    except:    
        return []
