#find out the polygram substitution cipher of a given plain text
# (consider the block size of 3).then perform the reverse operation to get original plaintext

def encrypt(text):
    result = ""

    text = text.upper().replace(" ", "")

    while len(text) % 3 != 0:
        text += 'X'

    for i in range(0, len(text), 3):
        block = text[i:i+3]

        encrypted_block = ""

        for char in block:
            encrypted_block += chr(
                (ord(char) - ord('A') + 3) % 26
                + ord('A')
            )

        result += encrypted_block

    return result

def decrypt(text):
    result = ""

    for i in range(0, len(text), 3):
        block = text[i:i+3]

        decrypted_block = ""

        for char in block:
            decrypted_block += chr(
                (ord(char) - ord('A') - 3) % 26
                + ord('A')
            )

        result += decrypted_block

    return result

plaintext = input("Enter Plain Text: ")

ciphertext = encrypt(plaintext)
print("Encrypted Text:", ciphertext)

original = decrypt(ciphertext)
print("Decrypted Text:", original)
