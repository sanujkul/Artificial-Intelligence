from graphics import *
import time;
from string import ascii_lowercase;
from string import ascii_uppercase;

grid_side = 50;
win = GraphWin("Sudoku", grid_side*10, grid_side*10);

variablesDict = dict();

n = 9;

startingConditions = {"A1":4, "A2":5, "B3":2,
                      "B5":7, "B7":6, "B8":3,
                      "C8":2, "C9":8, "D4":9,
                      "D5":5, "E2":8, "E3":6,
                      "E7":2, "F2":2, "F4":6,
                      "F7":7, "F8":5, "G7":4,
                      "G8":7, "G9":6, "H2":7,
                      "H5":4, "H6":5, "I3":8, "I6":9};

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
    self.valueAssigned = False if(value == 0) else True;
    
  def setVal(self,val):
    self.value = val;
    self.valueAssigned = False if(val == 0) else True;

  """
  This func will add a value to domain,
  or remove one, if val not in domain return false!! Constraints not satisfied
  """
  def addRemoveDomainVal(self, operation, value):
    if(operation == "add"):
      self.domain.append(value);
    else:
      if value in self.domain:
        self.domain.remove(value);
      else:
        return False;
      
    return True;

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

   

def drawNode(variableObj):
  row = ascii_uppercase.index(variableObj.row)+1;
  column = int(variableObj.column);
  #Color with the number's color:
  pt1 = Point((column-1)*grid_side, (row-1)*grid_side)
  pt2 = Point((column)*grid_side, (row)*grid_side)
  rect1 = Rectangle(pt1, pt2)
  rect1.setFill(numColors[variableObj.value]);
  rect1.draw(win)
  #Write the value at this node:
  label = Text(Point((column-0.5)*grid_side, (row-0.5)*grid_side),variableObj.value);
  label.setSize(30)
  label.setTextColor("black");
  #print("Writing {} at position ({},{})".format(val,(x-0.5)*grid_side,(row-0.5)*grid_side))
  label.draw(win)


"""
To empty a position, just make it white
"""
def clearNode(variableObj): 
  row = ascii_uppercase.index(variableObj.row)+1;
  column = int(variableObj.column);
  #Color with the number's color:
  pt1 = Point((column-1)*grid_side, (row-1)*grid_side)
  pt2 = Point((column)*grid_side, (row)*grid_side)
  rect1 = Rectangle(pt1, pt2)
  rect1.setFill('white');
  rect1.draw(win)
######################################################################
######################################################################

def initGame():
   """
   Initialize all the variables with val = 0 (blank) and domain (1..9)
   The results are stored in a dict.

   """
   global variablesDict;

   #In the beginning the domain for all the variables will be all ints from 1 to 9
   #We will assign all of them value 0, i.e they are blank
   
   for rowNo in ascii_uppercase[0:9]:
      for columnNo in range(1, 10): #From 1 to 9
         variableName = "{}{}".format(rowNo,columnNo);
         domain = [x for x in range(1,10)];
         #print("Added for {}".format(variableName));
         variablesDict[variableName] = variable(variableName,0,domain); # 0 means blank

   #Now we can apply the starting conditions of the game
   #i.e. Some nodes are previously assigned some value
   for pos in startingConditions:
      val = startingConditions[pos];
      variablesDict[pos].setVal(val);
      drawNode(variablesDict[pos]);
      addRemoveValueToMatchConstraints("remove", pos, val);
   time.sleep(2); 
######################################################################
######################################################################

"""
This function will find which node (A1, A2, ..., I8,I9)
has minimum domain size left and will return it
"""
def findMinRemainingValuesHeuristic():
  maxDomain = 10;   #A number greater than 9 (max domain size)
  minDoaminVar = '00';  #Lets init to this
  for variable in variablesDict:
    thisVarDomainLen = len(variablesDict[variable].domain)
    #if value is not assigned to this var and it has minimum domain length
    if thisVarDomainLen < maxDomain and variablesDict[variable].valueAssigned==False:
      maxDomain = thisVarDomainLen;
      minDoaminVar = variable;

  #It will return "00" if all of the vars are assigned values
  #        return "X#", varaible name of smallest domain func
  return minDoaminVar;

