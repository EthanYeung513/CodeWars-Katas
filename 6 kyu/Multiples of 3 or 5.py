#Kata name: Multiples of 3 or 5

#Kata link: https://www.codewars.com/kata/514b92a657cdc65150000006

#Kata description: Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.


def solution(number):
   numTotal = 0
   for x in range(1,number): #Goes from 1 to below number
       if x % 5 == 0 or x % 3 == 0:   #If mod to 5 or 3 == 0, then its a multiple. Add to numTotal
          numTotal += x
   return numTotal
