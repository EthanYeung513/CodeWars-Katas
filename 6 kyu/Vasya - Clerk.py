#Kata name: Vasya - Clerk

#Kata link: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

#Kata description: The new "Avengers" movie has just been released!
#There are a lot of people at the cinema box office standing in a huge line. 
#Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
#Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
#Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
#Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.




#Note that, I don't think an integer for "change" will work for because for example, 25+25+50 = 100,
#but you can't split that 50 into a 25, even if you have more "change" than neccesary.

def tickets(people):
    twentyFives = 0         #These two variables keep track of the notes we have
    fifties = 0             #Not neccesarry to have 100's as you wont need to give one back as change
    for x in people:        #Loop through array
        if x == 25:         #If 25, don't need to give change, but take a twentyFive
           twentyFives += 1
        elif x == 50:       #If 50, need to give back 1 "25" as price is 25.
           if twentyFives >= 1:       #Check if enough change.
              twentyFives -= 1   
              fifties += 1    
           else:             #Has no twentyFives, therefore can't give change
               return "NO"
        elif x == 100:
           if twentyFives >=1 and fifties >= 1 :    #You could give (1 "25"  and 1 "50") or (3 "25") for change for the 100's. 
              twentyFives -= 1
              fifties -= 1
           elif twentyFives >= 3:
               twentyFives -= 3
           else:
               return "NO"
    return "YES"  #If goes through iteration without returning no, return yes.
              
