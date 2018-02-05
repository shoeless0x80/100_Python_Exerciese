from datetime import datetime

old = input("How old are you?: ")
now = datetime.datetime.now().year
born = (int(now) - int(old))
print("You were born back in %s" % born)

'''
age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("We think you were born back in %s" % year_birth)
'''
