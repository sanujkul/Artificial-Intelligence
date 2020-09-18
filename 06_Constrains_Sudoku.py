from graphics import *
import time;
from string import ascii_lowercase;
from string import ascii_uppercase;

grid_side = 50;
win = GraphWin("Sudoku", grid_side*10, grid_side*10);

variablesDict = dict();

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

 # def getVal(self):
  #  return self.value;

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
         #variableName = "{}{}".format(rowNo,columnNo);
         print("Added for {}".format(variableName));
         variablesDict[variableName] = variable(variableName,0,domain); # 0 means blank
   

         

def main():
   initGame();
   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse();
   win.close();
   

   
main();


