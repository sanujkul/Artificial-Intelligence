#!/usr/bin/python3
import time
import random
import math


board = ["", "", "", "", "", "", "", "", ""]

players = ["X" , "0"];
scores = {"X":1 , "0":-1 , "tie":0}; #X-->Maximizing player, 0-->Minimizing Player


available = [0,1,2,3,4,5,6,7,8]; #All board positions available in the beginning

##########################################################################
##########################################################################
#current player is index 0,1 for X,0 respectively
def isMaximizingPlayer(currentPlayer):
    if(currentPlayer == 0):
        return True;
    else:
        return False;
    
##########################################################################
##########################################################################

#1. We will check if someone wins,
#2. If someone wins, returns winner's score
#3. else checking for maximizing players

def minimax(curBoard, availablePos, depth, currentPlayer):
    winner = checkWinner(curBoard)
    if(winner is not None):
        score = scores[winner];
        return score;

    if(len(availablePos) == 0):
        return 0;           #Tie score
    
    if(isMaximizingPlayer(currentPlayer)):
        bestScore = -math.inf;
        for emptPos in availablePos:
            #1. Make a move
            curBoard[emptPos] = players[currentPlayer];    #Let's make move here
            index = availablePos.index(emptPos);
            availablePos.remove(emptPos);      #removing the available position as it is occupied
            #2. Check following moves
            score = minimax(curBoard, availablePos,depth+1, (currentPlayer+1)%2);
            #3. Undo the move, to check other moves
            curBoard[emptPos] = ""; #Emptying the board again
            availablePos.insert(index,emptPos);  #adding the available position as it is unoccupied
        
            if (score > bestScore):
                bestScore = score;
                move = emptPos;
        return bestScore;

    else:   #Player is minimzing
        bestScore = math.inf;
        for emptPos in availablePos:
            #1. Make a move
            curBoard[emptPos] = players[currentPlayer];    #Let's make move here
            index = availablePos.index(emptPos);
            availablePos.remove(emptPos);      #removing the available position as it is occupied
            #2. Check following moves
            score = minimax(curBoard, availablePos,depth+1, (currentPlayer+1)%2);
            #3. Undo the move, to check other moves
            curBoard[emptPos] = ""; #Emptying the board again
            availablePos.insert(index,emptPos);  #adding the available position as it is unoccupied
        
            if (score < bestScore):
                bestScore = score;
        return bestScore;      
##########################################################################
##########################################################################
        
#What we are doing here is:
        #1. Finding an empty spot.
        #2. Making a move there.
        #3. Calling minmax to see what is future at that move
        
def bestMove(currentPlayer):
    if(isMaximizingPlayer(currentPlayer)):
        bestScore = -math.inf;  #As Best score should be maximum for maximizing player
        isMaximizing = True;
    else:
        bestScore = math.inf;  # As Best score should be minimum for minimizing player
        isMaximizing = False;

    move = available[0];
    
    for emptPos in available:
        board[emptPos] = players[currentPlayer];    #Let's make move here

        index = available.index(emptPos);
        available.remove(emptPos);      #removing the available position as it is occupied

        score = minimax(board, available, 0, isMaximizing);

        board[emptPos] = ""; #Emptying the board again
        available.insert(index,emptPos);  #adding the available position as it is unoccupied
        
        if ( isMaximizing and score > bestScore):
            bestScore = score;
            move = emptPos;
        elif( not isMaximizing and score < bestScore):
            bestScore = score;
            move = emptPos;
            
    available.remove(move); #Best  move is no longer available
    board[move] = players[currentPlayer];    

##########################################################################
    ##########################################################################
    
def checkWinner(board):
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

##########################################################################
##########################################################################        

def play():
    print("Welcome! You are '0' and CPU is 'X'")
    currentPlayer = random.choice([0,1]); #Choose random first player

    if(currentPlayer == 0):
        print("CPU goes first");
    else:
        print("You go first");
    
    for i in range(9):
        if (currentPlayer == 0): # CPU will play
            bestMove(currentPlayer);
        else:
            while(True): #Precaution if player make illegal move
                yourMove = input("Please choose available positions ({}) : ".format([(x+1) for x in available]));
                yourMove = int(yourMove) - 1; #As our indexing started from 0
                if(yourMove in available):
                    available.remove(yourMove);
                    board[yourMove] = players[currentPlayer]
                    break;
                else:
                    print("Illegal move, please choose empty space");

        currentPlayer = (currentPlayer+1)%2;
        displayBoard();
        winner = checkWinner(board);
        if(winner is not None):
            print("Winner is {}".format(winner));
            break;
        time.sleep(0.5);
            
    if(checkWinner(board) is None and len(available)==0):
        print("GAME TIED");

##########################################################################
##########################################################################

def displayBoard():
    print("__________________________________________________")
    for i in range(3): 
        print('|\t {} \t | \t {} \t | \t {} \t |'.format(board[i*3], board[(3*i)+1], board[(3*i)+2]));       
        print("|________________|_______________|_______________|")


##########################################################################
##########################################################################

play();
        
