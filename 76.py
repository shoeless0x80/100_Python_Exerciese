import datetime

day = datetime.date.today().strftime("%A")
month = datetime.date.today().strftime("%B")
day_of_month = datetime.date.today().strftime("%d")
year = datetime.date.today().strftime("%Y")

print("Today is %s, %s %s, %s" % (day, month, day_of_month, year))

'''
from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))
'''
