phrase = input("Write something: ")

list = []
word = ""
pontuation = ["!", "?", ".", ":", ",", ")", "("]

for character in phrase:
    if character in pontuation:
        list.append(character)
    elif character != ' ':
        word += character
    else:
        list.append(word)
        word = ""

list.append(word)
print(list)