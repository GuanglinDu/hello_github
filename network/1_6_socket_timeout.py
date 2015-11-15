#!/usr/bin/env python
# Chapter 1, Sockets, IPv4, and Simple Client/Server Programming
# Python Network Programming Cookbook by Dr. M. O. Faruque Sarker,  Packt Publishing, 2014

import socket

# Page 12
# Listing 1.6 on page 15 shows socket_timeout as follows:
def test_socket_timeout():
    print("--- Setting and getting the default socket timeout ---")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout: %s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout: %s" %s.gettimeout()

if __name__ == '__main__':
    test_socket_timeout()

