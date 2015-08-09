#!/usr/bin/env python
# Chapter 1, Sockets, IPv4, and Simple Client/Server Programming
# Python Network Programming Cookbook by Dr. M. O. Faruque Sarker,  Packt Publishing, 2014

import socket

# Page 9
# Listing 1.1 on shows how to get our machine info, as follows:
def print_machine_info():
    print("--- Printing your machine's name and IPv4 address ---")
    host_name = socket.gethostname() # static method
    ip_address = socket.gethostbyname(host_name) # static method
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address

if __name__ == '__main__':
    print_machine_info()

