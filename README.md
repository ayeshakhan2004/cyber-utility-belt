# 🦇 Cyber Utility Belt

Welcome to the **Cyber Utility Belt**! This repository is a curated collection of Python-based automation scripts and InfoSec tools designed for security analysts, penetration testers, and OSINT researchers. 

Whether you are performing initial reconnaissance, auditing passwords, or analyzing network headers, this toolkit provides fast, multi-threaded, command-line utilities to get the job done.

---

## 🧰 Tools Included

### 🕵️‍♂️ OSINT & Reconnaissance
* **`email_scraper.py`**: An OSINT tool that uses Regular Expressions to extract hidden email addresses from target webpages.
* **`ip_geolocator.py`**: A tracking script that resolves IP addresses to their real-world geographical locations.
* **`url_unshortener.py`**: Safely analyze, expand, and inspect potentially malicious or disguised phishing links without clicking them.

### 🕸️ Network & Web Scanning
* **`ping_sweeper.py`**: A fast, multi-threaded script to ping sweep local subnets and identify active network hosts.
* **`subdomain_scanner.py`**: A multi-threaded reconnaissance tool that enumerates hidden subdomains for a given target domain.
* **`dir_scanner.py`**: A fast, multi-threaded web fuzzer that discovers hidden directories and sensitive files (like `.env` or `/admin`) on target servers.
* **`banner_grabber.py`**: A network recon tool that connects to open ports to identify running services and software versions.
* **`header_analyzer.py`**: Connects to web servers to analyze HTTP security headers and identify missing security configurations.
* **arp_scanner.py**: A Layer 2 discovery tool that uses ARP requests to identify stealthy, firewalled hosts on local subnets that might ignore standard ICMP pings.

### 🔐 Cryptography & Cracking
* **`hash_cracker.py`**: A fast MD5 dictionary hash cracker built for password auditing and recovery.
* **`base64_tool.py`**: A rapid Base64 encoder and decoder specifically built for payload analysis and obfuscation testing.
* **`password_gen.py`**: Generates highly complex, cryptographically secure passwords.

---

## 💻 Installation

Clone this repository to your local machine to get started:

```bash
# Clone the repository
git clone [https://github.com/ayeshakhan2004/cyber-utility-belt.git](https://github.com/ayeshakhan2004/cyber-utility-belt.git)

# Navigate into the directory
cd cyber-utility-belt