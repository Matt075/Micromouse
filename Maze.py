"""
Created on Fri Mar  14 06:23:19 2020
@author: Matt Burns
Description: Generates a randomized guarenteed solveable 16x16 cell maze through
the use of randomized movements coupled with a stack of not yet visited cells.

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
"""
from Cell import Cell

import random
from colorama import Fore, Style

class Maze:
    maze = [[Cell(x, y) for y in range(16)] for x in range(16)]
    for i in range(16):
        for j in range(16):
            maze[i][j].set_north_wall(True)
            maze[i][j].set_south_wall(True)
            maze[i][j].set_west_wall(True)
            maze[i][j].set_east_wall(True)
    unvisited_stack = []

    @classmethod
    def cell(cls, x, y):
        """ Return the cell at the given coordinate"""
        return cls.maze[x][y]

    @classmethod
    def print(cls, counter, q):
        print("_____________________________________________________________________")
        print("")
        nextLine = ""
        for k in range(16):
            nextLine += ('-' * (len(str(counter)) + 2)) + '+'
        print( '+' + nextLine)
        for j in reversed(range(16)):
            nextLine = '|'
            for i in range(16):
                #count = count +1
                if not cls.maze[i][j].available:
                    if q == 0:
                        print(nextLine + ' ', end="")
                        print(Fore.RED + '\033[1m' + 'X' + Style.RESET_ALL, end="")
                        nextLine = (' ' * (len(str(counter))))
                    else:
                        nextLine += (' ' * (len(str(counter)) + 2))
                elif cls.maze[i][j].checked:
                    nextLine += ' '
                    print(nextLine, end="")
                    print(Fore.GREEN + '\033[1m' + str(cls.maze[i][j].step) + Style.RESET_ALL, end="")
                    nextLine = ("" + (' ' * ((int(len(str(counter)) - len(str(cls.maze[i][j].step))))+1))) 
                    
                else:
                    nextLine += (' ' * (len(str(counter)) + 2))
                if cls.maze[i][j].east_wall:
                    nextLine += '|'
                else:
                    nextLine += ' '
            print(nextLine)       
            nextLine = '+'
            for i in range(16):
                if i == 7 and j == 8:
                    if cls.maze[i][j].south_wall:
                        nextLine += ('-' * (len(str(counter)) + 2)) + '+'
                    else:
                        nextLine += (' ' * (len(str(counter)) + 2)) +  Fore.YELLOW + '\033[1m' + 'o' + Style.RESET_ALL
                elif cls.maze[i][j].south_wall:
                    nextLine += ('-' * (len(str(counter)) + 2)) + '+'
                else:
                    nextLine += (' ' * (len(str(counter)) + 2)) +   '+'
            print(nextLine)


    @classmethod
    def available_neighbor(cls, i, j):
        """ For use with creating the maze
        Return whether there is an available neighbor
        """
        if j < 15 and not cls.maze[i][j+1].checked:
            cls.unvisited_stack.append([i, j+1])
            return True

        if j > 0 and not cls.maze[i][j-1].checked:
            cls.unvisited_stack.append([i, j-1])
            return True

        if i < 15 and not cls.maze[i+1][j].checked:
            cls.unvisited_stack.append([i+1, j])
            return True

        if i > 0 and not cls.maze[i-1][j].checked:
            cls.unvisited_stack.append([i-1, j])
            return True

        return False

    @classmethod
    def create(cls):
        """ Create a random organic maze """
        # Start square is bounded on three sides by walls. 
        cls.maze[0][0].set_checked(True)
        cls.maze[0][0].set_north_wall(False)
        cls.maze[0][1].set_south_wall(False)

        i = 0
        j = 1
        k = 1
        visited_stack = []

        while k < 255:  # 16*16 - 1
            path = []
            cls.maze[i][j].set_checked(True)
            if [i, j] in cls.unvisited_stack:
                cls.unvisited_stack.remove([i, j])
            if cls.available_neighbor(i, j):
                visited_stack.append([i, j])
                if i < 15 and not cls.maze[i+1][j].checked:
                    path.append("r")
                if i > 0 and not cls.maze[i-1][j].checked:
                    path.append("l")
                if j < 15 and not cls.maze[i][j+1].checked:
                    path.append("u")
                if j > 0 and not cls.maze[i][j-1].checked:
                    path.append("d")

                destination = random.choice(path)
                if destination == "u":
                    cls.maze[i][j].set_north_wall(False)
                    cls.maze[i][j+1].set_south_wall(False)
                    j += 1
                elif destination == "d":
                    cls.maze[i][j].set_south_wall(False)
                    cls.maze[i][j-1].set_north_wall(False)
                    j -= 1
                elif destination == "r":
                    cls.maze[i][j].set_east_wall(False)
                    cls.maze[i+1][j].set_west_wall(False)
                    i += 1
                else:
                    cls.maze[i][j].set_west_wall(False)
                    cls.maze[i-1][j].set_east_wall(False)
                    i -= 1
                k += 1

            elif len(visited_stack) != 0:
                i = visited_stack[-1][0]
                j = visited_stack[-1][1]
                visited_stack.pop()

        cls.maze[7][7].set_north_wall(False)
        cls.maze[7][7].set_east_wall(False)
        cls.maze[7][8].set_east_wall(False)
        cls.maze[7][8].set_south_wall(False)
        cls.maze[8][7].set_north_wall(False)
        cls.maze[8][7].set_west_wall(False)
        cls.maze[8][8].set_south_wall(False)
        cls.maze[8][8].set_west_wall(False)

        for i in range(16):
            for j in range(16):
                cls.maze[i][j].set_checked(False)


Maze.create()

if __name__ == "__main__":
    Maze.print(10, 0)
