#!/usr/bin/env python3

# Lab 15 - Writing your own if-logic script
# Written by Brandon Doggett

score = int(input('Please enter a grade: '))

if score >= 90:
    lgrade = 'A'
elif score >= 80:
    lgrade = 'B'
elif score >= 70:
    lgrade = 'C'
elif score >= 60:
    lgrade = 'D'
else:
    lgrade = 'F'

print('The letter grade is ' + lgrade + '.')