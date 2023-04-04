# Inverser une chaîne

def inverse(words):
    print(words[::-1])

    if not words:
        print("erreur.")


word = input()

inverse(word)
