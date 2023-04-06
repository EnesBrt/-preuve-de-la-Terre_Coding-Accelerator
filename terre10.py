# Nombre premier

import sys


def prime_number(a):
    a = int(a)
    square_root = a ** (1 / 2)
    if a <= 1:
        print(f"Non, {a} n’est pas un nombre premier.")
    elif a == 2:
        print(f"Oui, {a} est un nombre premier.")
    elif a > 2 and a % 2 == 0:
        print(f"Non, {a} n’est pas un nombre premier.")
    else:
        for n in range(3, int(square_root) + 1, 2):
            if a % n == 0:
                print(f"Non, {a} n’est pas un nombre premier.")
                break
        else:
            print(f"Oui, {a} est un nombre premier.")


if len(sys.argv) > 2:
    print("Erreur : Veuillez entrer qu'un seul argument..")
elif len(sys.argv) == 2:
    number = sys.argv[1]
    if number.isalpha():
        print("Erreur : l'argument doit être un nombre entier.")
    else:
        prime_number(number)
else:
    print("Erreur : Veuillez entrer qu'un seul argument.")
