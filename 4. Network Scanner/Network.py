import scapy.all as scapy


def scan(ip):
	scapy.arping(ip)
	
scan("192.168.6.1/24")
