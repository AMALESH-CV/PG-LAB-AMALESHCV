import time

print("Current Time in Sec",time.time())

print("Current Time is ",time.ctime()) #printing the current time

print("Time after 30 sec",time.ctime(time.time()+30)) #time after 30 sec

t=time.localtime()
print("Current Time",t)
print("Current Year",t.tm_year)
print("Current Month",t.tm_mon)
print("Current Day",t.tm_mday)
print("Current Hour",t.tm_hour)
print("Current Minute",t.tm_min)
#print("Current Week",t.tm_week) 