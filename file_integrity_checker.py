import hashlib
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


filename = input("Enter file name: ")

if not os.path.exists(filename):
    print("File not found!")

else:
    current_hash = calculate_hash(filename)

    print("\n===== FILE INTEGRITY CHECK =====")
    print("File:", filename)
    print("SHA-256 Hash:", current_hash)

    save = input("\nSave this hash? (yes/no): ")

    if save.lower() == "yes":
        with open("original_hash.txt", "w") as hash_file:
            hash_file.write(current_hash)

        print("Original hash saved successfully!")