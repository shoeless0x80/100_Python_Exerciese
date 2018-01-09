f = open("41.txt", "w+")
for i in range(ord('a'), ord('z')+1 ):
    f.write(chr(i)+"\n")
f.close()

"""
import string
with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
"""
