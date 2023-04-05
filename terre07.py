# Taille d’une chaîne

import sys


def len_string(string):
    print(len(string))


if len(sys.argv) > 2:
    print("Erreur : Veuillez fournir un seul message en tant qu'argument.")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    if message.isdigit():
        print("Erreur : Veuillez fournir une chaîne de caractères non numérique en tant qu'argument.")
    else:
        len_string(message)
else:
    print("Erreur : Veuillez fournir un seul message en tant qu'argument.")
