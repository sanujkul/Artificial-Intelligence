from graphics import *
import time;

grid_side = 50;
win = GraphWin("Pacman", grid_side*10, grid_side*10);
#NOTE: In this list and other places, first point is y axis and second is x!!
wallsList = [(1,9), (1,10), (2,2), (2,4), (2,5), (2,7), (3,7), (3,9), (3,10),
            (4,3), (4,5), (4,7), (4,9), (5,3), (5,5), (5,7),(5,8),(5,9), (6,2),
            (6,3),(6,5),(6,8),(7,2),(7,5),(7,6),(7,8),(7,10),(8,2),(8,6),(8,8),
            (8,10),(9,4),(9,5),(9,6),(10,1),(10,2),(10,3)];

startPoint = (1,1);
endPoint = (8,5);

adjencyDict = {};

#In the beginning all nodes, except start, are not visited.
nodeVisit = [[False for i in range(11)] for j in range(11)]
nodeVisit[startPoint[0]][startPoint[1]] = True;

parent = [[None for i in range(11)] for j in range(11)]
gValue = [[None for i in range(11)] for j in range(11)]
fValue = [[None for i in range(11)] for j in range(11)]

path = [];
visitQueue = [];

# Global variables for OPEN heap
openNodesListHeap = [""]; # This will have nodes as tuples
openMinHeap = [""]; # Will start form index 1.
openHeapSize = 0;

# Global variables for CLOSED list
closedNodesList = [""];
closedNodesVals = [""];
######################################################################
######################################################################
# HEAP Programs
######################################################################
######################################################################

def openHeapParent(i):
   return int(i/2);

def openHeapLeftChild(i):
   return 2*i;

def openHeapRightChild(i):
   return ((2*i) + 1);

def openHeanSiftUp(i):
   global openMinHeap;
   global openNodesListHeap;
   #print(i,openMinHeap[openHeapParent(i)], openMinHeap[i] );
   while ((i > 1) and (openMinHeap[openHeapParent(i)] >= openMinHeap[i])):
      #swap values
      temp1 = openMinHeap[openHeapParent(i)];
      openMinHeap[openHeapParent(i)] = openMinHeap[i]
      openMinHeap[i] = temp1;
      #swap nodes
      temp2 = openNodesListHeap[openHeapParent(i)];
      openNodesListHeap[openHeapParent(i)] = openNodesListHeap[i]
      openNodesListHeap[i] = temp2;

      i = openHeapParent(i);
      print(i,openMinHeap[openHeapParent(i)], openMinHeap[i] );

def openHeapSiftDown(i):
   global openMinHeap;
   global openHeapSize;
   global openNodesListHeap;
   
   minIndex = i;
   l = openHeapLeftChild(i);
   if(l <= openHeapSize) and (openMinHeap[l] <= openMinHeap[minIndex]):
      minIndex = l;

   r = openHeapRightChild(i);
   if(r <= openHeapSize) and (openMinHeap[r] <= openMinHeap[minIndex]):
      minIndex = r;

   if i != minIndex:
      #swap openMinHeap[i] and openMinHeap[maxIndex]
      temp1 = openMinHeap[i];
      openMinHeap[i] = openMinHeap[minIndex];
      openMinHeap[minIndex] = temp1;
      #swap nodes
      temp2 = openNodesListHeap[i];
      openNodesListHeap[i] = openNodesListHeap[minIndex];
      openNodesListHeap[minIndex] = temp2;
      
      # Again call sift down
      openHeapSiftDown(minIndex);

def openHeapInsert(node, val):
   global openMinHeap;
   global openHeapSize;
   global openNodesListHeap;

   openHeapSize += 1;
   
   if(len(openMinHeap) > openHeapSize): #i.e. Arrat size is bigger than no. of elements in it
      openMinHeap[openHeapSize] = val;
      openNodesListHeap[openHeapSize] = node
   else:
      openMinHeap.append(val);
      openNodesListHeap.append(node);

   openHeanSiftUp(openHeapSize);

def openHeapExtractMin():
   global openMinHeap;
   global openHeapSize;
   global openNodesListHeap;
   
   result = (openNodesListHeap[1], openMinHeap[1]);
   openMinHeap[1] = openMinHeap[openHeapSize];   
   openNodesListHeap[1] = openNodesListHeap[openHeapSize]; 

   #print("Before Sift Down: we have put this at index 1: p = {}, and node".format(openMinHeap[openHeapSize]), openNodesListHeap[openHeapSize])

   openHeapSize -= 1;
   
   openHeapSiftDown(1);

   return result;

#i = index, p = new priority
def openHeapChangePriority(i, p):
   global openMinHeap;
   oldP = openMinHeap[i];
   openMinHeap[i] = p; #new value

   if(p < oldP):
      openHeanSiftUp(i);
   else:
      openHeapSiftDown(i);
   
######################################################################
######################################################################

