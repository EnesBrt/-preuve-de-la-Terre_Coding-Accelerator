# Inverser une chaîne

def inverse(words):
    print(words[::-1])

    if not words:
        print("erreur, l'entrer est vide.")


word = input()

inverse(word)
