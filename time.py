#!/usr/bin/python3
import time
import calendar

localtime = time.localtime(time.time())
print ("Local current time :", localtime)
localatime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localatime)

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)
