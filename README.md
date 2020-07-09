**Micromouse Maze Building/Solving algorithm:**
  *Originall designed as testind bed for a physical model, information about the whole embedded project can be found at **()***
  This program generates a randomized maze each time it is ran, then using the randomized maze, solves the maze in a series of steps 
  using only the information provided in the cells that have already been visited. The logic for the movements is dependent on the cells 
  pythagorean distance from the center cells (i.e when presented with an opportunity to move up, or right it will choose the cell with 
  the closest distance to the center, provided the cell has not already been explored.). In the case where the selected cell leads down
  a dead-end path it will incrementally backtrack to the last cell that had an unvisited neighbor cell that had not been selected, and 
  continue steps down that unexplored path. The steps will continue until it has reached the targeted cell, upon which the program will 
  re-run using the same maze and with the knowledge from the last run will sovle the maze in fewer steps, provided some of the steps that
  it took to get to the center in the subsequent run were less-efficient paths that required backtracking. 
  
**File Descriptions Brief:** **More detailed description for each found below this section or in header comments of each file**   
  Flood - Runs the entirety of the program. *(Dependency on Maze.py, Cell.py)*.   
  Maze - Generates randomized 16x16 maze, used by Flood. *(Dependency on Cell.py)  
  Cell.py - Creates class Cell which describes the attributes for each index in the 2-D struct array  
  MazeGeneratorBuilder - Shows the process of maze construction in stepped movements, made for demonstrative / debugging purposes. (Also standalone).
  Note: MazeGeneratorBuilder works but doesnt utilize updated code.
  
**Key Files Descriptions Expanded:**  
**Flood:**  
Description: Flooding algorithm designed initally as a sandbox for testing the logic for   
a physical autonomous robot.  
  
Steps:    
1. Creates a randomized generated maze from Maze.py  
  
2. Does initial run assuming no knowledge about the maze other than what has been visible    
to the theoretical robot as it moves from cell to cell. Moves from cell to cell based   
upon its lowest pythagonal distance to one of the 4 center cells, prioritizing cells   
that it has yet to visit. If it encounters a route that leads to a dead end it marks   
all cells along the route as unavailable ('X') and uses its seen (but not explored)  
neighbors stack to return to the last position that has an unexplored path. Once it   
reaches one of the four middle cells the first run terminates and proceeds into the   
optimized run.  
  
3. Performs optimized run utilizing the same algorithm as before, only it learned from  
the first run and knows not to explore the paths where it knows it does not lead to the   
center position. In this way it optimizes the number of steps needed to achieve the "win"  
condition.   
  
**Maze:**  
Description: Generates a randomized guarenteed solveable 16x16 cell maze through
the use of randomized movements coupled with a stack of not yet visited cells.
  
Steps:  
  
1. Generates a randomized number based on the avaliable moves (i.e non-explored cells and 
movements that do not go out of bounds). Based upon the generated number it will move to
the corresponding cell and mark it as visited, and also removing it from the available
neighbors stack (cells that have been seen (adjacent) but not yet visited and destroying
the "wall" between the current position and target cell).

2. Once the cursor moves to a position where it has no legal moves (no non-visited neighbors
or in bound moves) it uses its avaliable_neighbor stack to return to the position where
it encountered a cell that it did not explore.

3. Execution continues until the cursor has moved to every available cell in the array, in
this way assuring that the exists at least 1 path from the start to the finish.

  

  
  **Outdated Files:**  
  MazeGenerator - Generates the maze for the Main_Flood program *(Dependency on Main_Flood)*.  
  MazeGeneratorShowcase - Prints out a randomized maze each time it is ran, standalone program used only for demonstrative purposes.  
  *(MazeGenerator + MazeGenerator Showcase were combined into Maze.py)*
  
