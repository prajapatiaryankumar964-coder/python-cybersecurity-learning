import os
import time
import hashlib


def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


filename = input("Enter file path: ")

if os.path.exists(filename):

    file_name = os.path.basename(filename)
    file_extension = os.path.splitext(filename)[1]
    file_size = os.path.getsize(filename)

    created_time = os.path.getctime(filename)
    modified_time = os.path.getmtime(filename)

    file_hash = calculate_sha256(filename)

    print("\n" + "=" * 40)
    print("      FILE SECURITY REPORT")
    print("=" * 40)

    print("File Name      :", file_name)
    print("Extension      :", file_extension)
    print("File Size      :", file_size, "bytes")
    print("Created Time   :", time.ctime(created_time))
    print("Modified Time  :", time.ctime(modified_time))
    print("SHA-256 Hash   :", file_hash)

    print("=" * 40)

else:
    print("❌ File not found!")