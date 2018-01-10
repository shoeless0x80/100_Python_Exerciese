#Write a script that iterates thorugh each of the 26 text files, checks if the letter inside the text
#file is in string "python" and puts the letter in a list if the letter is a character of "python".
import string

python_list = []

for letter in string.ascii_lowercase[0::]:
	with open(letter + ".txt", "r") as file:
		content = file.read()
		print(content)
		if content in "python":
			python_list.append(content)

print(python_list)

"""
import glob

letters = []
file_list = glob.iglob("letters/*.txt")
check = "python"

for filename in file_list:
	with open(filename, "r") as file:
		letter = file.read().strip("\n")
		if letter in check:
			letters.append(letter)

print(letters)
"""
