#Create a program that generates a password of 6 random alphanumeric characters
#in the range abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?
import string
import random

password = ""
chars = string.printable
for i in range(6):
    ran = random.randint(0, len(chars))
    password = password + chars[ran]

print(password)

'''
import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)
'''
