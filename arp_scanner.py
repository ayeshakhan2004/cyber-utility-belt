import scapy.all as scapy
import argparse
import sys

def get_arguments():
    parser = argparse.ArgumentParser(description="🦇 Cyber Utility Belt - ARP Scanner")
    parser.add_argument("-t", "--target", dest="target", required=True)
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    return parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast_frame / arp_request
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        
    return clients_list

def print_result(results_list):
    print("\n🦇 Cyber Utility Belt - Active Hosts Discovered")
    print("--------------------------------------------------")
    print("IP Address\t\tMAC Address")
    print("--------------------------------------------------")
    
    if not results_list:
        print("No hosts found. Ensure you are scanning a valid local subnet.")
        return

    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    try:
        options = get_arguments()
        print(f"[*] Scanning {options.target} via ARP...")
        scan_result = scan(options.target)
        print_result(scan_result)
        
    except KeyboardInterrupt:
        print("\n[!] Scan aborted by user.")
        sys.exit(0)
    except PermissionError:
        print("\n[!] Permission Denied. Please run this script as root/Administrator.")
        sys.exit(1)