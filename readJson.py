import json
import datetime
from datetime import date
import calendar
file = open("days.json")
file = file.read()
data = json.loads(file)
'''a = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]
for i in range(len(a)):
    print(data[a[i]])'''
x = str(datetime.datetime.today().date())
x = x.replace("-"," ",2)
def findDay(x):
	day, month, year = (int(i) for i in x.split(' '))
	dayNumber = calendar.weekday(day, month, year )
	days =["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
						"FRIDAY", "SATURDAY", "SUNDAY"]
	return (days[dayNumber])
#print(findDay(x))
print(data[findDay(x)])
for BREAK in data:
    print(BREAK)
