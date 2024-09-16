from scapy.all import sniff, conf
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine the protocol type (TCP, UDP, ICMP)
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "Other"
        
        # Print the packet details
        print(f"Source: {ip_src} -> Destination: {ip_dst} | Protocol: {protocol}")

        # Print Payload data (if any)
        if packet[IP].payload:
            payload = packet[IP].payload
            print(f"Payload: {bytes(payload)}\n")

# List available network interfaces
print(f"Available Interfaces: {conf.ifaces}")
selected_iface = input("Enter the network interface (e.g., eth0, wlan0): ")

# Use Layer 3 socket for sniffing to avoid WinPcap/Npcap dependency
conf.L3socket = conf.L3socket

# Capture packets (requires admin/root privileges)
try:
    print(f"Sniffing packets on interface {selected_iface}")
    sniff(prn=packet_callback, count=10, iface=selected_iface, filter="ip")
except Exception as e:
    print(f"Error occurred: {e}")
