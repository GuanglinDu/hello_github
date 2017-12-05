#!/usr/bin/env python
# Chapter 1, Sockets, IPv4, and Simple Client/Server Programming
# Python Network Programming Cookbook by Dr. M. O. Faruque Sarker,  Packt Publishing, 2014

import socket

# Page 11
# Listing 1.2 shows how to get a remote machine's IP address as follows:
def get_remote_machine_info():
    print("--- Retrieving a remote machine's IP address ---")
    remote_host = 'www.python.org'
    #remote_host = 'www.pytgo.org' # no error due to redirection here at Beijing
    try:
        print "IP address: %s" % socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" % (remote_host, err_msg)

if __name__ == '__main__':
    get_remote_machine_info()

