#!/usr/bin/env python3

# Written by Brandon Doggett
# Lab 12 - Lists of lists

list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)
list1.extend(['juniper'])
print(list1)
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print(list1[4])
print(list1[4][0])

# Challenge 
animals = ['Fox','Fly','Ant','Bee','Cod','Cat','Dog','Yak','Cow','Hen','Koi','Hog','Jay','Kit']
print(animals)
print(animals[0], animals[1])