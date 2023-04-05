# Inverser une chaîne

import sys


def inverse(words):
    print(words[::-1])


if len(sys.argv) > 2:
    print("Erreur : Veuillez fournir un seul message en tant qu'argument.")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    inverse(message)
else:
    print("Erreur : Veuillez fournir un message en tant qu'argument.")
