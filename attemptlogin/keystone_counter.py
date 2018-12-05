#!/usr/bin/env python3

loginfail = 0
loginsuccess = 0
ipflist = []
ipsplit = []

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines = keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1
        tempip = keystone_file_lines[i]
        ipsplit = tempip.split()
        if 'from' in ipsplit:
            ipflist.append(ipsplit[-1])
    if "-] Authorization failed" in keystone_file_lines[i]:
        loginsuccess += 1

print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(loginsuccess))
print('The failures were from the following IP(s): ' + str(ipflist))