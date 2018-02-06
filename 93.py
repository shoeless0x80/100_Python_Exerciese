import glob

file_list = glob.glob('./93/**/*.py', recursive=True)
print(len(file_list))
