import ipaddress
from urllib.parse import urlparse

print("===== IP / URL VALIDATOR =====")

choice = input("Enter 1 for IP or 2 for URL: ")

if choice == "1":
    ip = input("Enter IP Address: ")

    try:
        ipaddress.ip_address(ip)
        print("Valid IP Address:", ip)
    except ValueError:
        print("Invalid IP Address!")

elif choice == "2":
    url = input("Enter URL: ")

    parsed = urlparse(url)

    if parsed.scheme in ("http", "https") and parsed.netloc:
        print("Valid URL:", url)
        print("Protocol:", parsed.scheme)
        print("Domain:", parsed.netloc)
    else:
        print("Invalid URL!")

else:
    print("Invalid choice!")