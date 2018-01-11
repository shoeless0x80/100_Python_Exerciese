import datetime
from dateutil.relativedelta import relativedelta
'''
old = input("How old are you?: ")
now = datetime.datetime.now()
born = (int(now.year) - old)
print("You were born back in %s" % born)
'''
blah = datetime.datetime.now() - relativedelta(years=5)
print(blah)
