""" 
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, 
the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
"""

def alarm_clock(day, vacation):
  Sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6
  
  if vacation and (day >= Mon and day <= Fri):
    return "10:00"
  if vacation and (day == Sun or day == Sat):
    return "off"
  if not vacation and (day >= Mon and day <= Fri):
    return "7:00"
  if not vacation and (day == Sun or day == Sat):
    return "10:00"
