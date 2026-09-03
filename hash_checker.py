import hashlib

file_name = input("Enter file name: ")

sha256 = hashlib.sha256()

with open(file_name, "rb") as file:
    while True:
        data = file.read(4096)

        if not data:
            break

        sha256.update(data)

print("SHA-256 Hash:")
print(sha256.hexdigest())