a = [1,2,3]
b = (4,5,6)

zipped = zip(a, b)
for i in zipped:
    print(i[0]+i[1])

"""
for i, j in zip(a, b):
    print(i + j)
"""
