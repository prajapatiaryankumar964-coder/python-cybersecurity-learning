import hashlib
import secrets

def hash_password(password, salt):
    combined = password + salt
    return hashlib.sha256(combined.encode()).hexdigest()


print("===== SALTED PASSWORD HASHING =====")

password = input("Create a password: ")

# Generate random salt
salt = secrets.token_hex(16)

# Create hash
stored_hash = hash_password(password, salt)

print("\n===== STORED SECURITY DATA =====")
print("Salt:", salt)
print("Password Hash:", stored_hash)


print("\n===== LOGIN VERIFICATION =====")

login_password = input("Enter password again: ")

login_hash = hash_password(login_password, salt)

if login_hash == stored_hash:
    print("✅ Password Verified Successfully!")
else:
    print("❌ Incorrect Password!")