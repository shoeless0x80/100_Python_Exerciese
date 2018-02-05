import pandas

data = pandas.read_csv('countries-by-area.txt')
dens = []
for index, row in data.iterrows():
    dens.append(row['population_2013']/row['area_sqkm'])
data['density'] = dens
data_sorted = data.sort_values(by='density', ascending=False)
print(data_sorted['country'][:5])

'''
data = pandas.read_csv("countries-by-area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"])
'''
