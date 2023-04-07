# Trouver la Suisse

import sys


def isalpha(input_string):
    for x in input_string:
        if not ('a' <= x <= 'z'):
            return False
    return True


def find_the_middle(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)

    numbers = [a, b, c]

    minimum = numbers[0]
    maximum = numbers[0]
    number = 0

    equal = False
    for n in range(1, len(numbers)):
        if numbers[n] == numbers[0]:
            equal = True
            break

    if equal:
        print("erreur.")

    for n in numbers:
        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

    numbers.remove(minimum)
    numbers.remove(maximum)

    for x in numbers:
        if equal:
            break
        else:
            number += x
            print(number)


if len(sys.argv) > 4:
    print("Erreur: Veuillez entrer trois argument.")
elif len(sys.argv) == 4:
    number_one = sys.argv[1]
    number_two = sys.argv[2]
    number_three = sys.argv[3]
    if isalpha(number_one) and isalpha(number_two) and isalpha(number_three):
        print("Erreur: les arguments doivent être trois nombres entiers.")
    else:
        find_the_middle(number_one, number_two, number_three)
else:
    print("Erreur: Veuillez entrer trois arguments.")
