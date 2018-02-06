#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

while True:
    data = input("Write a value: ")
    if data == "CLOSE":
        break
    else:
        with open("96.txt", "a+") as file:
            file.write(data+"\n")

'''
file = open("user_data.txt", 'a+')

while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
'''
