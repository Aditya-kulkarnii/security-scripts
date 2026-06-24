# Port Scanner
# Written by Aditya Kulkarni
# Purpose: Check which ports are open on a target IP

import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return True
        return False
    except:
        return False

def scan_target(ip):
    print(f"\nScanning {ip}...\n")
    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        445: "SMB",
        3389: "RDP",
        8080: "HTTP-Alt"
    }
    for port, name in ports.items():
        if scan_port(ip, port):
            print(f"[OPEN]   Port {port} - {name}")
        else:
            print(f"[CLOSED] Port {port} - {name}")
    print("\nScan complete.")

scan_target("127.0.0.1")
