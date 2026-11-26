#suppose you are given a line of text as a plain text.
# find out the corresponding Caesar Cipher(i.e.character three to the right modulo26)
# Then perform the reverse operation to get original plain text...

def encrypt(text):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        else:
            result += char

    return result

plaintext = input("Enter the plain text: ")

ciphertext = encrypt(plaintext)
print("Encrypted Text:", ciphertext)

original_text = decrypt(ciphertext)
print("Decrypted Text:", original_text)
