#!/usr/bin/env python
# Chapter 1, Sockets, IPv4, and Simple Client/Server Programming
# Python Network Programming Cookbook by Dr. M. O. Faruque Sarker,  Packt Publishing, 2014

import socket

# Page 13
# Listing 1.4 shows finding_service_name as follows:
def find_service_name():
    print("--- Finding a service name, given the port and protocol ---")	
    protocolname = 'tcp'
    for port in [80, 25, 443]: # iterates over an array
        print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
    
    # A UDP protocol port test
    print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))

if __name__ == '__main__':
    find_service_name()

