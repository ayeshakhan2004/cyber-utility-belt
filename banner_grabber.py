import socket
import argparse

def grab_banner(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        
        print(f"[*] Connecting to {target_ip}:{port}...")
        s.connect((target_ip, port))
        
        # If it's a web port, we need to poke it with an HTTP request to get it to talk
        if port in [80, 443, 8080]:
            s.send(b"HEAD / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")

        # Receive up to 1024 bytes of the banner
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        
        if banner:
            print("-" * 50)
            print(f"[+] Banner caught on port {port}:")
            print(banner)
            print("-" * 50)
        else:
            print(f"[-] Connected to port {port}, but no banner was received.")
        
        s.close()

    except socket.timeout:
        print(f"[-] Connection to port {port} timed out.")
    except ConnectionRefusedError:
        print(f"[-] Connection to port {port} was refused (port is likely closed).")
    except socket.gaierror:
        print("[-] Error resolving the target hostname.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Network Banner Grabber")
    parser.add_argument("target", help="The IP address or domain to target (e.g., scanme.nmap.org)")
    parser.add_argument("port", type=int, help="The specific port to grab a banner from (e.g., 22 or 80)")
    args = parser.parse_args()

    grab_banner(args.target, args.port)

if __name__ == "__main__":
    main()