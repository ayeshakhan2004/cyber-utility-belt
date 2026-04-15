import urllib.request
import urllib.error
import argparse
import concurrent.futures
import sys

DEFAULT_WORDLIST = [
    "admin", "login", "dashboard", "api", "backup", "db", 
    "config", "test", "dev", "staging", "robots.txt", "sitemap.xml",
    ".git", ".env", "wp-admin", "wp-login.php", "old", "tmp"
]

def check_directory(base_url, path):
    if not base_url.endswith('/'):
        base_url += '/'
        
    target_url = base_url + path
    
    try:
        req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=3)
        
        if response.status == 200:
            print(f"[+] FOUND: {target_url}")
            
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print(f"[*] FORBIDDEN (Exists, but blocked): {target_url}")
    except urllib.error.URLError:
        pass
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Web Directory Scanner")
    parser.add_argument("url", help="The base URL to scan (e.g., https://example.com)")
    args = parser.parse_args()

    target_url = args.url
    if not target_url.startswith('http'):
        target_url = 'https://' + target_url

    print("-" * 50)
    print(f"[*] Starting Directory Scan on: {target_url}")
    print("-" * 50)

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for path in DEFAULT_WORDLIST:
                executor.submit(check_directory, target_url, path)
    except KeyboardInterrupt:
        print("\n[*] Scan canceled by user.")
        sys.exit()

    print("-" * 50)
    print("[*] Scan completed.")

if __name__ == "__main__":
    main()