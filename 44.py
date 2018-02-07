import string

for i in (string.ascii_lowercase):
	a = string.ascii_lowercase[0::3]
	b = string.ascii_lowercase[1::3]
	c = string.ascii_lowercase[2::3]
	print(a+b+c)

'''
for letter1 in (string.ascii_lowercase[0::3]):
	print(letter1)
	for letter2 in (string.ascii_lowercase[1::3]):
		print(letter2)
		for letter3 in (string.ascii_lowercase[2::3]):
			print(letter3)

with open("44.txt", "w") as file:
	for letter1, letter2 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3]):
		for letter3 in (string.ascii_lowercase[2::3]):
			file.write(letter1 + letter2 + letter3 + "\n")
			print("letter1 " + letter1)
			print("letter2 " + letter2)
			print("letter3 " + letter3)
'''
