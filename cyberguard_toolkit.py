import hashlib
import secrets
import string
import socket
import ipaddress
import os
import time
import re
import requests
from urllib.parse import urlparse


# ===============================
# 1. PASSWORD STRENGTH CHECKER
# ===============================

def password_strength():

    password = input("Enter password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*]", password):
        score += 1

    print("\n===== PASSWORD RESULT =====")

    if score <= 2:
        print("Weak Password ❌")
    elif score <= 4:
        print("Medium Password ⚠️")
    else:
        print("Strong Password ✅")


# ===============================
# 2. PASSWORD GENERATOR
# ===============================

def password_generator():

    length = int(input("Enter password length: "))

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print("Generated Password:", password)


# ===============================
# 3. TEXT HASH GENERATOR
# ===============================

def text_hasher():

    text = input("Enter text: ")

    result = hashlib.sha256(
        text.encode()
    ).hexdigest()

    print("SHA-256 Hash:")
    print(result)


# ===============================
# 4. FILE HASH GENERATOR
# ===============================

def file_hash():

    filename = input("Enter file path: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    print("SHA-256 Hash:")
    print(sha256.hexdigest())


# ===============================
# 5. FILE METADATA ANALYZER
# ===============================

def file_metadata():

    filename = input("Enter file path: ")

    if os.path.exists(filename):

        print("\n===== FILE INFORMATION =====")

        print("File Name:", os.path.basename(filename))
        print("Extension:", os.path.splitext(filename)[1])
        print("Size:", os.path.getsize(filename), "bytes")

        print(
            "Created:",
            time.ctime(os.path.getctime(filename))
        )

        print(
            "Modified:",
            time.ctime(os.path.getmtime(filename))
        )

    else:
        print("File not found!")


# ===============================
# 6. IP ADDRESS ANALYZER
# ===============================

def ip_analyzer():

    ip_input = input("Enter IP Address: ")

    try:

        ip = ipaddress.ip_address(ip_input)

        print("\n===== IP REPORT =====")

        print("IP:", ip)
        print("Version:", ip.version)
        print("Private:", ip.is_private)
        print("Loopback:", ip.is_loopback)
        print("Multicast:", ip.is_multicast)

    except ValueError:
        print("Invalid IP Address!")


# ===============================
# 7. URL VALIDATOR
# ===============================

def url_validator():

    url = input("Enter URL: ")

    parsed = urlparse(url)

    if parsed.scheme in ("http", "https") and parsed.netloc:

        print("Valid URL ✅")
        print("Protocol:", parsed.scheme)
        print("Domain:", parsed.netloc)

    else:
        print("Invalid URL ❌")


# ===============================
# 8. DNS LOOKUP
# ===============================

def dns_lookup():

    domain = input("Enter domain: ")

    try:

        ip = socket.gethostbyname(domain)

        print("Domain:", domain)
        print("IP Address:", ip)

    except socket.gaierror:
        print("DNS Lookup Failed!")


# ===============================
# 9. SECURITY LOG ANALYZER
# ===============================

def log_analyzer():

    filename = input("Enter log file name: ")

    if not os.path.exists(filename):
        print("Log file not found!")
        return

    failed_users = {}

    with open(filename, "r") as file:

        for line in file:

            if "FAILED LOGIN" in line:

                if "user=" in line:

                    user = line.split("user=")[1].strip()

                    failed_users[user] = (
                        failed_users.get(user, 0) + 1
                    )

    print("\n===== LOG ANALYSIS REPORT =====")

    if not failed_users:
        print("No failed login attempts found.")

    for user, count in failed_users.items():

        print(
            f"User: {user} | Failed Attempts: {count}"
        )

        if count >= 3:
            print("⚠️ Suspicious Activity Detected!")


# ===============================
# 10. SECURITY HEADER CHECKER
# ===============================

def security_headers():

    url = input("Enter website URL: ")

    headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Referrer-Policy"
    ]

    try:

        response = requests.get(url, timeout=5)

        print("\n===== SECURITY HEADER REPORT =====")

        print("Status Code:", response.status_code)

        for header in headers:

            if header in response.headers:
                print(f"✅ {header}")
            else:
                print(f"⚠️ {header} - Not Found")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


# ===============================
# MAIN MENU
# ===============================

while True:

    print("\n")
    print("=" * 45)
    print("     CYBERGUARD SECURITY TOOLKIT")
    print("=" * 45)

    print("1. Password Strength Checker")
    print("2. Secure Password Generator")
    print("3. Text SHA-256 Hasher")
    print("4. File Hash Generator")
    print("5. File Metadata Analyzer")
    print("6. IP Address Analyzer")
    print("7. URL Validator")
    print("8. DNS Lookup")
    print("9. Security Log Analyzer")
    print("10. Security Header Checker")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        password_strength()

    elif choice == "2":
        password_generator()

    elif choice == "3":
        text_hasher()

    elif choice == "4":
        file_hash()

    elif choice == "5":
        file_metadata()

    elif choice == "6":
        ip_analyzer()

    elif choice == "7":
        url_validator()

    elif choice == "8":
        dns_lookup()

    elif choice == "9":
        log_analyzer()

    elif choice == "10":
        security_headers()

    elif choice == "0":
        print("Thank you for using CyberGuard Toolkit!")
        break

    else:
        print("Invalid Choice!")