from graphics import *
import time;
from string import ascii_lowercase;
from string import ascii_uppercase;

grid_side = 50;
win = GraphWin("Sudoku", grid_side*10, grid_side*10);

variablesDict = dict();





#numColors has color corresponding to each number from 0 (blank), 1,.,9.
numColors = ['white','red', 'skyblue', 'yellow', 'green', 'orange', 'pink', 'magenta', 'violet', 'lightgreen']

"""
A1, A2, ..., I8, I9 can be variable names.
where A--I are for Rows and
and 1 -- 9 are for Columns.
Values a variable can take is form 1 to 9.
Domain is a list of all available values (after subtracting constraints) can be taken
"""
class variable:
  def __init__(self, name, value, domain):
    self.value = value;
    self.domain = domain
    self.row = name[0];
    self.column = name[1];
    self.color = numColors[value];

 # def getVal(self):
  #  return self.value;


######################################################################
######################################################################
def initGraphics():
   """
   This function initializes the board grahics

   """
   #Coloring the background black
   win.setBackground(color_rgb(255,255,255));
   n = 9; #The number of squares per row and column
   for i in range(1,n+1):
      for j in range(1,n+1):
         pt1 = Point((i-1)*grid_side, (j-1)*grid_side)
         pt2 = Point((i)*grid_side, (j)*grid_side)
         rect1 = Rectangle(pt1, pt2)
         rect1.setFill(color_rgb(255,255,255))
         rect1.draw(win)

   #Writing A.B.C... along a row     
   x = 10;
   for row in range(1, n+1): #For every row at column = 10*grid_side;
      pt1 = Point((x-1)*grid_side, (row-1)*grid_side)
      pt2 = Point((x)*grid_side, (row)*grid_side)
      rect1 = Rectangle(pt1, pt2);
      rect1.setFill(color_rgb(0,0,0))
      rect1.draw(win)

      val = ascii_uppercase[row-1];
      label = Text(Point((x-0.5)*grid_side, (row-0.5)*grid_side),val);
      label.setSize(30)
      label.setTextColor("white");
      #print("Writing {} at position ({},{})".format(val,(x-0.5)*grid_side,(row-0.5)*grid_side))
      label.draw(win)
      
   #Writing 1,2,3... along a column     
   y = 10;
   for column in range(1, n+1): #For every row at column = 10*grid_side;
      pt1 = Point((column-1)*grid_side, (y-1)*grid_side)
      pt2 = Point((column)*grid_side, (y)*grid_side)
      rect1 = Rectangle(pt1, pt2);
      rect1.setFill(color_rgb(0,0,0))
      rect1.draw(win)

      val = column;
      label = Text(Point((column-0.5)*grid_side, (y-0.5)*grid_side),val);
      label.setSize(30)
      label.setTextColor("white");
      #print("Writing {} at position ({},{})".format(val,(x-0.5)*grid_side,(row-0.5)*grid_side))
      label.draw(win)

######################################################################
######################################################################

def initGame():
   """
   Initialize all the variables with val = 0 (blank) and domain (1..9)
   The results are stored in a dict.

   """
   global variablesDict;

   #In the beginning the domain for all the variables will be all ints from 1 to 9
   domain = [x for x in range(1,10)];
   #We will assign all of them value 0, i.e they are blank
   
   for rowNo in ascii_uppercase[0:9]:
      for columnNo in range(1, 10): #From 1 to 9
         variableName = "{}{}".format(rowNo,columnNo);
         #print("Added for {}".format(variableName));
         variablesDict[variableName] = variable(variableName,0,domain); # 0 means blank
   

         
######################################################################
######################################################################

         
def main():
   initGame();
   initGraphics();
   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse();
   win.close();
   

   
main();


