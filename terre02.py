# Afficheur d’arguments

import sys


def display_arguments(arguments):
    for n in arguments:
        print(n)


arguments = sys.argv[1:]
display_arguments(arguments)
