# Educational tool to scan TCP ports on a target host
# Use only on authorized systems with explicit permission

import socket
import sys
import logging
import threading
from queue import Queue
import time
import re

# Configure logging to a file
logging.basicConfig(filename='port_scan.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Expanded port-to-service mappings
COMMON_PORTS = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    445: "SMB", 1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 50000: "Custom Chat App"  # Added for your chat app
}

def scan_port(host, port, results):
    """Attempt to connect to a single port and log the result."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # 1-second timeout per port
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            print(f"Port {port} is OPEN ({service})")
            logging.info(f"Port {port} is OPEN ({service})")
            results.append((port, service))
        sock.close()
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")
    finally:
        sock.close()

def scan_ports(host, start_port, end_port):
    """Scan a range of ports on the target host using multiple threads."""
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    logging.info(f"Starting scan on {host} from port {start_port} to {end_port}")
    start_time = time.time()

    results = []
    queue = Queue()
    threads = []

    # Add ports to the queue
    for port in range(start_port, end_port + 1):
        queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            scan_port(host, port, results)
            queue.task_done()

    # Start 50 threads for faster scanning
    for _ in range(50):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Sort and display results
    results.sort()
    if results:
        print("\nOpen ports found:")
        for port, service in results:
            print(f"Port {port}: {service}")
    else:
        print("No open ports found.")
    logging.info(f"Scan completed in {time.time() - start_time:.2f} seconds")
    print(f"Scan completed in {time.time() - start_time:.2f} seconds")

def main():
    """Main function to parse arguments and start the scan."""
    if len(sys.argv) < 2:
        print("Usage: python3 port_scanner.py <target_ip> [start_port] [end_port]")
        sys.exit(1)

    host = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    # Validate IP address
    if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", host):
        print("Error: Invalid IP address")
        logging.error(f"Invalid IP address: {host}")
        sys.exit(1)

    # Validate port range
    if not (1 <= start_port <= end_port <= 65535):
        print("Error: Ports must be between 1 and 65535, and start_port <= end_port")
        logging.error(f"Invalid port range: {start_port}-{end_port}")
        sys.exit(1)

    scan_ports(host, start_port, end_port)

if __name__ == "__main__":
    main()