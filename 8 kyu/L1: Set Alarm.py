#Kata name: L1: Set Alarm

#Kata link: https://www.codewars.com/kata/568dcc3c7f12767a62000038/python

#Kata description: setAlarm(true, true) -> false setAlarm(false, true) -> false setAlarm(false, false) -> false 
#setAlarm(true, false) -> true



def set_alarm(employed,vacation):
    if employed == True and vacation == False: #Only condition when returning true,
        return True
    else:                                      #So everything else returns False
        return False
