import urllib.request
import urllib.error

def unshorten_url(short_url):
    if not short_url.startswith(('http://', 'https://')):
        short_url = 'http://' + short_url
        
    print(f"🔗 Analyzing link: {short_url}\n" + "-" * 40)
    
    try:
        req = urllib.request.Request(
            short_url, 
            headers={'User-Agent': 'Mozilla/5.0'}, 
            method='HEAD'
        )
        
        with urllib.request.urlopen(req, timeout=5) as response:
            final_url = response.geturl()
            
        if final_url != short_url:
            print(f"[+] REDIRECT DETECTED 🚩")
            print(f"[+] Final Destination: {final_url}")
        else:
            print(f"[-] No redirect. Final URL: {final_url}")
            
    except urllib.error.URLError as e:
        print(f"[-] Connection failed: {e.reason}")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    test_url = "http://bit.ly/3m4aWjT" 
    unshorten_url(test_url)