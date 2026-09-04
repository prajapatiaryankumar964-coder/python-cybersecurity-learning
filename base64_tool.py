import base64

print("===== BASE64 ENCODER / DECODER =====")

choice = input("1. Encode\n2. Decode\nEnter your choice: ")

if choice == "1":
    text = input("Enter text: ")

    encoded = base64.b64encode(text.encode())

    print("\nEncoded Text:")
    print(encoded.decode())

elif choice == "2":
    text = input("Enter Base64 text: ")

    try:
        decoded = base64.b64decode(text.encode())
        print("\nDecoded Text:")
        print(decoded.decode())

    except Exception:
        print("Invalid Base64 input!")

else:
    print("Invalid choice!")