import time
import os
import subprocess

hour = input("the hour to sound the alarm:")
int (hour)
minute = input("the hour to sound the alarm:")
second = input("the hour to sound the alarm:")
while True:
    from datetime import datetime
    now = datetime.now()  
    print("\a")
    print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)) 
    os.system("clear")
    if now.hour == hour and now.minute == minute and now.second == second:
        subprocess.call(["afplay","sounds/beep.wav"])