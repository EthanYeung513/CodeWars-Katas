#Kata name: Third Angle of a Triangle

#Kata link: https://www.codewars.com/kata/5a023c426975981341000014

#Kata description: You are given two angles (in degrees) of a triangle.
#Write a function to return the 3rd.

def other_angle(a, b):  
    return 180 - (a + b) #Angles add up to 180 in a triangle. 
                         
