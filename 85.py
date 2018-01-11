import pycountry

original_file = open('countries-raw.txt', 'r')
lines = original_file.readlines()
lines[:] = [line.rstrip('\n') for line in lines]
for country in lines:
    print(country)
    try:
        pycountry.countries.lookup(country)
        with open('85.txt', 'a+') as new_file:
            new_file.write(country+'\n')
    except:
        pass

original_file.close()
