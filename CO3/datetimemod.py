import datetime

t=datetime.time(22,56,44,17) #hour mint sec microsec
print(t)

print("Hour is ",t.hour)
print("Minute is ",t.minute)
print("Second is ",t.second)
print("Micro Second is",t.microsecond)

d=datetime.date.today()
print(d)

print("Year is ",d.year)
print("Month is ",d.month)

d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=2) #timedelta class
print(td)
d2=d1+td #adding 2 days
print(d2)

dt=datetime.datetime.combine(d,t)
print(dt)
