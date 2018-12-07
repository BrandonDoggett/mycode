#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# function to iterate through a list of IPs
def devicereboot(iplist):
    for z in iplist:
        print('Connecting to ' + z + '.' + ' REBOOTING NOW!')

def createIPList (ipFile):
    theFile = open(ipFile,'r')
    theDict = {}
    fileLines = theFile.readlines()
    n = 0
    for i in range(len(fileLines)):
        theDict[i] = fileLines[i+1]
    print(theDict)
    

### Start our script
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices

listofip = ['0.0.0.0','1.1.1.1','2.2.2.2']
devicereboot(listofip)