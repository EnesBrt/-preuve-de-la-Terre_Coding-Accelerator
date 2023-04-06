# L’alphabet à partir de

import sys

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v",
           "w", "x", "y", "z"]


def index(letter):
    index = 0

    for i in range(len(letters)):
        if letters[i] == letter:
            index = i

    result = ''.join(letters[index:])
    print(result)


if len(sys.argv) > 2:
    print("Erreur : Veuillez entrer qu'un seul argument.")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    index(message)
else:
    print("Erreur : Veuillez entrer qu'un seul argument.")
