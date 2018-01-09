t = open('words2.txt', 'r+')
tempstr = t.read()
count=0
for i in tempstr:

    if i == ",":
        i.replace(',', ' ')
t.close()
print(count)
