d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    if word in d:
        return d[word]
    else:
        return "That word doesn't exist!"

word = input("Enter word: ")
print(vocabulary(word))

'''
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter word: ")
print(vocabulary(word))
''' 
