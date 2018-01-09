d = {"a": 1, "b": 2, "c": 3}
'''
total = 0
for key, value in d.items():
    total+= value
print(total)
'''
print(sum(d.values()))
