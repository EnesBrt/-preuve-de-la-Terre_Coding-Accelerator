# Racine carrée d’un nombre

import sys


def isalpha(input_string):
    for x in input_string:
        if not ('a' <= x <= 'z'):
            return False
    return True


def square_root(a):
    a = int(a)
    result = a ** (1 / 2)
    print(int(result))


if len(sys.argv) > 2:
    print("Erreur : Veuillez entrer qu'un seul argument.")
elif len(sys.argv) == 2:
    number = sys.argv[1]
    if isalpha(number):
        print("Erreur : Veuillez entrer un nombre en tant qu'argument.")
    else:
        square_root(number)
else:
    print("Erreur : Veuillez entrer qu'un seul argument.")
