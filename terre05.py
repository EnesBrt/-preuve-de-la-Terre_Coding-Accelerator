# Divisions

import sys

def division(a, b):
    try:
        a = int(a)
        b = int(b)
        result = int((a / b))
        remainder = a % b

        if result != 0:
            print(f"réslutat: {result} \n"
                  f"reste: {remainder}")
        else:
            print("erreur.")

    except ZeroDivisionError:
        print("erreur.")


if len(sys.argv) > 3:
    print("Erreur : Veuillez entrer deux arguments.")
elif len(sys.argv) == 3:
    first_argument = sys.argv[1]
    second_argument = sys.argv[1]
    division(first_argument, second_argument)
else:
    print("Erreur : Veuillez entrer deux arguments.")
