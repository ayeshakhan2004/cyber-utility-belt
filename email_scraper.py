import urllib.request
import urllib.error
import re
import argparse
import sys

def scrape_emails(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    print(f"[*] Fetching HTML from: {url}")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8', errors='ignore')

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        emails = set(re.findall(email_pattern, html_content))

        print("-" * 40)
        if emails:
            print(f"[+] Found {len(emails)} unique email(s):")
            for email in sorted(emails):
                print(f"    -> {email}")
        else:
            print("[-] No email addresses found on this page.")
        print("-" * 40)

    except urllib.error.URLError as e:
        print(f"[-] Network Error: Could not reach the URL. ({e.reason})")
    except ValueError:
        print("[-] Invalid URL format.")
    except KeyboardInterrupt:
        print("\n[*] Scraper stopped by user.")
        sys.exit()

def main():
    parser = argparse.ArgumentParser(description="OSINT Web Email Scraper")
    parser.add_argument("target", help="The URL or domain to scrape (e.g., example.com)")
    args = parser.parse_args()

    scrape_emails(args.target)

if __name__ == "__main__":
    main()