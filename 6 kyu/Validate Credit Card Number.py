#Kata name: Validate Credit Card Number

#Kata link: https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2

#Kata description: In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.
#Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.
#Double every other digit, scanning from right to left, starting from the second digit (from the right).
#Another way to think about it is: if there are an even number of digits, double every other digit starting with the first;
#if there are an odd number of digits, double every other digit starting with the second:
#f a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 9 from it)
#Sum all of the final digits:
#Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.





def validate(n):
   newList = []
   n = str(n)          #Typecast to string so you can loop  through it
   length = len(n)     #Get the length
   double = True
   if length % 2 == 0:    #If even length, double the odd positions in n
      double = True
   else: 
      double = False      #If odd length, double the even positions in n
   for x in n: 
      x = int(x)          #Typecast to int so mathmaticall operations don't cause an error
      if double == True:
         temp = x * 2
         if temp > 9:        #If more than 9, take away by its original value
            temp = temp - x
            newList.append(temp)
            double = False     #Change boolean value so it alternates
         else: 
            newList.append(temp)
            double = False
      else:
         newList.append(x)
         double = True
   Sum = sum(newList)     #Adds all values in list
   if Sum % 10 == 0:     
      return True
   else:
      return False
    
