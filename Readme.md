Simple Port Scanner

A Python-based port scanner designed for educational purposes to demonstrate basic network reconnaissance techniques. This tool identifies open TCP ports on a target host, showcasing socket programming and multi-threading concepts.

Features





Scans a user-specified range of TCP ports (default: 1–1024) on a single IP address.



Reports open ports and their associated services (e.g., port 80 for HTTP, 50000 for Custom Chat App).



Uses multi-threading (50 threads) for efficient scanning with a 1-second timeout per port.



Logs scan details to port_scan.log for auditing (excluded from repository).



Validates IP addresses and port ranges to prevent errors.

Prerequisites





Python 3.x installed (check with python3 --version).



Permission to scan the target host (e.g., your own system, such as 127.0.0.1, or authorized devices).



Firewall configured to allow outgoing TCP connections on the scanning device and incoming TCP connections on the target.

Setup





Clone the repository from GitHub:

git clone <your-repo-url>
cd simple-port-scanner



Ensure port_scanner.py, .gitignore, and README.md are present:

ls



Verify Python 3 is installed:

python3 --version

Usage

Run the scanner from the command line with the following syntax:

python3 port_scanner.py <target_ip> [start_port] [end_port]

Examples





TCP Scan on Localhost (default ports 1–1024):

python3 port_scanner.py 127.0.0.1

Output:

Scanning 127.0.0.1 from port 1 to 1024...
Port 80 is OPEN (HTTP)
Port 443 is OPEN (HTTPS)

Open ports found:
Port 80: HTTP
Port 443: HTTPS
Scan completed in 5.23 seconds



TCP Scan with Specific Port Range (e.g., ports 1–100):

python3 port_scanner.py 127.0.0.1 1 100



Scan a Custom Server (e.g., a server running on port 50000):

python3 port_scanner.py <your_server_ip> 50000 50000

Output:

Scanning <your_server_ip> from port 50000 to 50000...
Port 50000 is OPEN (Custom Chat App)
Open ports found:
Port 50000: Custom Chat App
Scan completed in 0.12 seconds

Output Files





Log File: Scan details are logged to port_scan.log (excluded from repository).





Example log entry:

2025-08-31 17:14:23 - Port 80 is OPEN (HTTP)

Security Note

This tool is for educational purposes only. Scanning ports on systems or networks without explicit permission is illegal and unethical. Use only on systems you own (e.g., 127.0.0.1, your own devices) or have written authorization to scan (e.g., a virtual machine in a lab environment). Replace <your_server_ip> with your own authorized IP address.

Troubleshooting





Invalid IP Address: Ensure the IP is a valid IPv4 address.





Check with: ping <target_ip>



No Open Ports: Start a known service (e.g., python3 -m http.server 80) or verify firewall settings.





Example for allowing ports (Windows):

netsh advfirewall firewall add rule name="Port Scanner" dir=in action=allow protocol=TCP localport=1-1024



Connection Errors: Ensure the target is reachable and not blocking connections.



Slow Scans: Reduce the port range (e.g., 1 100) or increase threads in port_scanner.py (edit range(50)).

Testing with a Custom Application

To test with a custom server (e.g., a chat application running on port 50000):





Start the server on your machine:

python server.py 50000



Allow port 50000 in the firewall:

netsh advfirewall firewall add rule name="Custom Server" dir=in action=allow protocol=TCP localport=50000



Scan from another device:

python3 port_scanner.py <your_server_ip> 50000 50000

GitHub Repository

The project is hosted at <your-repo-url>. Only the following files are included:





port_scanner.py



.gitignore



README.md

Sensitive files (e.g., port_scan.log) are excluded via .gitignore to ensure no scan results or IP addresses are uploaded.

License

All rights reserved. This code is for educational viewing only and may not be copied, modified, or distributed without explicit permission from the author.

Disclaimer

This project is for educational use only. Do not use on unauthorized systems or networks. The author is not responsible for any misuse.