import string

with open("44.txt", "w") as file:
	for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
		
		file.write(letter1 + letter2 + letter3 + "\n")
		print("letter1 " + letter1)
		print("letter2 " + letter2)
		print("letter3 " + letter3)
