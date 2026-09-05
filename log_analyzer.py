failed_attempts = 0

with open("security_log.txt", "r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            failed_attempts += 1
            print("Suspicious Activity:", line.strip())

print("\n===== SECURITY LOG REPORT =====")
print("Total Failed Login Attempts:", failed_attempts)

if failed_attempts >= 3:
    print("⚠️ ALERT: Multiple failed login attempts detected!")
else:
    print("✅ Login activity looks normal.")