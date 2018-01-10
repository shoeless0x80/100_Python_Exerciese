import string

for letter in string.ascii_lowercase[0::]:
	with open((letter+".txt"), "w") as file:
		file.write(letter)