phrase = input("Write something: ")

list = []
word = ""
pontuation = ["!", "?", ".", ":", ",", ")", "("]

for character in phrase:
    if character in pontuation:
        if word != "":
            list.append(word)
            word = ""
        list.append(character)
    elif character != ' ':
        word += character
    else:
        if word != "":
            list.append(word)
        word = ""

#list.append(word)
print(list)