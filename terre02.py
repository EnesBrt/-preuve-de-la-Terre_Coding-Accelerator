# Afficheur d’arguments

def display_arguments():
    sentence = input("Write a sentence : ")
    words = sentence.split()
    for n in words:
        print(n)


display_arguments()
