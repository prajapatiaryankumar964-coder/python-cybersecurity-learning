import socket

domain = input("Enter domain name (example: google.com): ")

try:
    ip_address = socket.gethostbyname(domain)

    print("\n===== DNS LOOKUP RESULT =====")
    print("Domain:", domain)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("Invalid domain or DNS lookup failed!")