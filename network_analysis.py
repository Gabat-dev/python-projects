from scapy.all import rdpcap, IP, TCP, UDP, DNS
from collections import Counter
import pandas as pd
from datetime import datetime
def analyze_pcap(filename):
    print(f"[*] loading PCAP: {filename}")
    packets = rdpcap(filename)
    print(f"[+] loaded {len(packets)} packets\n")
    ip_sources = []
    ip_destination = []
    protocols = []
    dns_queries = []
    print("[*] parsing packets ...")
    for pkt in packets:
        if IP in pkt:
    ip_sources.append(pkt[IP].src)
    ip_destination.append(pkt[IP].dst)

if TCP in pkt:
        protocols.append("TCP")
        ports.append(pkt[TCP].dport)
    elif UDP in pkt:
        protocols.append("UDP")
        ports.append(pkt[UDP].dport)
if DNS in pkt and pkt[DNS].qd:
    try:
        query = pkt[DNS].qd.qname.decode()
        dns_queries.append(query)
 except:
    pass
else:
    protocols.append("other")
    ports.append(None)
    print("=" * 50)
    print("TRAFFIC ANALYSIS REPORT")
    print("=" * 50)

    print("\n[1] TOP 5 SOURCE IPs")
    for ip, count in Counter(ip_sources).most_common(5):
        print(f"{ip:<20} {count} packets")

print("\n[2] TOP 5 DESTINATION IPS:")
for ip, count in Counter(ip_sources).most_common(5):
    print(f"{ip:<20} {count} packets")

print("\n[3] PROTOCOL BREAKDOWN:")
for proto, count in Counter(protocols).most_common():
    pct = (count / len(protocols)) * 100
    print(f"{proto:<10} {count} packets ({pct:.if}%)")
    24283076


