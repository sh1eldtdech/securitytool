import socket 
import os
from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
import scapy.all
from scapy.all import scapy
import sys
from scapy.sendrecv import sr1
from scapy.layers.inet import ICMP, IP, TCP  
from scapy.volatile import RandShort


#Input From User
def inp(ch):
    host_inp = input("Enter Host Name/ IP Address\n")
    ip = socket.gethostbyname(host_inp)
    print(ip)
    ping = os.system("ping -c 1 " + ip)
    if ping ==0:
        if ch == 1:
            for i in range(0,65535):
                sc(ip, i)
        elif ch == 2:
            port_list = [21,22,58,80,443]
            for i in port_list:
                sc(ip, i)
        elif ch == 3:
            inp_p = input("Enter Port Number: ")
            sc(ip, int(inp_p))
        else:
            print("Invalid Input")
    else:
        print("Host is Down")    
     

#syn_scan
def sc(ip, port):
    
    open_ports = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sport = RandShort()
    pkt = sr1(IP(dst=ip)/TCP(sport = sport, dport=port, flags="S"),timeout=5)
    #print(pkt)
    print("Port Number: " + str(port))
    if pkt != None:
        if pkt.haslayer(TCP):
            if pkt[TCP].flags==20:
                print("CLosed")
            elif pkt[TCP].flags == 18:
                print(port, " | Open" )
                s.settimeout(5)
                s.connect((ip, port))
                print("Service", s.recv(1024).decode())
                
            else:
                print("Filtered")
        elif pkt.haslayer(ICMP):
                print(" ICMP Filtered")
        else:
            print("Unknown Response")
            print(pkt.summary())
    else:
        print("Unanswered")
    print(open_ports)
    '''for i in open_ports:
        banner(ip,i)'''
    
'''def banner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.settimeout(5)
    print(s.recv(1024).decode())
    s.close()'''


def main():
    print("*"*16)
    print("* Port Scanner *")
    #print("*              *")
    print("*"*16)
    print("1. SYN Scan All Ports\n2. Common Ports Scan\n3. Specific Port Scan\n4. Generate Report\n")
    ch = int(input("Enter Your Choice: "))
    inp(ch)

main()

#banner("172.217.160.238", 80)


