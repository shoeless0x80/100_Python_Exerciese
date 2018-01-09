import string

for i in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
	print(i)