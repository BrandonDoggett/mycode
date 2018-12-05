#!/usr/bin/env python3

# Lab 17 - Python Dictionaries
# Written by Brandon Doggett

# Create a dictionary
switch = {'hostname':'sw1','ip':'10.0.1.1','version':'1.2','vendor':'cisco'}

# Display parts of the dictionary
print(switch['hostname'])
print(switch['ip'])

# Request a 'fake' key
# print(switch['lynx'])

# Request a 'fake key with .get() method
print('First test - .get()')
print(switch.get('lynx'))

print('Second test - .get()')
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print('Third test - .get()')
print(switch.get('version'))

print('Fourth test - .keys()')
print(switch.keys())

print('Fifth test - .values()')
print(switch.values())

print('Sixth test - .pop()')
switch.pop('version') # removes this key and value pair
print(switch.keys())
print(switch.values())

print('Seventh test - ADD a new value')
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())

print('Eighth test - ADD a new value')
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())