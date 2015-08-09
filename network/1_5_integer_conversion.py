#!/usr/bin/env python
# Chapter 1, Sockets, IPv4, and Simple Client/Server Programming
# Python Network Programming Cookbook by Dr. M. O. Faruque Sarker,  Packt Publishing, 2014

import socket

# Page 14
# Listing 1.5 shows integer_conversion as follows:
def convert_integer():
    print("--- Converting integers to and from host to network byte order ---")	
    data = 1234
    # 32-bit
    print "Original: %s => Long host byte order: %s, Network byte order: %s" \
        %(data, socket.ntohl(data), socket.htonl(data))
    # 16-bit
    print "Original: %s => Short host byte order: %s, Network byte order: %s" \
        %(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()

