# Racine carrée d’un nombre

import sys


def square_root(a):
    a = int(a)
    result = a ** (1 / 2)
    print(int(result))


if len(sys.argv) > 2:
    print("Erreur : Veuillez fournir un nombres en tant qu'argument.")
elif len(sys.argv) == 2:
    number = sys.argv[1]
    if number.isalpha():
        print("Erreur : Veuillez fournir un nombre en tant qu'argument.")
    else:
        square_root(number)
else:
    print("Erreur : Veuillez fournir un message en tant qu'argument.")
