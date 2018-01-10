#Write a script that iterates thorugh each of the 26 text files, checks if the letter inside the text
#file is in string "python" and puts the letter in a list if the letter is a character of "python".
import string

python_list = []

for letter in string.ascii_lowercase[0::]:
	with open(letter + ".txt", "r") as file:
		content = file.read()
		print(type(content))
		"""if content is in "python":
			continue
		else:
			python_list.append(file.read())

print(python_list)
"""