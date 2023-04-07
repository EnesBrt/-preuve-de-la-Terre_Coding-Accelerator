# Puissance d’un nombre

import sys


def isalpha(input_string):
    for x in input_string:
        if not ('a' <= x <= 'z'):
            return False
    return True


def power(a, b):
    a = int(a)
    b = int(b)
    result = a ** b
    if b < 0:
        print("erreur.")
    else:
        print(result)


if len(sys.argv) > 3:
    print("Erreur: Veuillez entrer deux arguments.")
elif len(sys.argv) == 3:
    number_one = sys.argv[1]
    number_two = sys.argv[2]
    if isalpha(number_one) and isalpha(number_two):
        print("Erreur: les arguments doivent être deux nombres entiers.")
    else:
        power(number_one, number_two)
else:
    print("Erreur: Veuillez entrer deux arguments.")
