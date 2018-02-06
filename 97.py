#Create a proram that asks the user to submit text repeatedly
#The program saves the changes when the user submits SAVE, but doesn't close
#The program saves the changes and closes when the user submits CLOSE

line_lst = []

while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        file = open("97.txt", 'a+')
        for i in line_lst:
            file.write(i + "\n")
        file.close()
        break
    elif line == "SAVE":
        file = open("97.txt", 'a+')
        for i in line_lst:
            file.write(i + "\n")
        line_lst = []
        file.close()
    else:
        line_lst.append(line)
