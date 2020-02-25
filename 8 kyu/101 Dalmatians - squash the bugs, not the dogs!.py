#Kata name: 101 Dalmatians - squash the bugs, not the dogs!

#Kata link: https://www.codewars.com/kata/56f6919a6b88de18ff000b36

#Kata description: Your friend has been out shopping for puppies (what a time to be alive!)... 
#He arrives back with multiple dogs, and you simply do not know how to respond!
#By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.


def how_many_dalmatians(n):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  if n <= 10:
     respond = dogs[0]
  elif n <= 50 :
     respond = dogs[1]
  elif n == 101:
     respond = dogs[3]
  else:
    respond = dogs[2]
  return respond
