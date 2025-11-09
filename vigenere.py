def vigenere(message,cle):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    message=message.lower()
    cle=cle.lower()
    clelenght=len(cle)
    position = 0
    for i in message:
        if i in alphabet:
            ind = alphabet.index(i)
            key=cle[position%clelenght]
            indice = alphabet.index(key)
            rang = (ind + indice) % 26
            result += alphabet[rang]
            position+=1
        else:
            message +=i

    return result


def vigenere_decrypt(ciphertext, cle):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    ciphertext = ciphertext.lower()
    cle = cle.lower()
    clelenght = len(cle)
    position = 0

    for i in ciphertext:
        if i in alphabet:
            ind = alphabet.index(i)
            key = cle[position % clelenght]
            indice = alphabet.index(key)
            rang = (ind - indice + 26) % 26
            result += alphabet[rang]
            position += 1
        else:
            result += i
    return result

message = "mastercsuemf"
cle = "clefvigenere"

print(vigenere(message,cle))
cipher=vigenere(message,cle)

print(vigenere_decrypt(cipher,cle))


