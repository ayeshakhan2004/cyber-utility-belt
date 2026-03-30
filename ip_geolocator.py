import urllib.request
import json

def track_ip(ip_address):
    """Fetches geolocation data for a target IP address."""
    url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
        if data.get("status") == "success":
            print(f"🌍 Target IP : {data.get('query')}")
            print(f"📍 Location  : {data.get('city')}, {data.get('country')}")
            print(f"🏢 ISP       : {data.get('isp')}")
            print(f"🌐 Timezone  : {data.get('timezone')}")
        else:
            print(f"[-] Failed to locate IP: {data.get('message')}")
            
    except Exception as e:
        print(f"[-] Connection Error: {e}")

if __name__ == "__main__":
    print("🔍 OSINT IP Tracker Initialized")
    print("-" * 35)
    
    test_ip = "8.8.8.8"
    track_ip(test_ip)