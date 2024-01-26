#!/usr/bin/env python3
#Guess the number game in Python
from random import randint as rint
def guessTheNumber():
    flag = True
    random = rint(1,20)
    print('Im thinking of a number between 1-20')
    count = 0
    while flag:
        count+=1
        print('Take a guess')
        guess = int(input())
        if(guess>random):
            print('Your guess is too high')
        elif(guess<random):
            print('Your guess is too low')
        else:
            print('Congrats you guess is correct with '+ str(guess) + ' in '+ str(count)+ ' guesses')
            flag=False

guessTheNumber()

