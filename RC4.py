
def RC4(key,data):
    S = list(range(256))
    print(S)
    T=[ord(key[i%len(key)]) for i in range(256)]
    print(T)
    j =0
    for i in range(256):
        j = (j+S[i]+T[i])%256
        S[i], S[j] = S[j], S[i]
    encrypt = []
    for char in data:
        i = (i+1)%256
        j = (j+S[i])%256
        S[i], S[j] = S[j], S[i]
        t = (S[i]+S[j])%256
        k= S[t]
        encrypt.append(chr(ord(char) ^ k))
    print(S)
    return ''.join(encrypt)

key="secret"
plaintext="hello world hello world hello world skdqposfdqos"
cipher = RC4(key,plaintext)

print("encrypted:",cipher)

decrypted = RC4(key,cipher)
print("decrypted:",decrypted)
