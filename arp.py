#!/usr/bin/python3
#########WRITEN BY DANIEL MAGEVSKI##########
import sys
from datetime import datetime
from scapy.all import *


try:
    interface = input("\n[*] Set interface: ")
    print("[*] Ex:192.168.0.0/24")
    ips = input("[*] Set IP RANGE or Network: ")
except KeyboardInterrupt:
    print("\n user aborted!")
    sys.exit()

print("Scanning...")
start_time = datetime.now()

conf.verb = 0

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface=interface,inter=0.1)

print("\n\tMAC\t\tIP\n")

for snd,rcv in ans:
    print(rcv.sprintf("%Ether.src% - %ARP.psrc%"))
stop_time = datetime.now()
total_time = stop_time - start_time
print("\n[*] Scan completo!")
print("[*] Scan Duration: %s" %(total_time))
