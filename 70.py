import requests

response = requests.get('http://www.pythonhow.com/data/universe.txt')
print(response.text)
