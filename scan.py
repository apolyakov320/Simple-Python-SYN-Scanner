from scapy.all import IP, TCP, sr1, send
import logging
import socket

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def get_banner(target_ip, port):
    """Attempt to grab the service banner from an open port."""
    try:
        # Create a standard TCP socket
        s = socket.socket()
        s.settimeout(2)  # Wait 2 seconds for a response
        s.connect((target_ip, port))
        
        # Some services send a banner immediately; others need a prompt
        # We try to receive first
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "No banner available"

def syn_scan(target_ip, ports):
    if not target_ip:
        print("[!] Error: No target IP.")
        return

    print(f'[*] Scanning {target_ip}...')

    for port in ports:
        packet = IP(dst=target_ip)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            print(f'[-] Port {port:5}: Filtered')
        elif response.haslayer(TCP):
            flags = response.getlayer(TCP).flags
            
            if flags & 0x12:
                # Port is Open - Now grab the banner
                banner = get_banner(target_ip, port)
                print(f'[+] Port {port:5}: OPEN | Banner: {banner}')
                
                # Send RST to close the Scapy-initiated half-open connection
                send(IP(dst=target_ip)/TCP(dport=port, flags='R'), verbose=0)
            
            elif flags & 0x14:
                print(f'[-] Port {port:5}: Closed')

if __name__ == "__main__":
    target = "10.245.223.223"  # Replace with your test VM IP
    common_ports = [21, 22, 80, 443, 3389]
    syn_scan(target, common_ports)
