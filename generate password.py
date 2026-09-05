import secrets
import string
import random

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Password length must be at least 8!")
else:
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    random.SystemRandom().shuffle(password)

    print("\nSecure Password:")
    print("".join(password))