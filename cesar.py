def cesar(k, word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    word = word.lower()

    for char in word:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx + k) % 26
            result += alphabet[new_idx]
        else:
            result += char

    return result



word = "meow"
k = 3
print("Chiffré :", cesar(k, word))
res = cesar(k, word)
print("Déchiffré :", cesar(-k, res))
