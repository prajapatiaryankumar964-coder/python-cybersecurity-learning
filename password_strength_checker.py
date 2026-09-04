import re

password = input("Enter a password to check: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1

# Number check
if re.search(r"[0-9]", password):
    score += 1

# Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1


print("\n===== PASSWORD STRENGTH RESULT =====")

if score <= 2:
    print("Strength: Weak ❌")
elif score <= 4:
    print("Strength: Medium ⚠️")
else:
    print("Strength: Strong ✅")

print("Score:", score, "/ 5")