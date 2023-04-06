# Trié ou pas

import sys


def order(*a):

    numbers = [int(i) for i in a]

    for n in range(len(numbers) - 1):
        if numbers[n] > numbers[n + 1] > numbers[n + 2] > numbers[n + 3] or numbers[n + 1] > numbers[n + 2] or numbers[n + 2] > numbers[n + 3]:
            print("pas trié !")
            break
        else:
            print("trié !")
            break


if len(sys.argv) > 5:
    print("Erreur: Veuillez fournir des nombres en tant qu'argument.")
elif len(sys.argv) >= 2:
    arguments = sys.argv[1:]

    for arg in arguments:
        if arg.isalpha():
            print("Erreur: Veuillez fournir des nombres en tant qu'argument.")
            break
    else:
        order(*arguments)
else:
    print("Erreur: Veuillez fournir des nombres en tant qu'argument.")
