# Simple Port Scanner

A Python-based port scanner developed for educational purposes to demonstrate network reconnaissance techniques. This tool identifies open TCP ports on a single target host, showcasing socket programming and multi-threading concepts.

## Features
- Scans a user-specified range of TCP ports (default: 1–1024).
- Identifies open ports and their associated services (e.g., port 80 for HTTP, 50000 for Custom Chat App).
- Employs multi-threading (50 threads) for efficient scanning with a 1-second timeout per port.
- Logs scan details to `port_scan.log` (excluded from repository).
- Validates IP addresses and port ranges to ensure accurate inputs.

## Prerequisites
- **Python 3.x**: Verify installation with:
  ```bash
  python3 --version
  ```
- **Permissions**: You must have explicit permission to scan the target host.
- **Firewall Configuration**: Ensure the scanning device allows outgoing TCP connections and the target allows incoming TCP connections.

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd simple-port-scanner
   ```
2. Verify the presence of `port_scanner.py`, `.gitignore`, `README.md`, and `LICENSE`:
   ```bash
   ls
   ```
3. Confirm Python 3 is installed:
   ```bash
   python3 --version
   ```

## Usage
Run the scanner with the following command:
```bash
python3 port_scanner.py <target_ip> [start_port] [end_port]
```

### Examples
- **Scan Localhost (Ports 1–1024)**:
  ```bash
  python3 port_scanner.py <your_server_ip>
  ```
  **Sample Output**:
  ```
  Scanning <your_server_ip> from port 1 to 1024...
  Port 80 is OPEN (HTTP)
  Port 443 is OPEN (HTTPS)

  Open ports found:
  Port 80: HTTP
  Port 443: HTTPS
  Scan completed in 5.23 seconds
  ```

- **Scan Specific Port Range (Ports 1–100)**:
  ```bash
  python3 port_scanner.py <your_server_ip> 100
  ```

- **Scan a Custom Server (Port 50000)**:
  ```bash
  python3 port_scanner.py <your_server_ip> 50000 50000
  ```
  **Sample Output**:
  ```
  Scanning <your_server_ip> from port 50000 to 50000...
  Port 50000 is OPEN (Custom Chat App)
  Open ports found:
  Port 50000: Custom Chat App
  Scan completed in 0.12 seconds
  ```

## Output Files
- **Log File**: Scan results are logged to `port_scan.log` (excluded from repository).
  - **Example Entry**:
    ```
    2025-08-31 17:14:23 - Port 80 is OPEN (HTTP)
    ```

## Security Note
This tool is for **educational purposes only**. Scanning systems or networks without explicit permission is illegal and unethical. Use only on systems you own or have written authorization to scan (e.g., a lab environment). Replace `<your_server_ip>` with your own authorized IP address.

## Troubleshooting
- **Invalid IP Address**:
  - Ensure the IP is a valid IPv4 address.
  - Verify with:
    ```bash
    ping <target_ip>
    ```
- **No Open Ports**:
  - Start a service (e.g., HTTP server):
    ```bash
    python3 -m http.server 80
    ```
  - Check firewall settings (e.g., Windows):
    ```bash
    netsh advfirewall firewall add rule name="Port Scanner" dir=in action=allow protocol=TCP localport=1-1024
    ```
- **Connection Errors**: Confirm the target is reachable and not blocking connections.
- **Slow Scans**: Reduce the port range (e.g., `1 100`) or adjust threads in `port_scanner.py` (edit `range(50)`).

## Testing with a Custom Application
To test with a custom server (e.g., a chat application on port 50000):
1. Start the server:
   ```bash
   python server.py 50000
   ```
2. Configure the firewall (e.g., Windows):
   ```bash
   netsh advfirewall firewall add rule name="Custom Server" dir=in action=allow protocol=TCP localport=50000
   ```
3. Scan the server:
   ```bash
   python3 port_scanner.py <your_server_ip> 50000 50000
   ```

## Repository Contents
The project is hosted at `<your-repo-url>` and includes:
- `port_scanner.py`
- `.gitignore`
- `README.md`
- `LICENSE`

Sensitive files (e.g., `port_scan.log`) are excluded via `.gitignore` to prevent uploading scan results or IP addresses.

## License
This project is licensed under the Simple Port Scanner Educational Use Only License. See the [LICENSE](LICENSE) file for details. The code may be viewed and run for educational purposes only; modifications and distribution are prohibited without explicit permission from the author.

## Disclaimer
This project is for educational use only. Do not use on unauthorized systems or networks. The author is not responsible for any misuse.