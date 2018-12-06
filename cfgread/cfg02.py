#!/usr/bin/env python3
## create file object in "r"ead mode

print('Please provide a filename: ')
cFilename = input()

configfile = open(cFilename, 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## display number of lines
print('Number of lines: ' + str(len(configlist)))

## Always close your file
configfile.close()
