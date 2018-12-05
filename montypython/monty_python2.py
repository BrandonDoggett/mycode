#!/usr/bin/env python3

# Lab 18 - Using while, if, elif, else
# Written by Brandon Doggett

round = 0

while(True):
    round += 1
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = str.lower(input())
    if answer == 'brian':
        print('Correct')
        break
    elif answer == 'shrubbery':
        print('You gave the super secret answer!')
        break
    elif round == 3:
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')
