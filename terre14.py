# Trié ou pas

import sys


def order(*a):
    try:
        numbers = [int(i) for i in a]
        is_sorted = True

        for n in range(len(numbers) - 1):
            if numbers[n] > numbers[n + 1]:
                is_sorted = False
                break

        if is_sorted:
            print("trié !")
        else:
            print("pas trié !")

    except ValueError:
        print("Erreur: Veuillez fournir des nombres en tant qu'argument.")


if len(sys.argv) > 5:
    print("Erreur: Veuillez fournir des nombres en tant qu'argument.")
elif len(sys.argv) >= 2:
    arguments = sys.argv[1:]
    order(*arguments)
else:
    print("Erreur: Veuillez fournir des nombres en tant qu'argument.")
