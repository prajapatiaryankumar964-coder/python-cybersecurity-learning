import os
import hashlib


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except PermissionError:
        return "Permission Denied"


folder_path = input("Enter folder path: ")

if os.path.exists(folder_path) and os.path.isdir(folder_path):

    print("\n===== DIRECTORY HASH REPORT =====\n")

    for filename in os.listdir(folder_path):

        filepath = os.path.join(folder_path, filename)

        if os.path.isfile(filepath):
            file_hash = calculate_hash(filepath)

            print("File:", filename)
            print("SHA-256:", file_hash)
            print("-" * 50)

else:
    print("❌ Invalid folder path!")