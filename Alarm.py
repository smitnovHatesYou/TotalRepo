#this is the time file
# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
#Write a Python program to solve the general version of the above problem. 
#Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. 
#Your program should output what the time will be on the clock when the alarm goes off.

import time
current_hour = int(input("What is the current hour (0-23)? "))
alarm_hours = int(input("How many hours from now do you want the alarm to go off? "))
alarm_time = (current_hour + alarm_hours) % 24
print("The alarm will go off at the hour:", alarm_time, "Or ")
if alarm_time < 12:
    print(alarm_time, "am")
elif alarm_time <= 24 >= 48:
    print(alarm_time, + "the next day")
else:
    print(alarm_time - 12, "pm")