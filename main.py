
phrase = input("Write something: ")

list = []
word = ""
for character in phrase:
    if character != ' ':
        word += character
    else:
        list.append(word)
        word = ""

list.append(word)
print(list)