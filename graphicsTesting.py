from graphics import *

def main():
   #Just create an empty window with name Pacman
   win = GraphWin("Pacman", 500, 500)

   #Coloring the background black
   win.setBackground(color_rgb(0,0,0)); 
   
   #creating a CIRCLE in the middle:
   #circle need center (Point) ,radius
   center = Point(250,250);
   cir = Circle(center, 50);
   cir.setFill(color_rgb(255,255,0))
   cir.draw(win);

   #Creating a POINT: Draws a single pixel
   center.setOutline(color_rgb(0,0,0))
   center.draw(win);
   
   #Creating a RECTANGLE: Draws a single pixel
   rect1 = Rectangle(Point(0, 0), Point(25, 25))
   rect1.setFill(color_rgb(255,255,0))
   rect1.draw(win)

   rect2 = Rectangle(Point(25, 0), Point(50, 25))
   rect2.setFill(color_rgb(255,255,0))
   rect2.draw(win)

   rect3 = Rectangle(Point(475, 475), Point(500, 500))
   rect3.setFill(color_rgb(255,255,0))
   rect3.draw(win)
   

   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse();
   win.close();


main();
