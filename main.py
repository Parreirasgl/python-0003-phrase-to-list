# Program to transform words from phrases into a list.
# Programa para transformar palavras de frases em uma lista.

phrase = input("Write something: ")

list = []
word = ""
punctuation = ["!", "?", ".", ":", ",", ")", "("]

# Loop through the characters in the phrase.
# Fazer um loop pelos caracteres da frase.
for character in phrase:

# If the character is a punctuation, check if there is already a word,...
# ...since there is a punctuation, there is usually already a word.
# If there is a word, add it to the list, and delete the word.
# Whether or not there is a word, add punctuation to the list.
# Caso o caractere seja uma pontuação, verificar se já há uma palavra,...
# ...pois havendo uma pontuação geralmente já há uma palavra.
# Caso haja uma palavra, adicioná-la a lista, e apagar a palavra.
# Havendo ou não havendo uma palavra, adicionar a pontuação à lista.
    if character in punctuation:
        if word != "":
            list.append(word)
            word = ""
        list.append(character)

# If the character is not a space, that is, if it is an ordinary character...
# ...add the character to the variable word.
# Caso o caractere não seja espaço, ou seja, caso seja um caractere comum...
# ...adicionar o caractere à variável palavra.
    elif character != ' ':
        word += character

# When a space appears, check for a word.
# If a word does not exist (as occurs between sentences), do nothing.
# If it exists, add the word to the list.
# Quando surgir um espaço, verificar se existe uma palavra.
# Se não existir (como ocorre entre frases), não fazer nada.
# Se existir, adicionar a palavra a lista.
    else:
        if word != "":
            list.append(word)
            word = ""

print(list)