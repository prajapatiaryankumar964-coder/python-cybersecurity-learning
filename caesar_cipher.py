def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr(
                (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            )
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== SIMPLE ENCRYPTION TOOL =====")

choice = input("1. Encrypt\n2. Decrypt\nEnter choice: ")

text = input("Enter your message: ")
shift = int(input("Enter shift number: "))

if choice == "1":
    result = encrypt(text, shift)
    print("Encrypted Text:", result)

elif choice == "2":
    result = decrypt(text, shift)
    print("Decrypted Text:", result)

else:
    print("Invalid choice!")