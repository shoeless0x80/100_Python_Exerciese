#import pycountry
import string

original_file = open('countries-raw.txt', 'r')
new_file = open('85.txt', 'w+')
delete_list = ["Top of Page", "\n"]
for letter in range(65, 91):
    delete_list.append(chr(letter))
print(delete_list)
for line in original_file:
    for word in delete_list:
        line = line.replace(word, '')
    new_file.write(line+'\n')
original_file.close()
new_file.close()

'''
#lines = original_file.readlines()
for line in original_file:
    lines = line.split('\n')
lst = ["\n", "Top of Page"]
print(lines)
for country in lines:
    if country not in lst and len(country) > 1:
        with open('85.txt', 'a+') as new_file:
            new_file.write(country+'\n')
original_file.close()
'''
