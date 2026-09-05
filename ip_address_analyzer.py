import ipaddress

print("===== IP ADDRESS ANALYZER =====")

ip_input = input("Enter an IP Address: ")

try:
    ip = ipaddress.ip_address(ip_input)

    print("\n===== IP INFORMATION =====")
    print("IP Address :", ip)
    print("IP Version :", ip.version)

    if ip.is_private:
        print("Type       : Private IP")
    else:
        print("Type       : Public IP")

    print("Loopback   :", ip.is_loopback)
    print("Multicast  :", ip.is_multicast)
    print("Reserved   :", ip.is_reserved)

except ValueError:
    print("❌ Invalid IP Address!")
    