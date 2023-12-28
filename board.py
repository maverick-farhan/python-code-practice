#!/usr/bin/env python3
import sys
theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}
def printBoard(board):
    print(board['top-L']+"|"+board['top-M']+"|"+board['top-R'])
    print("--++--")
    print(board['mid-L']+"|"+board['mid-M']+"|"+board['mid-R'])
    print("--++--")
    print(board['low-L']+"|"+board['low-M']+"|"+board['low-R'])


def posMark(string):
        print('Where to insert | Options:'+ str(theBoard.keys()))
        pos = input()
        if(theBoard[pos]!=string):
            for pos_option in theBoard.keys():
                if(pos==pos_option):
                    theBoard[pos]=string
        else:
            print('Already filled. Fill Again')
            print('Where to insert | Options:'+ str(theBoard.keys()))
            pos = input()
            if(pos==pos_option and theBoard[pos]!=string):
                theBoard[pos]=string

             # while theBoard[pos_option]!=string

def playerX():
    print("PLayer X turn")
    putX = input()
    if(putX=='X' or putX=='x'):
        posMark(putX.upper())
        winner(putX.upper())
def playerO():
    print("PLayer O turn")
    putO = input()
    if(putO=='O' or putO=='o'):
         posMark(putO.upper())
         winner(putO.upper())

def winner(mark):
    if theBoard['top-L']==mark and theBoard['top-M']==mark and theBoard['top-R']==mark or theBoard['mid-L']==mark and theBoard['mid-M']==mark and theBoard['mid-R']==mark or theBoard['low-L']==mark and theBoard['low-M']==mark and theBoard['low-R']==mark or theBoard['top-L']==mark and theBoard['mid-L']==mark and theBoard['low-L']==mark or theBoard['top-M']==mark and theBoard['mid-M'] and theBoard['low-M'] or theBoard['top-R'] and theBoard['mid-R']==mark and theBoard['low-R']==mark or theBoard['top-L'] and theBoard['mid-M']==mark and theBoard['low-R']==mark or theBoard['top-R'] and theBoard['mid-M']==mark and theBoard['low-L']==mark :
        if mark=='X':
            print('congratulation X won this match')
            print("Press Enter to exit or 'e' to continue")
            close = input()
            if(close==''):
                sys.exit()
        elif mark=='O':
            print('congratulation O won this match' )
            print("Press Enter to exit or 'e' to continue")
            close = input()
            if(close==''):
                sys.exit()
        else:
            print('Draw')
            print("Press Enter to exit or 'e' to continue")
            close = input()
            if(close==''):
                sys.exit()
def game_runner():
    fields_count = 0
    while fields_count<=9:
        playerX()
        printBoard(theBoard)
        playerO()
        printBoard(theBoard)
        fields_count+=1

game_runner()
