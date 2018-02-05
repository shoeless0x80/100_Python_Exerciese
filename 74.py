import pandas

data_1 = pandas.read_csv("74a.csv")
data_2 = pandas.read_csv("74b.csv")
data_new = pandas.concat([data_1, data_2])
data_new.to_csv("74.txt", index=None)

'''
data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)
'''
