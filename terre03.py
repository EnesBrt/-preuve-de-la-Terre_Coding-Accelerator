# L’alphabet à partir de

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v",
           "w", "x", "y", "z"]


def index(letter):
    index = 0

    for i in range(len(letters)):
        if letters[i] == letter:
            index = i

    result = ''.join(letters[index:])
    print(result)


letter = input("write a letter: ").lower()

index(letter)
