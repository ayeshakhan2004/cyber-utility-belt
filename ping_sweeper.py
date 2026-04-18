import subprocess
import platform
import argparse
import concurrent.futures
import sys

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    timeout_param = '-w' if platform.system().lower() == 'windows' else '-W'
    timeout_val = '1000' if platform.system().lower() == 'windows' else '1'
    
    command = ['ping', param, '1', timeout_param, timeout_val, ip]
    
    try:
        # capture_output=True manages memory handles much better on Windows
        output = subprocess.run(command, capture_output=True, text=True)
        if output.returncode == 0 and "unreachable" not in output.stdout.lower() and "failure" not in output.stdout.lower():
            print(f"[+] Active Host Found: {ip}")
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="Fast Subnet Ping Sweeper")
    parser.add_argument("subnet", help="The first 3 octets of the subnet (e.g., 192.168.1)")
    args = parser.parse_args()

    base_ip = args.subnet.strip('.')
    
    print("-" * 50)
    print(f"[*] Sweeping Subnet: {base_ip}.0/24")
    print("-" * 50)

    try:
        # Lowered max_workers to 20 to prevent Windows handle exhaustion
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for i in range(1, 255):
                ip = f"{base_ip}.{i}"
                executor.submit(ping_host, ip)
    except KeyboardInterrupt:
        sys.exit()

    print("-" * 50)
    print("[*] Sweep completed.")

if __name__ == "__main__":
    main()