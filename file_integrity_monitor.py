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
    print("❌ File not found!")

else:
    current_hash = calculate_hash(filename)

    hash_file_name = filename + ".hash"

    if not os.path.exists(hash_file_name):

        with open(hash_file_name, "w") as file:
            file.write(current_hash)

        print("✅ First scan completed!")
        print("Original hash saved.")

    else:

        with open(hash_file_name, "r") as file:
            original_hash = file.read()

        print("\n===== FILE INTEGRITY RESULT =====")

        if current_hash == original_hash:
            print("✅ File is SAFE!")
            print("No modification detected.")

        else:
            print("⚠️ WARNING: FILE MODIFIED!")
            print("The file content has changed.")