def createAdjencyDict():
   for y in range(1,11):
      for x in range(1,11):
         point = (y,x);
         if point in wallsList:
            continue;
         else:
            adjencyDict[point] = [];
            if((y-1 != 0)):
               if (y-1,x) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0,(y-1,x));
            if((y+1 != 11)):
               if (y+1,x) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0,(y+1,x));
            if((x-1 != 0)):
               if (y,x-1) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0,(y,x-1));
            if((x+1 != 11)):
               if (y,x+1) not in wallsList:
                  currList = adjencyDict[point];
                  currList.insert(0,(y,x+1));
               
######################################################################
######################################################################
                  
def initializeGame():
   """
   This function initializes the board with walls and place the pacman at start and
   marks the end position.

   """
   #Coloring the background black
   win.setBackground(color_rgb(0,0,0)); 

   for i in range(1,11):
      for j in range(1,11):
         center = Point((i-0.5)*grid_side,(j-0.5)*grid_side);
         cir = Circle(center, 1);
         cir.setFill(color_rgb(255,255,255))
         cir.draw(win)

   #Drawing the walls;
   for a in wallsList:
      pt1 = Point((a[1]-1)*grid_side, (a[0]-1)*grid_side)
      pt2 = Point((a[1])*grid_side, (a[0])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(color_rgb(0,102,248))
      rect1.draw(win)

   center = Point((startPoint[1]-0.5)*grid_side,(startPoint[0]-0.5)*grid_side);
   cir = Circle(center, 25);
   cir.setFill(color_rgb(255,255,0))
   cir.draw(win)
   
   
   rect1 = Rectangle(Point((endPoint[1]-1)*grid_side, (endPoint[0]-1)*grid_side),
                     Point((endPoint[1])*grid_side, (endPoint[0])*grid_side))
   rect1.setFill(color_rgb(255,0,0))
   rect1.draw(win)

######################################################################
######################################################################
# BFS algorithm: A*
#node is coordinate in (y,x) way.
def explore_BestFirstSearch():
   
   """
   Our Heuristic will be manhattan distance
   """
   global path;
   global openMinHeap;
   global openHeapSize;
   global openNodesListHeap;
   global closedNodesList;
   global closedNodesVals;
   global startPoint;
   global endPoint;

   global parent
   global gValue;
   global fValue;
   global nodeVisit;

   gValue[startPoint[0]][startPoint[1]] = 0;
   f = hValPoint(startPoint);
   openHeapInsert(startPoint, f);
   
   print("OPENHEAP:", openHeapSize, openMinHeap, openNodesListHeap)
   
   while openHeapSize > 0:
      time.sleep(0.2);
      #Extracting best node in OPEN and putting it in CLOSED
      bestNode = openHeapExtractMin(); #It retuens (node, f)
      closedNodesList.append(bestNode[0]);
      closedNodesVals.append(bestNode[1]);
      
      colorNode(bestNode[0],250,0,250); #Trun PINK is closed!!
      label = Text(Point((bestNode[0][1]-0.5)*grid_side, (bestNode[0][0]-0.5)*grid_side),bestNode[1]);
      label.setSize(20)
      label.draw(win)
                     
      print("Best Node is {} with fVal = {}".format(bestNode[0], bestNode[1]))
   
      #Checking if this is goal state
      if(bestNode[0] == endPoint):
         break;
      
      
      for SUCCESSOR in adjencyDict[bestNode[0]]:
         # Set SUCCESSOR to point back to BESTNODE
         #parent[SUCCESSOR[0]][SUCCESSOR[1]] = bestNode[0];
         # Compute g(SUCCESSOR) = g(BESTNODE) + the cost 
         g = gValue[bestNode[0][0]][bestNode[0][1]] + 1;
         
         #if SUCCESSOR is the same as any node on OPEN
         if( SUCCESSOR in openNodesListHeap):
            OLD = SUCCESSOR;
            #IF OLD was expensive, then change its parent
            if gValue[OLD[0]][OLD[1]] > g:
               parent[OLD[0]][OLD[1]] = bestNode[0];
               gValue[OLD[0]][OLD[1]] = g;
               #Yaha change priority aaega in heap to change f value
               newF = g + hValPoint(startPoint);
               indexOfNodeInHeap = openNodesListHeap.index(OLD);
               openHeapChangePriority(indexOfNodeInHeap, newF);
               
         elif( SUCCESSOR in closedNodesList):
            OLD = SUCCESSOR;
            #IF OLD was expensive, then change its parent
            if gValue[OLD[0]][OLD[1]] > g:
               parent[OLD[0]][OLD[1]] = bestNode[0];
               gValue[OLD[0]][OLD[1]] = g;
               #Yaha change priority aaega in heap to change f value
               newF = g + hValPoint(startPoint);
               indexOfNodeInHeap = openNodesListHeap.index(OLD);
               openHeapChangePriority(indexOfNodeInHeap, newF);
               #Now we have to change values of successor too.
               for neighbour in adjencyDict[OLD]:
                  if (nodeVisit[neighbour[0]][neighbour[1]] == True):
                     updateSuccessor(neighbour, OLD, g+1);
                     #continue;
                     
         else:
            for neighbour in adjencyDict[bestNode[0]]:
                  if (nodeVisit[neighbour[0]][neighbour[1]] == False):
                     g = gValue[bestNode[0][0]][bestNode[0][1]] + 1
                     gValue[neighbour[0]][neighbour[1]] = g;
                     fVal = g + hValPoint(neighbour);
                     print("\tAdding ({}) to heap: {}".format(neighbour, openNodesListHeap))
                     openHeapInsert(neighbour, fVal);
                     print("\tNow heap is ({})".format(openNodesListHeap)) 
                     nodeVisit[neighbour[0]][neighbour[1]] = True;
                     parent[neighbour[0]][neighbour[1]] = bestNode[0];
                     
                     colorNode(neighbour,0,200,0)
                     label = Text(Point((neighbour[1]-0.5)*grid_side, (neighbour[0]-0.5)*grid_side),fVal);
                     label.setSize(20)
                     label.draw(win)

      print("OPENHEAP:",openHeapSize, openMinHeap, openNodesListHeap)
      print("CLOSEDHEAP:", closedNodesList, closedNodesVals,"\n")


# DFS approach of updating successor.
# Successor would already been visited, and
# its parent would be node that calls it
# (otherwise if its parent is different, do not update)
#parameter is gValue of node
def updateSuccessor(node, parentOfNode, nodeGVal):
   global openMinHeap;
   global openHeapSize;
   global openNodesListHeap;
   global closedNodesList;
   global closedNodesVals;
   global parent
   global gValue;
   global fValue;
   global nodeVisit;
   

   if nodeVisit[node[0]][node[1]] == False:
      return;

   #If this prev visited node has other parent that has more expensive path,
   #Then we will change its parent and gValue (and so fValue).
   if(parent[node[0]][node[1]] !=  parentOfNode):
      if(nodeGVal < gValue[node[0]][node[1]]):
         parent[node[0]][node[1]] =  parentOfNode; #Update the parent
      else:
         return; # Since this node was already in a better path
   
   #Change f value in minHeap for this node
   gValue[node[0]][node[1]] = nodeGVal;
   newF = nodeGVal + hValPoint(node);
   indexOfNodeInHeap = openNodesListHeap.index(node);
   openHeapChangePriority(indexOfNodeInHeap, newF);

   for neighbour in adjencyDict[node]:
      if (nodeVisit[neighbour[0]][neighbour[1]] == True):
         updateSuccessor(neighbour, node, nodeGVal+1);

   

def hValPoint(node):
   return (abs(node[0] - endPoint[0]) + abs(node[1] - endPoint[1]))


#################################################
#################################################
"""
def explore(node):
   global path;
   endReached = False;
  
   time.sleep(0.1);
   if node != startPoint:
      colorNode(node,0,175,0); # Green

   queue = [];
   queue.append(node);

   while len(queue) != 0:
      child = queue.pop(0);
      print("length, current node = ",len(queue), child)
      nodeVisit[child[0]][child[1]] = True;
      if child ==  endPoint:
         endReached = True;
         break;
      if child != startPoint:
         colorNode(child,0,175,0); # Green
      
      for neighbour in adjencyDict[child]:
         if (nodeVisit[neighbour[0]][neighbour[1]] == False):
            queue.append(neighbour);
            parent[neighbour[0]][neighbour[1]] = child;
            
   return;
"""

def getPathBacktracking():
   print("Getting path")
   currPoint = endPoint;
   path.insert(0,endPoint);
   while currPoint != startPoint:
      print(parent[currPoint[0]][currPoint[1]])
      path.insert(0,parent[currPoint[0]][currPoint[1]]);
      currPoint = parent[currPoint[0]][currPoint[1]];

   path.insert(0, startPoint);

def colorNode(node,r,g,b):
   pt1 = Point((node[1]-1)*grid_side, (node[0]-1)*grid_side)
   pt2 = Point((node[1])*grid_side, (node[0])*grid_side)
   rect1 = Rectangle(pt1, pt2)
   rect1.setFill(color_rgb(r,g,b))
   rect1.draw(win)

def colorPathBlack():
   for node in path:
      pt1 = Point((node[1]-1)*grid_side, (node[0]-1)*grid_side)
      pt2 = Point((node[1])*grid_side, (node[0])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(color_rgb(0,0,0))
      rect1.draw(win)
      
      rect1 = Rectangle(Point((endPoint[1]-1)*grid_side, (endPoint[0]-1)*grid_side),
                     Point((endPoint[1])*grid_side, (endPoint[0])*grid_side))
      rect1.setFill(color_rgb(255,0,0))
      rect1.draw(win)



def movePackMan():
   for i in range(0, len(path) - 1):
      time.sleep(0.1);
      #Put a circle in next cell:
      cell = path[i+1];
      center = Point((cell[1]-0.5)*grid_side,(cell[0]-0.5)*grid_side);
      cir = Circle(center, 25);
      cir.setFill(color_rgb(255,255,0))
      cir.draw(win)

      #Turn current circle green
      colorNode(path[i],255,20,147);
      

def main():
   initializeGame();
   createAdjencyDict();
   #explore(startPoint);
   explore_BestFirstSearch()
   
   getPathBacktracking();
   #scolorPathBlack()
   movePackMan();
   
   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse();
   win.close();
   

   
main();


