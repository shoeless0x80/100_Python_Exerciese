with open('words2.txt', 'r') as file:
    content = file.read()
    content = content.replace(',', ' ')
    content = content.split(' ')
    print(len(content))

'''
def count_words(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(",", " ")
        string_list = string.split(" ")
        return len(string_list)

print(count_words("words2.txt"))
'''
