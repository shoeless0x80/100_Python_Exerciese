with open('urls.txt', 'r') as f:
    for i in f:
        i = i.replace("s", "", 1)
        print(i[:6] + "/" + i[6:])

'''
with open("urls.txt", "r") as file:
    line = file.readlines()

print(lines)

with open("urls_corrected.txt", "w") as file:
    for line in lines:
        line_remove_s = line.replace("s", "", 1)
        line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[6:]
        file.write(line_remove_s_add_slash)
'''
