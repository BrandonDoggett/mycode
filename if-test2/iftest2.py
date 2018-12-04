#!/usr/bin/env python3

# Lab 14 - IPv4 Testing with if
# Written by Brandon Doggett

# Set the var
ipchk = input('Apply an IP address: ')

# Check the var with an if statement
if ipchk == '192.168.70.1':
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif ipchk:
    print('Looks like the IP address was set: ' + ipchk)
else:
    print('You did not provide input.')