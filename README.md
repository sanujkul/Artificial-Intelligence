# ArtificialIntelligence-CED16
***
## Table of Content - 
### i.    01_basicTicTakToe.py
### ii.   02_miniMaxTicTakToe.py
### iii.  03_packmanDFS.py
### iv.   04_packmanBFS.py
### v.    05a_hillClimbing_8Puzzle.py
### vi.   005b_hillClimbing_4queens.py
### vii.  05b2_hillClimbing_8queens.py
### viii. 06_Constrains_Sudoku.py
### ix.   07_packmanAStar.py
***

## i.    01_basicTicTakToe.py
In this program, the loction to make a move is chosen randomly.  
![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/01_BasicTicTacToe.png)

***

## ii.   02_miniMaxTicTakToe.py
In this program, the loction to make a move is chosen by miniMax approach. 
Hence it is impossible to beat the AI. Either AI will win or game will draw.  
![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/02_miniMaxTicTacToe.png)


***

## iii.  03_packmanDFS.py  
In this program, pacman is simulated and its way to find its goal to end node is demonstarated by using Depth first search Algorithm.  
Yellow Ball - Pacman. 
Red Node - Goal Node.  
Blue Nodes - Walls.  
Green Nodes - Searching the path.   
Pink Nodes - Path taken.  

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=-vWjmX9M5rg)

Following 2 images show the start and end states respectively-    
![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/03_DFS_PACKMAN_START.png) ![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/03_DFS_PACKMAN_END.png)

***

## iv.   04_packmanBFS.py
In this program, pacman is simulated and its way to find its goal to end node is demonstarated by using Breath first search Algorithm.  
Yellow Ball - Pacman. 
Red Node - Goal Node.  
Blue Nodes - Walls.  
Green Nodes - Searching the path.   
Pink Nodes - Path taken.  

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=mbi9hgKg-hU)

Following 2 images show the start and end states respectively-    
![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/04_BFS_PACKMAN_START.png) ![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/04_BFS_PACKMAN_END.png)

***

## v.   05a_hillClimbing_8Puzzle.py
In this program, 8 puzzle game has been simulated using hill climbing technique.    

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=utepHs5Nwpc&list=PLD0rOb-SUEXZ9IMxkrxjcj0LJnzunQeAd&index=1)

Following 2 images show the start and end states respectively-    
![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/05_hillClmbing_8Puzzle_start.png) ![](https://github.com/sanujkul/ArtificialIntelligence-CED16/blob/master/Images/05_hillClmbing_8Puzzle_end.png)

***

## vi.   005b_hillClimbing_4queens.py
In this program, 4 Queens game has been simulated using hill climbing technique. Queens have to be placed such that no queen attack each other

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=ZcQsixOocRc&list=PLD0rOb-SUEXZ9IMxkrxjcj0LJnzunQeAd&index=5)

Following 2 images show the start and end states respectively-    
![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/05b_hillClmbing_4Queens_start.png) ![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/05b_hillClmbing_4Queens_end.png)

***


## vii.  05b2_hillClimbing_8queens.py
In this program, 8 Queens game has been simulated using hill climbing technique. Queens have to be placed such that no queen attack each other

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=q_YPeDci8oU&list=PLD0rOb-SUEXZ9IMxkrxjcj0LJnzunQeAd&index=5)

Following 2 images show the start and end states respectively-    
![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/05b_hillClmbing_8Queens_start.png) ![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/05b_hillClmbing_8Queens_end.png)

***

## viii. 06_Constrains_Sudoku.py  
In this program,Sudoku has been solved using Constraint Satisfaction technique.

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=7F_EM4iAfRE&list=PLD0rOb-SUEXZ9IMxkrxjcj0LJnzunQeAd&index=7)

Following Sudoku problem was taken from the internet:   
![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/SampleSudokuQues.png) ![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/SampleSudokuSol.png)

Following 2 images show the start and end states respectively-     
![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/06_Constrains_Sudoku_start.png) ![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/06_Constrains_Sudoku_end.png)

***

## ix.   07_packmanAStar.py
In this program, pacman is simulated and its way to find its goal to end node is demonstarated by using A* search Algorithm.  
Heuristic is the manhattan distance. And the cost to get from one node to another is 1.
We can see here that packman takes the shortest path (unlike Depth first search) and scan lesser area while finding path (unlike Breath First Search).

Pink Nodes - CLOSED nodes. 
Yellow Ball - Pacman. 
Red Node - Goal Node/Path Taken.  
Blue Nodes - Walls.  
 

The working of this appraoch [has been uploaded on this YouTube Video](https://www.youtube.com/watch?v=0pKdbXYBgPM)

Following 2 images show the start and end states respectively-    
![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/07_packmanAStar_start.png) ![](https://github.com/sanujkul/Artificial-Intelligence/blob/master/Images/07_packmanAStar_end.png)

