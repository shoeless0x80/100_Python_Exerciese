#write a script that extracts letters from 26 text files and put the letters in a list.
import string

letters_list = []

for letter in string.ascii_lowercase[0::]:
	with open(letter + ".txt", "r") as file:
		letters_list.append(file.read())
print(letters_list)


"""
import glob

letters = []
file_list = glob.glob("letters/*.txt")

for filename in file_list:
	with open(filename, "r") as file:
		letters.append(file.read().strip("\n"))

print(letters)
"""