#!/usr/bin/env python3

# Lab 23 - for loops and range()
# Written by Brandon Doggett

# Initialize variables
x = int(input("Enter a number: "))
f = 1

# For loop
for i in range(1, x+1):
    f = f * i

# Final print statement
print(str(x) + '! = ' + str(f))