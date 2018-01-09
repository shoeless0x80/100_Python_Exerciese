def count_words(file):
    data = open(file, "r")
    return(len(data.read().split()))

print(count_words("words1.txt"))
