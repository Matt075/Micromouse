"""
Created on Fri Mar  23 14:20:12 2020
@author: Matt Burns
Description: Flooding algorithm designed as a sandbox for testing the logic for 
physical Micromouse movement. 

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
"""

import time
from Maze import Maze

start_time = time.time()

def advance():
    """ Advance to the available neighbor with the lowest distance from the
    four center cells """
    global i, j, counter
    shortest = 300
    path = ""
    if (not Maze.cell(i, j).east_wall and not Maze.cell(i+1, j).checked and Maze.cell(i+1, j).available
            and Maze.cell(i+1, j).available):
        shortest = Maze.cell(i+1, j).distance
        path = "r"
    if (not Maze.cell(i, j).west_wall and not Maze.cell(i-1, j).checked and Maze.cell(i-1, j).available
            and Maze.cell(i-1, j).available
            and Maze.cell(i-1, j).distance < shortest):
        shortest = Maze.cell(i-1, j).distance
        path = "l"
    if (not Maze.cell(i, j).north_wall and not Maze.cell(i, j+1).checked and Maze.cell(i, j +1).available
            and Maze.cell(i, j+1).available
            and Maze.cell(i, j+1).distance < shortest):
        shortest = Maze.cell(i, j+1).distance
        path = "u"
    if (not Maze.cell(i, j).south_wall and not Maze.cell(i, j-1).checked and Maze.cell(i, j -1).available
            and Maze.cell(i, j-1).available
            and Maze.cell(i, j-1).distance < shortest):
        path = "d"

    if path == "u":
        j += 1
    elif path == "d":
        j -= 1
    elif path == "r":
        i += 1
    else:
        i -= 1
    counter += 1

    # check if this area is available (after virtually moving to it)
    
    if not check_area():
        if path == "u":
            j -= 1
        elif path == "d":
            j += 1
        elif path == "r":
            i -= 1
        else:
            i += 1
        counter -= 1

    Maze.cell(i, j).set_checked(True)
    Maze.cell(i, j).set_step(counter)


def check_area():
    """ This algorithm checks if an entire area is available without
    physically searching it.
    - When the robot first enters the area, the algorithm adds unchecked
    adjacent cells to the list.
    - The algorithm then virtually moves to the next cell in the list which
    was added by the step above. The same process is repeated until either it
    reaches the center cells (there IS a path to the center passing through
    this area without intersecting older paths -->> this area is available),
    or there is no adjacent unchecked cells (this area leads back to older
    path or leads to nowhere).
    - If the area is unavailable, the algorithm will mark all cells in this
    area unavailable.
    NOTE: Notice that this algorithm doesn't check or need to check about any
    walls -->> No need to traverse the area. Its structure is actually quite
    similar to available_neighbor
    """
    global counter
    unchecked_list = [[i, j]]
    unchecked_available = True
    num = 0
    while num < len(unchecked_list):
        x = unchecked_list[num][0]
        y = unchecked_list[num][1]
      
        if Maze.cell(x, y).distance == 0 or not unchecked_available:
            break
        unchecked_available = False

        if x < 15 and not Maze.cell(x+1, y).checked and Maze.cell(x+1, y).available:
            unchecked_available = True

            if [x+1, y] not in unchecked_list:
                unchecked_list.append([x+1, y])

        if x > 0 and not Maze.cell(x-1, y).checked and Maze.cell(x-1, y).available:
            unchecked_available = True

            if [x-1, y] not in unchecked_list:
                unchecked_list.append([x-1, y])

        if y < 15 and not Maze.cell(x, y+1).checked and Maze.cell(x, y+1).available:
            unchecked_available = True

            if [x, y+1] not in unchecked_list:
                unchecked_list.append([x, y+1])

        if y > 0 and not Maze.cell(x, y-1).checked and Maze.cell(x, y-1).available:
            unchecked_available = True

            if [x, y-1] not in unchecked_list:
                unchecked_list.append([x, y-1])
        num += 1
 

        

    # If the loop successfully reaches the end of the list, it means that
    # there is no more adjacent unchecked cell -->> Unavailable area
    if num == len(unchecked_list):
        for item in unchecked_list:
            Maze.cell(item[0], item[1]).set_unavailable()
            counter = counter +1
        return False
    else:
        return True


# i = x coordinate, j = y coordinate
# - counter counts the steps taken after each move
for q in range(2):
    for i in range(16):
        for j in range(16):
            if Maze.cell(i,j).available == True:
                Maze.cell(i,j).set_checked(False)   
    i = 0
    j = 0
    counter = 0
    if q == 0:
        print(' ' * 32 + "|INITIAL MAZE|:")
        Maze.print(10,q)
    Maze.cell(i, j).set_checked(True)
    Maze.cell(i, j).set_step(counter)
   
    while Maze.cell(i, j).distance != 0:
        #***uncomment these to see progress***
        #Maze.print(counter,q)
        #time.sleep(0.22)
        advance()
    if q == 0:
        print("\n" + ' ' * 32 + "|FIRST SOLVE|")
        counter_One = counter
        Maze.print(counter, q)
        print(f"Cells traversed = {counter}")
    else:
        print("\n" + ' ' * 24 + "|EFFICIENT RUN - NO BACKTRACKING|")
        Maze.print(counter, q)
        execution_time = int((time.time() - start_time) * 1000)
        print(f"Execution time = {execution_time} milliseconds !!!")
        print(f"First run cells traversed = {counter_One}")
        print(f"Efficient run cells traversed = {counter}")
        print(f"Optimization = {counter_One-counter} Step(s)")
        
   
    
    
