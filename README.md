# security-scripts
Python scripts built for network security and
automation as part of my cybersecurity learning
journey.

---

## Scripts

### port-scanner.py
A basic TCP port scanner that checks whether
common ports are open or closed on a target IP.

**Ports checked:** FTP (21), SSH (22), Telnet (23),
SMTP (25), DNS (53), HTTP (80), HTTPS (443),
SMB (445), RDP (3389), HTTP-Alt (8080)

**How it works:**
Uses Python's socket library to attempt a TCP
connection to each port. If the connection
succeeds, the port is open. If it fails or
times out, the port is closed.

**Usage:**
