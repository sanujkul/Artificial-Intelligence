#!/usr/bin/python3
import time
import random

board = ["", "", "", "", "", "", "", "", ""]

players = ["X" , "0"];

available = [0,1,2,3,4,5,6,7,8]; #All board positions available in the beginning

def displayBoard():
    print("__________________________________________________")
    for i in range(3): 
        print('|\t {} \t | \t {} \t | \t {} \t |'.format(board[i*3], board[(3*i)+1], board[(3*i)+2]));       
        print("|________________|_______________|_______________|")

def nextTurn(currentPlayer):
    #We chose a random available position and also remove it from list
    index = random.choice([x for x in range(0,len(available))])
    pos = available.pop(index);
    board[pos] = players[currentPlayer];

def checkWinner():
    winner = None;

    #row winner:
    for i in range(3):
        if(board[3*i] == board[(3*i) + 1] == board[(3*i) + 2] != ""):
            winner = board[3*i];
            break;

    #column winner:
    for i in range(3):
        if(board[i] == board[i+3] == board[i+6] != ""):
            winner = board[i];
            break;
        
    #diagonal winner
    if(winner is None):
        if(board[0] == board[4] == board[8] != ""):
            winner = board[0];
        elif(board[2] == board[4] == board[6] != ""):
            winner = board[2];

    return winner;

        

def play():
    currentPlayer = random.choice([0,1]);
    for i in range(9):
        if (i%2 == 0): # CPU will play
            nextTurn(currentPlayer);
        else:
            yourMove = input("Please choose available positions ({}) : ".format([(x+1) for x in available]));
            yourMove = int(yourMove) - 1; #As our indexing started from 0
            available.remove(yourMove);
            board[yourMove] = players[currentPlayer]

        currentPlayer = (currentPlayer+1)%2;
        displayBoard();
        winner = checkWinner();
        if(winner is not None):
            print("Winner is {}".format(winner));
            break;
        time.sleep(1);
            
    if(checkWinner() is None and len(available)==0):
        print("GAME TIED");


play();
        
