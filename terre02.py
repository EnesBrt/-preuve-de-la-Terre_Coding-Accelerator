# Afficheur d’arguments

def display_arguments(arguments):
    words = arguments.split()
    for n in words:
        print(n)


sentence = input("Write a sentence: ")

display_arguments(sentence)
