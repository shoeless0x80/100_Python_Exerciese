
with open("countries-by-area.txt", "r") as file:
    content = file.read()
    print(content.split(','))
