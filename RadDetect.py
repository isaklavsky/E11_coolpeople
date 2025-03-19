import RPi.GPIO as gp
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys
cnum=6
# Placeholder channel number

gp.setmode(gp.BCM)
gp.setup(6, gp.IN, pull_up_down=gp.PUD_DOWN)
file = open('RadData.csv','w',newline = None)
csvwriter = csv.writer(file,delimiter=',')
csvwriter.writerow(["Real Time","Seconds","Count"])
print("Time Set:" , sys.argv)
seconds_argv = int(sys.argv[1])
global count
count=0

def my_callback():
    print("Callback Ran")
    global count
    count+=1
i=0
gp.add_event_detect(cnum, gp.FALLING,callback=my_callback)
while i < seconds_agrv:
    
    Time = time.time()
    if (i % 60 == 0):
        csvwriter.writerow([i, count])
        count=0
    if i ==  seconds_argv:
        csvwriter.writerow([Time, i, count])
    i += 1
    time.sleep(1)
print("Ended loop")
file.close()

