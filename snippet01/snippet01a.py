#!/usr/bin/env python3

file = open('/home/student/mycode/snippet01/somelist.txt','r')

new_list = file.readlines()

print("\n".join(new_list))
print("\t".join(new_list))