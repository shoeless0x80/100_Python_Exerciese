#Create a program that generates a password of 6 random alphanumeric characters
#in the range abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?
import string

foo = []
for a, b, c, d in zip(string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation):
    foo.append(a) 
    foo.append(b)
    foo.append(c)
    foo.append(d)
'''
foo.append(string.ascii_uppercase)
foo.append(string.digits)
foo.append(string.punctuation)
'''
print(foo)
