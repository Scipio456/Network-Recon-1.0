Simple Port Scanner

A Python-based port scanner that identifies open TCP and UDP ports on target hosts, mimicking advanced functionality of tools like Nmap. Developed as part of MCA cybersecurity coursework to explore network reconnaissance techniques, this tool is designed for educational purposes and demonstrates socket programming, multi-threading, and vulnerability assessment basics.

Features





Scans a user-specified range of ports (default: 1–1024) on a single IP or multiple IP addresses.



Supports both TCP and UDP scanning (--udp flag).



Reports open ports, their associated services (e.g., port 80 for HTTP, 50000 for Custom Chat App), and service banners for TCP ports (e.g., "Apache/2.4.41").



Saves scan results to JSON or CSV files (--output json|csv, excluded from repository).



Uses multi-threading (50 threads) for efficient scanning with a 1-second timeout per port.



Logs scan details to port_scan.log for auditing (excluded from repository).



Validates IP addresses and port ranges to prevent errors.

Prerequisites





Python 3.x installed (check with python3 --version).



Permission to scan the target host(s) (e.g., your own system, such as 127.0.0.1, or authorized network devices).



Firewall configured to allow outgoing TCP/UDP connections on the scanning device and incoming connections on the target.



Administrative privileges (e.g., sudo) may be required for UDP scanning or low-numbered ports.

Setup





Clone the repository from GitHub:

git clone <your-repo-url>
cd MCA-Port-Scanner



Ensure port_scanner.py, .gitignore, README.md, and LICENSE are present:

ls



Verify Python 3 is installed:

python3 --version

Usage

Run the scanner from the command line with the following syntax:

python3 port_scanner.py <target_ip_or_range> [start_port] [end_port] [--udp] [--output json|csv]

Examples





TCP Scan on Localhost (default ports 1–1024):

python3 port_scanner.py 127.0.0.1

Output:

Scanning 127.0.0.1 from port 1 to 1024 (TCP)...
Port 80 is OPEN (HTTP) - Banner: Apache/2.4.41
Port 443 is OPEN (HTTPS)

Open ports found:
Port 80: HTTP (TCP) - Banner: Apache/2.4.41
Port 443: HTTPS (TCP) - Banner: No banner
Scan completed in 5.23 seconds



UDP Scan on Localhost (requires sudo):

sudo python3 port_scanner.py 127.0.0.1 --udp



TCP Scan with Specific Port Range (e.g., ports 1–100):

python3 port_scanner.py 127.0.0.1 1 100



Scan a Local Network (replace <your_network> with your authorized IP range, e.g., a lab network):

python3 port_scanner.py <your_network> 1 100



Scan Chat App Server (e.g., your Windows machine running server.py on port 50000):

python3 port_scanner.py <your_windows_ip> 50000 50000

Output:

Scanning <your_windows_ip> from port 50000 to 50000 (TCP)...
Port 50000 is OPEN (Custom Chat App)
Open ports found:
Port 50000: Custom Chat App (TCP) - Banner: No banner
Scan completed in 0.12 seconds



Save Results to JSON:

python3 port_scanner.py 127.0.0.1 --output json

Creates scan_results_127_0_0_1.json (not uploaded to GitHub).



Save Results to CSV:

python3 port_scanner.py <your_windows_ip> --output csv

Creates scan_results_<ip>.csv (not uploaded).

Output Files





Log File: Scan details are logged to port_scan.log (excluded from repository).



JSON/CSV Files: Results are saved to scan_results_<ip>.json or scan_results_<ip>.csv if --output is used (excluded via .gitignore).





JSON example:

[{"port": 80, "service": "HTTP", "banner": "Apache/2.4.41"}, {"port": 443, "service": "HTTPS", "banner": "No banner"}]



CSV example:

Port,Service,Protocol,Banner
80,HTTP,TCP,Apache/2.4.41
443,HTTPS,TCP,No banner

Security Note

This tool is for educational purposes only. Scanning ports on systems or networks without explicit permission is illegal and unethical. Use only on systems you own (e.g., 127.0.0.1, your own devices) or have written authorization to scan (e.g., a virtual machine in a lab environment). Replace <your_network> or <your_windows_ip> with your own authorized IP addresses.

Troubleshooting





Invalid IP Address: Ensure the IP is a valid IPv4 address or range (e.g., a private network range).





Check with: ping <target_ip>



No Open Ports: Start a known service (e.g., python3 -m http.server 80) or verify firewall settings.





Windows firewall example:

netsh advfirewall firewall add rule name="Port Scanner" dir=in action=allow protocol=TCP,UDP localport=1-1024



Connection Errors: Ensure the target is reachable and not blocking connections.



Permission Denied: Use sudo for UDP scanning or low-numbered ports:

sudo python3 port_scanner.py 127.0.0.1 --udp



UDP Scanning Unreliable: UDP ports may not respond consistently; test with known services (e.g., DNS on port 53).



Slow Scans: Reduce the port range (e.g., 1 100) or increase threads in port_scanner.py (edit range(50)).

Testing with Your Chat Application

To test with your chat application server running on a Windows machine (e.g., <your_windows_ip>:50000):





Start the server on Windows:

python server.py 50000



Allow port 50000 in Windows Firewall:

netsh advfirewall firewall add rule name="Chat Server" dir=in action=allow protocol=TCP localport=50000



Scan from your Mac:

python3 port_scanner.py <your_windows_ip> 50000 50000

GitHub Repository

The project is hosted at <your-repo-url>. Only the following files are included:





port_scanner.py



.gitignore



README.md



LICENSE

Sensitive files (port_scan.log, *.json, *.csv) are excluded via .gitignore to ensure no scan results or IP addresses are uploaded.

License

MIT License (see LICENSE file).

Disclaimer

This project is for educational use only. Do not use on unauthorized systems or networks. The author is not responsible for any misuse.