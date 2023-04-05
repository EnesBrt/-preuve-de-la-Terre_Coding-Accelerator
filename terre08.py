# Puissance d’un nombre

import sys


def power(a, b):
    a = int(a)
    b = int(b)
    result = a ** b
    print(result)


if len(sys.argv) > 3:
    print("Erreur : Veuillez fournir deux nombres en tant qu'argument.")
elif len(sys.argv) == 3:
    number_one = sys.argv[1]
    number_two = sys.argv[2]
    if number_one.isalpha() and number_two.isalpha():
        print("Erreur : Veuillez fournir deux nombres en tant qu'argument.")
    else:
        power(number_one, number_two)
else:
    print("Erreur : Veuillez fournir un message en tant qu'argument.")
