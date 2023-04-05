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
    print("Erreur : Veuillez fournir un nombres en tant qu'argument.")
elif len(sys.argv) == 2:
    number = sys.argv[1]
    if number.isalpha():
        print("Erreur : Veuillez fournir un nombre en tant qu'argument.")
    else:
        prime_number(number)
else:
    print("Erreur : Veuillez fournir un nombre en tant qu'argument.")
