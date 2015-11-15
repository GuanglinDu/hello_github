#!/usr/bin/env python
# Chapter 1, Sockets, IPv4, and Simple Client/Server Programming
# Python Network Programming Cookbook by Dr. M. O. Faruque Sarker,  Packt Publishing, 2014

import socket
from binascii import hexlify # imports a function only

# Page 12
# Listing 1.3 shows ip4_address_conversion as follows:
def convert_ip4_address():
    print("--- Converting an IPv4 address to different formats ---")
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        # Attention: continuation sign
        print "IP Address: %s => Packed: %s, Unpacked: %s" \
    % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)

if __name__ == '__main__':
    convert_ip4_address()

