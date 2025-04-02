import RPi.GPIO as gp
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import sys
 
# This code detects radiation counts from a sensor, and writes them to a table
# with: Real Time, Time Relative to to start (0), Radiation Counts

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

def my_callback(cnum):
    print("Callback Ran")
    global count
    count+=1
i=0
gp.add_event_detect(cnum, gp.FALLING,callback=my_callback)
while i < seconds_argv:
    
    Time = time.time()
    if (i % 60 == 0):
        csvwriter.writerow([Time, i, count])
        count=0
    i += 1
    last=i
    time.sleep(1)
csvwriter.writerow([Time, last, count])
print("Ended loop")
file.close()

