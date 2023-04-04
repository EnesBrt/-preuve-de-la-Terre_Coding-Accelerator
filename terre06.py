# Inverser une chaîne

def inverse(words):
    print(words[::-1])

    if not words:
        raise ValueError("L'entrer est vide.")


word = input()

inverse(word)
