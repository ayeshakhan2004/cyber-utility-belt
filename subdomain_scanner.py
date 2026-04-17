import socket
import argparse
import concurrent.futures
import sys

DEFAULT_SUBDOMAINS = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp",
    "pop", "ns1", "webdisk", "ns2", "cpanel", "whm",
    "autodiscover", "autoconfig", "m", "imap", "test",
    "dev", "blog", "server", "ws", "admin", "api", "vpn",
    "staging", "secure", "beta", "portal", "support"
]

def check_subdomain(domain, subdomain):
    target = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] FOUND: {target} ({ip})")
    except socket.gaierror:
        pass
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Fast Subdomain Scanner")
    parser.add_argument("domain", help="The target domain to scan (e.g., example.com)")
    args = parser.parse_args()

    domain = args.domain.replace("http://", "").replace("https://", "").replace("www.", "").strip("/")

    print("-" * 50)
    print(f"[*] Starting Subdomain Scan for: {domain}")
    print("-" * 50)

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for sub in DEFAULT_SUBDOMAINS:
                executor.submit(check_subdomain, domain, sub)
    except KeyboardInterrupt:
        print("\n[*] Scan canceled by user.")
        sys.exit()

    print("-" * 50)
    print("[*] Scan completed.")

if __name__ == "__main__":
    main()