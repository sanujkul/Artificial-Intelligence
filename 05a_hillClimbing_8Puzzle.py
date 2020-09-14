from graphics import *
import time;

n = 3; # number  of queens

# 0 --> is blank box, rest are numbers at those indexes
# and indexing starts from 1 (instead of zero)
positions = ["",["",1,5,2],["",0,4,3],["",7,8,6]];

curBlank = (0,0); #index of 0 or empty node
goalPositions = [(3,3), (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)];

#These colors are in sequence for 1 to 8
numColors = ['black','red', 'skyblue', 'yellow', 'green', 'orange', 'pink', 'magenta', 'violet'];

grid_side = 100;
win = GraphWin("8 squares", grid_side*n, grid_side*n);
#Coloring the background black
win.setBackground(color_rgb(0,0,0));
   
##################################################################
##################################################################
# These are graphics functions
##################################################################
##################################################################
def updateBoard():
   """
   This function updates the GUI of board

   """
   #Drawing the initial board positions;
   for y in range(1, n+1): #1,2,3
      for x in range(1, n+1):
         val = positions[y][x];
         colorNode((x,y), numColors[val])
         label = Text(Point((x-0.5)*grid_side, (y-0.5)*grid_side),val);
         label.setSize(30)
         label.draw(win)
   

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
   heuristic value decreases sharply. It will move blank to all possible moves
   """
   minHCalc = curHVal;     #Initializing to curHVal
   minNewPosition = (0,0); #Initializing it

   tempBoardPositions = [x for x in positions]
   
   for move in findPlacesToMove():
      #Move number to blank
      tempBoardPositions[curBlank[0]][curBlank[1]] = tempBoardPositions[move[0]][move[1]];
      #Move blank to new move position
      tempBoardPositions[move[0]][move[1]] = 0;
      
      hVal = heuristicValueOfPosition(tempBoardPositions);
      if(hVal < minHCalc):
         minHCalc = hVal;
         minNewPosition = move;
         
      #Resetting board to what it was before this move
      tempBoardPositions[move[0]][move[1]] = tempBoardPositions[curBlank[0]][curBlank[1]]
      #tempBoardPositions[curBlank[0]][curBlank[1]] = 0;

      print("After calc -- {}".format(positions))
      
   if minHCalc < curHVal:
      return (minNewPosition, minHCalc)
   else:
      return -1; #That we have reached local minima

##################################################################
##################################################################

def heuristicValueOfPosition(currPositions):
   """
   Heuristic is sum of manhattan distance of misplaced nodes
   """
   hVal = 0;

   for y in range(1, n+1): #1,2,3
      for x in range(1, n+1):
         val = currPositions[y][x];
         if ((val == 0) or (goalPositions[val] == (y,x))): #val 0 means blank
            continue;
         else:
            hVal += abs(y-goalPositions[val][0]) + abs(x-goalPositions[val][1])

   return hVal;      
##################################################################
##################################################################
      
def findPlacesToMove():
   """
   #This function will find location of all the plasces a blank
   can move to and replace to.
   curBlank can move to up, down, left right (if available)
   """
   movesDestinations = [];
   
   curY = curBlank[0];
   curX = curBlank[1];

   if(curY-1 >= 1): #UP
      movesDestinations.append((curY-1, curX));
   if(curY+1 <= n): #DOWN
      movesDestinations.append((curY+1, curX));
   if(curX-1 >= 1): #LEFT
      movesDestinations.append((curY, curX-1));
   if(curX+1 <= n): #RIGHT
      movesDestinations.append((curY, curX+1));
   
   return movesDestinations;

##################################################################
##################################################################
def ai():
   global curBlank;
   for y in range(1,n+1):
      for x in range(1,n+1):
         if positions[y][x] == 0:
            curBlank = (y,x);
         
         
   curHVal = heuristicValueOfPosition(positions);
   
   while True:
      time.sleep(1);
      
      blankNewPos = findNextMove(curHVal); #It returns (new pos, hVal)
      if(blankNewPos == -1):
         print("Reached global minima, can make more moves !");
         break;
      move = blankNewPos[0];
      print("Recommended move is {} because of h val = {}".format(move,blankNewPos[1] ))
      #Update with new minimun H val positions
      #Move number to blank
      positions[curBlank[0]][curBlank[1]] = positions[move[0]][move[1]];
      #Move blank to new move position
      positions[move[0]][move[1]] = 0;
      curBlank = move;
      updateBoard();
      
      curHVal = blankNewPos[1];
      
      print("Current Board position with {} is : {}".format(curHVal,positions));
      if(curHVal == 0):
         print("We have achieved our Goal!");
         break;
      
##################################################################
##################################################################

def main():
   updateBoard();
   print(heuristicValueOfPosition(positions))
   ai();
   
   #print(findPlacesToMove());
   #print(findNextMove(1))
   print(findPlacesToMove());
main();
