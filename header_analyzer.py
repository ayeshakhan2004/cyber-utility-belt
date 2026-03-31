import urllib.request
import urllib.error

def analyze_headers(url):
    if not url.startswith('http'):
        url = 'http://' + url
        
    print(f"🔍 Analyzing headers for: {url}\n" + "-" * 45)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            
            for key, value in headers.items():
                print(f"[{key}]: {value}")
                
            print("\n🛡️ Security Header Audit:")
            print("-" * 45)
            sec_headers = [
                'Strict-Transport-Security', 
                'Content-Security-Policy', 
                'X-Frame-Options', 
                'X-Content-Type-Options'
            ]
            
            for sh in sec_headers:
                if sh in headers:
                    print(f"[+] {sh}: PRESENT ✅")
                else:
                    print(f"[-] {sh}: MISSING ❌ (Potential Vulnerability)")
                    
    except urllib.error.URLError as e:
        print(f"[-] Failed to connect: {e.reason}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    target_site = "example.com" 
    analyze_headers(target_site)