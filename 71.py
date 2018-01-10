import requests

response = requests.get('http://www.pythonhow.com/data/universe.txt')
text = response.text
count = 0
for i in text:
    if i == 'a':
        count += 1
print(count)

'''
import requests

response = requests.get('http://www.pythonhow.com/data/universe.txt')
text = response.text
count_a = text.count("a")
print(count_a)
'''
