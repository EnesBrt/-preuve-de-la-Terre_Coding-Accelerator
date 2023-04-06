# Trouver la Suisse

import sys


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
    print("Erreur: Veuillez entrer trois arguments.")
elif len(sys.argv) == 4:
    number_one = sys.argv[1]
    number_two = sys.argv[2]
    number_three = sys.argv[3]
    if number_one.isalpha() and number_two.isalpha():
        print("Erreur: les arguments doivent être trois nombres entiers.")
    else:
        find_the_middle(number_one, number_two, number_three)
else:
    print("Erreur: Veuillez entrer trois arguments.")
