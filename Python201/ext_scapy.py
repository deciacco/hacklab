#!/usr/bin/env python3
import os
from scapy.all import *

curr_dir = os.path.dirname(os.path.realpath(__file__))

"""
ip_layer = IP(dst="247ctf.com")
icmp_layer = ICMP()
packet = ip_layer / icmp_layer
r = send(packet)

print(packet.show())
#can call wireshark directly
#wireshark(packet)
"""
#arp scan

#arping("192.168.31.0/24")
"""
IFACES.show()

#ARP Scan
#*****************************************************************
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.31.0/24"), timeout=5, iface=IFACES.dev_from_index(11), verbose=True)
for i in ans:
    print(i[1].psrc)
"""
SYN = 0x02
RST = 0x04
ACK = 0x10


"""
#TCP Handshake Scanner
#****************************************************************
for port in [22, 80, 139, 443, 445, 8080]:
    tcp_connect = sr1(IP(dst="247ctf.com")/TCP(sport=RandShort(), dport=port, flags="S"), timeout=1, verbose=False)
    if tcp_connect and tcp_connect.haslayer(TCP):
        response_flags = tcp_connect.getlayer(TCP).flags
        if response_flags == (SYN + ACK):
            snd_rst = send(IP(dst="247ctf.com")/TCP(sport=RandShort(), dport=port, flags="AR"), verbose=False)
            print("{} is open!".format(port))
        elif response_flags == (RST + ACK):
            print("{} is closed!".format(port))
    else:
        print("{} is closed!".format(port))
"""

"""
#Packet Sniffing
#****************************************************************
from scapy.layers.http import HTTPRequest

def process(packet):
    if packet.haslayer(HTTPRequest):
        print(packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode())

sniff(filter="port 80", prn=process, store=False, iface=IFACES.dev_from_index(11))

"""

#Load pcap file and analyze it
#****************************************************************
scapy_cap = rdpcap(os.path.join(curr_dir, "error_reporting.pcap"))
for packet in scapy_cap:
    if packet.getlayer(ICMP):
        print(packet.load)
        
    