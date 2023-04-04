# L’alphabet à partir de

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v",
           "w", "x", "y", "z"]


def index(letter):

    element_index = 0

    for i in range(len(letters)):
        if letters[i] == letter:
            element_index = i
    print(f"the index of {letter} is: ", element_index)


index("o")
