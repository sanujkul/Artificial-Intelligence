from graphics import *
import time;

n = 8; # number  of queens
#emptyPlaces = [];
#Following is position where queens will be placed
queensPositions = ["",(1,2), (2,3), (3,2), (4,3), (5,2), (6,3), (7,2), (8,3),];
queensPColors = ["",'red', 'blue', 'yellow', 'green', 'orange', 'pink', 'magenta', 'violet'];

grid_side = 50;
win = GraphWin("8 queens", grid_side*n, grid_side*n);

##################################################################
##################################################################
# These are graphics functions
##################################################################
##################################################################
def initializeGame():
   """
   This function initializes the board with walls and place the pacman at start and
   marks the end position.

   """
   #Coloring the background black
   win.setBackground(color_rgb(0,0,0)); 

   # Creating dots in the middle of each square
   for i in range(1,n+1):
      for j in range(1,n+1):
         center = Point((i-0.5)*grid_side,(j-0.5)*grid_side);
         cir = Circle(center, 1);
         cir.setFill(color_rgb(255,255,255))
         cir.draw(win)

   #Drawing the Queens;
   i = 1;
   for a in queensPositions[1:]:
      pt1 = Point((a[0]-1)*grid_side, (a[1]-1)*grid_side)
      pt2 = Point((a[0])*grid_side, (a[1])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(queensPColors[i]);
      i += 1;
      rect1.draw(win)

##################################################################
##################################################################
      
def colorNode(node, color):
   pt1 = Point((node[0]-1)*grid_side, (node[1]-1)*grid_side)
   pt2 = Point((node[0])*grid_side, (node[1])*grid_side)
   rect1 = Rectangle(pt1, pt2)
   rect1.setFill(color)
   rect1.draw(win)

##################################################################
##################################################################
      # Below functions are AI related functions
##################################################################
##################################################################
def findNextMove(curHVal):
   """
   This function will find next best move based on where
   heuristic value decreases sharply
   It can move any one of n queens
   """
   minHCalc = curHVal;     #Initializing to curHVal
   minPlayerMove = 0;      #Initializing
   minNewPosition = (0,0);
   
   for queen in range(1,n+1): #i.e. [1,...,n]
      #1. Finding all possible mover for this
      queenMoves = findPlacesToMove(queen);
      tempQueensPositionList = [x for x in queensPositions];
      for move in queenMoves:
         #Change the position of this queen
         tempQueensPositionList[queen] = move;
         #Calculate the heuristic val
         hVal = heuristicValueOfPosition(tempQueensPositionList);
         #print("in min: hval is {} for {}".format(hVal, tempQueensPositionList))
         if (hVal < minHCalc):
            minHCalc = hVal;
            minPlayerMove = queen;
            minNewPosition = move;
         #print("\t\t new return vars are")   
   #print("hVal we are sending back is {}".format(minHCalc));
   if minHCalc < curHVal:
      return (minPlayerMove, minNewPosition, minHCalc)
   else:
      return -1; #That we have reached local minima

##################################################################
##################################################################

def heuristicValueOfPosition(tempQueenPosList):
   """
   Heuristic is no. of pairs of queens attacking each other
   in current positions scenario
   """
   hVal = 0;
   
   for q1 in range(1,n): #i.e. [1,...,n-1]
      q1X = tempQueenPosList[q1][0];
      q1Y = tempQueenPosList[q1][1];
      for q2 in range(q1+1,n+1): #i.e. [i,i+1, ....., n]
         q2X = tempQueenPosList[q2][0];
         q2Y = tempQueenPosList[q2][1];
         if (q1X == q2X) or (q1Y == q2Y) or (abs(q1X-q2X) == abs(q1Y-q2Y)):
            #then q1 and q2 are not attacking each other
            hVal += 1;
            #print("hVal is {} since {} <-> {}".format(hVal, q1, q2))
   return hVal;
      
##################################################################
##################################################################
      
def findPlacesToMove(queenNumber):
   """
   #This function will find location of all the plasces a queen
   can move to.
   """
   movesDestinations = [];
   currentQueenPos = queensPositions[queenNumber];
   #1.Search horizontally:
      # Searching in +ve direction
   for x in range(1,n): #i.e 1,2,3
      if (currentQueenPos[0]+x <= n) and ((currentQueenPos[0]+x, currentQueenPos[1]) not in queensPositions):
         movesDestinations.append((currentQueenPos[0]+x, currentQueenPos[1]));
      else:
         break;

      # Searching in -ve direction
   for x in range(1,n): #i.e -1,-2,-3
      if (currentQueenPos[0]-x >= 1) and ((currentQueenPos[0]-x, currentQueenPos[1])) not in queensPositions:
         movesDestinations.append((currentQueenPos[0]-x, currentQueenPos[1]));
      else:
         break;

   #2.Search vertically:
      # Searching in +ve direction
   for y in range(1,n): #i.e 1,2,3
      if (currentQueenPos[1]+y <= n) and ((currentQueenPos[0], currentQueenPos[1]+y) not in queensPositions):
         movesDestinations.append((currentQueenPos[0], currentQueenPos[1]+y));
      else:
         break;

      # Searching in -ve direction
   for y in range(1,n): #i.e -1,-2,-3
      if (currentQueenPos[1]-y >= 1) and ((currentQueenPos[0], currentQueenPos[1]-y)) not in queensPositions:
         movesDestinations.append((currentQueenPos[0], currentQueenPos[1]-y));
      else:
         break;

   #3.Search diagonally 1:
      # Searching in +ve direction
   for i in range(1,n): #i.e 1,2,3
      if (currentQueenPos[0]+i <= n) and (currentQueenPos[1]+i <= n) and ((currentQueenPos[0]+i, currentQueenPos[1]+i) not in queensPositions):
         movesDestinations.append((currentQueenPos[0]+i, currentQueenPos[1]+i));
      else:
         break;

      # Searching in -ve direction
   for i in range(1,n): #i.e -1,-2,-3
      if (currentQueenPos[0]-i >= 1) and (currentQueenPos[1]-i >= 1) and ((currentQueenPos[0]-i, currentQueenPos[1]-i)) not in queensPositions:
         movesDestinations.append((currentQueenPos[0]-i, currentQueenPos[1]-i));
      else:
         break;

   #4.Search diagonally 2:
      # Searching in +ve x direction
   for i in range(1,n): #i.e 1,2,3
      if (currentQueenPos[0]+i <= n) and (currentQueenPos[1]-i >= 1) and ((currentQueenPos[0]+i, currentQueenPos[1]-i) not in queensPositions):
         movesDestinations.append((currentQueenPos[0]+i, currentQueenPos[1]-i));
      else:
         break;

      # Searching in -ve direction
   for i in range(1,n): #i.e -1,-2,-3
      if (currentQueenPos[0]-i >= 1) and (currentQueenPos[1]+i <= n) and ((currentQueenPos[0]-i, currentQueenPos[1]+i)) not in queensPositions:
         movesDestinations.append((currentQueenPos[0]-i, currentQueenPos[1]+i));
      else:
         break;
   

   return movesDestinations;

##################################################################
##################################################################
def ai():
   curHVal = heuristicValueOfPosition(queensPositions);
   while True:
      time.sleep(1);
      queenNewPos = findNextMove(curHVal); #It returns (queen, new pos, hVal)
      if(queenNewPos == -1):
         print("Reached global minima, can make more moves !");
         break;

      colorNode(queensPositions[queenNewPos[0]], 'black'); #turn old position black
      
      queensPositions[queenNewPos[0]] = queenNewPos[1];

      colorNode(queensPositions[queenNewPos[0]], queensPColors[queenNewPos[0]]); #turn old position black
      
      curHVal = queenNewPos[2];
      print("Current Board position with {} is : {}".format(curHVal,queensPositions));
      if(curHVal == 0):
         print("We have achieved our Goal!");
         break;
   print("Final positionsa are {}".format(queensPositions));
      
##################################################################
##################################################################

def main():
   initializeGame();
   ai();
   #print(findPlacesToMove(1));
   #curHVal = heuristicValueOfPosition(queensPositions);
   #print(curHVal);
   #print(findNextMove(curHVal));
   #print(heuristicValueOfPosition(["",(1,1), (2,2), (3,1), (4,2)]));
   #print(heuristicValueOfPosition(['', (1, 1), (2, 4), (3, 1), (4, 2)]));
   
main();