######################################################################
######################################################################
def addRemoveValueToMatchConstraints(operation, varaibleName, value):
  """
  Remove will be needed for CONSTARINT PROPAGATION when variable is assigned some value.
  Now we need to remove this value from domain of other variables
  Add will be needed when backtarcking and value needs to be added back
  to the list of domain
  """
  #Satisfying Row Constraints:
  row = variablesDict[varaibleName].row;
  for i in range(1,n+1): #These will be columns number
    constraintVarName = "{}{}".format(row,i);
    variablesDict[constraintVarName].addRemoveDomainVal(operation, value);

  #Satisfying Column Constraints:
  column = variablesDict[varaibleName].column;
  for rowNo in ascii_uppercase[0:9]: #These will be rows number
    constraintVarName = "{}{}".format(rowNo,column);
    variablesDict[constraintVarName].addRemoveDomainVal(operation, value);

  #Satisfying Square Constraints:
  rowIndex = ascii_uppercase.index(row)
  squareRowStart = rowIndex - (rowIndex % 3);
  
  squareColumnStart = int(column) - ((int(column)-1)%3);

  for r in range(squareRowStart,squareRowStart+3):
    for c in range(squareColumnStart, squareColumnStart+3):
      constraintVarName = "{}{}".format(ascii_uppercase[r],c);
      #print(constraintVarName);
      variablesDict[constraintVarName].addRemoveDomainVal(operation, value);
  
######################################################################
######################################################################

def performConstraintSatisfaction():
  """
  This is main AI recursive function for constrains satisfaction
  Recursion is end with
      true - if all variables are assigned some value
      false - if there is a valriable whom value cant be assigned

      Otherwise it will iterate over domain of a variable and
      assign the value to this variable and then propagate it
      to satisfy constraints and then recursively call this function
  """
  #Get the node that has min domain left and value is not assigned
  varName = findMinRemainingValuesHeuristic();

  if(varName == "00"): #i.e. alll positions are filled now
    return True;
  
  thisVarObj = variablesDict[varName]; 
  #Recursion end: If length of domain of this var is 0, then
  #There are no more moves left, return False;
  if(len(thisVarObj.domain) == 0):
    return False;

  constraintMatched = False;
  print("Now we'll assess for variable = {}".format(varName));
  #Else now we'll iterate over all possible domain values of this var
  for value in [x for x in thisVarObj.domain]:
    time.sleep(0.3);
    #Lets assign this somevalue
    thisVarObj.setVal(value);
    drawNode(thisVarObj);
    #Constraint Propagation: Then remove this value from all those nodes with
    #whim this variable node has a consytraint with
    addRemoveValueToMatchConstraints("remove", varName, value);

    constraintMatched = performConstraintSatisfaction()

    if(constraintMatched == True):
      print("{} constraint matched with value {}!!".format(varName,value))
      return True;                #Send True Back
    else:
      addRemoveValueToMatchConstraints("add", varName, value);                   #Add value back to all the variables from which it was removes
      print("{} constraint NOT matched with value {}!!".format(varName,value))
      clearNode(thisVarObj);
      
  return constraintMatched; #Returning False if constarint cant be matched

######################################################################
######################################################################
def main():
   initGraphics();
   initGame();
   performConstraintSatisfaction();
   #findMinRemainingValuesHeuristic();
   #print(findMinRemainingValuesHeuristic());
   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse();
   win.close();
   
main();





def printForAllVariables(prop="value"):
  for rowNo in ascii_uppercase[0:9]:
      for columnNo in range(1, 10): #From 1 to 9
         variableName = "{}{}".format(rowNo,columnNo);
         if (prop == "domain"):
           print(variablesDict[variableName].domain,  end ="\t ");
         elif (prop == "valAss"):
           print(variablesDict[variableName].valueAssigned,  end ="\t ");
         else:
           print(variablesDict[variableName].value, end ="\t ");
      print("\n")
