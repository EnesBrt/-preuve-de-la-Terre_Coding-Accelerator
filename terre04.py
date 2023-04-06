# Pair ou impair

import sys


def odd_or_even(number):
    try:
        number = int(number)

        if number % 2 == 0:
            print("pair")
        else:
            print("impair")

    except ValueError:
        print("Tu ne me la mettras pas à l’envers.")


if len(sys.argv) == 2:
    arguments = sys.argv[1]
    odd_or_even(arguments)
else:
    print("Tu ne me la mettras pas à l’envers.")