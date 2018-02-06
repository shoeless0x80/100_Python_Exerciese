#Create a program that aska the user to input values separated by commas and those values will be
#store in a separate line each in a text file

data = input("Enter values: ")
data_b = data.split(",")
with open("95.txt", "a+") as file:
    for i in data_b:
        file.write(i+"\n")
