# Taille d’une chaîne

import sys


def isdigit(s):
    for x in s:
        if not ('0' <= x <= '9'):
            return False
    return True


def len_string(string):
    print(len(string))


if len(sys.argv) > 2:
    print("Erreur : Veuillez entrer qu'un seul argument.")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    if isdigit(message):
        print("Erreur : l'argument doit être une chaine de charactère.")
    else:
        len_string(message)
else:
    print("Erreur : Veuillez entrer qu'un seul argument.")
