
checklist = ["Portugal", "Germany", "Spain"]
mergedList= []

with open("countries-missing.txt", "r") as ifile:
    countries = [line.strip() for line in ifile]
    mergedList = checklist + countries
    mergedList.sort()

with open("87.txt", "w+") as newFile:
    for country in mergedList:
        newFile.write("%s\n" % country)

'''
checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for in in checklist]

with open("countries-missing.txt", "r") as file:
    content = file.readlines()

updated_list = sorted(checklist + content)

with open("countried_missing_fixed.txt", "w") as file:
    for i in updated_list:
        file.write(i)
'''
