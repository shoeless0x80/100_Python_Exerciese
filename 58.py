import json

entry = {'firstName': 'Albert', 'lastName': 'Bert'}

with open('company1.json') as f:
    data = json.load(f)

data.update(entry)

with open('test.json', 'w') as f:
    json.dump(data, f)
