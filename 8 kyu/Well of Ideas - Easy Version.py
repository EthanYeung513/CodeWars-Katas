#Kata name: Well of Ideas - Easy Version.py

#Kata link: https://www.codewars.com/kata/563b662a59afc2b5120000c6/python

#Kata description: In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
#If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'.
#If there are no good ideas, as is often the case, return 'Fail!'.



def well(x):
    counter = 0
    for i in x:
        if i == "good":
          counter += 1
        
  
    if counter == 0:
      return "Fail!"
    elif counter == 1 or counter == 2:
      return "Publish!"
    else:
        return "I smell a series!"
