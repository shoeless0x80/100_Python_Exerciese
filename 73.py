#Mutiply the values of the text file in the URL by two and export the output to a new file
import requests

response = requests.get('http://www.pythonhow.com/data/sampledata.txt')
text = response.text
with open("73.txt", "w") as file:
    for i in text:
        if i.isnumeric() == True:
            file.write(str(int(i)*2))
        else:
            file.write(i)

'''
import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)
'''
