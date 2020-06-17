# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:40:29 2020
@author: Matt-HP
"""
import time
import random
import math
from MazeGenerator2 import Maze_Creation

class Cell():
    x = 0
    y = 0
    Available = True
    Checked = False
    Top = True
    Bottom = True
    Left = True
    Right = True
    Distance = 0
    Count = 10000
    Neighbor_X = 0
    Neighbor_Y = 0
    Neighbor_Count = 0

#[checked?, up, bottom, left, right, distance to centre, available for reentry?]
maze_list = [[Cell() for y in range(16)] for x in range(16)]
unvisited_neighbor = []


"""Sets the distance for each cell in the maze"""
def setDistance(list):
    for i in range(16):
        for j in range(16):
            a = round(math.sqrt((7-i)*(7-i) + (7-j)*(7-j)), 2)
            b = round(math.sqrt((7-i)*(7-i) + (8-j)*(8-j)), 2)
            c = round(math.sqrt((8-i)*(8-i) + (7-j)*(7-j)), 2)
            d = round(math.sqrt((8-i)*(8-i) + (8-j)*(8-j)), 2)
            list[i][j].Distance = min(a,b,c,d)
            

def randomWall():
        rand = random.randint(1,2)
        if rand == 1: 
            return True
        else:
            return False

def checked(list):
	return list.Checked
	
def upWall(list):
	return list.Top

def bottomWall(list):
	return list.Bottom

def leftWall(list):
	return list.Left
	
def rightWall(list):
	return list.Right

def distToCenter(list):
	return list.Count

def available(list):
	return list.Available

def printMaze(mazeMap,counter,x,y):
    #count =0
    print("_____________________________________________________________________")
    print("")
    nextLine = ""
    for k in range(16):
        nextLine += ('-' * (len(str(counter)) + 2)) + '+'
    print( '+' + nextLine)
    for i in reversed(range(16)):
        nextLine = '|'
        for j in range(16):
            #count = count +1
            if not available(mazeMap[j][i]):
                nextLine += (' ' + 'X' + (' ' * (len(str(counter)))))
            elif checked(mazeMap[j][i]):
                #nextLine += ' * '
                nextLine += (' ' + str(maze_list[j][i].Count) + (' ' * ((int(len(str(counter)) - len(str(maze_list[j][i].Count))))+1)))
            else:
                nextLine += (' ' * (len(str(counter)) + 2))
            if rightWall(mazeMap[j][i]):
                nextLine += '|'
            else:
                nextLine += ' '
        print(nextLine)       
        nextLine = '+'
        for j in range(16):
            if bottomWall(mazeMap[j][i]):
                nextLine += ('-' * (len(str(counter)) + 2)) + '+'
            else:
                nextLine += (' ' * (len(str(counter)) + 2)) +   '+'
        print(nextLine)
        


"""
Called after moving to an unvisited cell. 
1. Checks if there is an adjacent cell that is accessible (No walls, and available),
and unchecked.
2. For each available move, if its not already in the stack then it will be added
with information about the cell that added it to the stack (Neighbor_X,Y,Count)
3. Otherwise if the cell was already in the stack then its neighbor information
will be updated so that if it has to backtrack to that cell it will enter it from 
the updated neighbor cell which is closer to the cell in the stack than its 
previous neighbor. 
"""
def availableNeighbor(mazeMap,i,j):
    neighbor = False
    count = 0
    if j < 15:
        if upWall(mazeMap[i][j]) == False and mazeMap[i][j+1].Checked == False and mazeMap[i][j+1].Available == True:
                neighbor = True
                count = count +1
                if (mazeMap[i][j+1] not in unvisited_neighbor):
                    maze_list[i][j+1].Neighbor_X = maze_list[i][j].x
                    maze_list[i][j+1].Neighbor_Y = maze_list[i][j].y
                    #maze_list[i][j+1].Neighbor_Count = maze_list[i][j].Count
                    maze_list[i][j+1].Neighbor_Count = counter
                    unvisited_neighbor.append(mazeMap[i][j+1])
                else:
                    for k, item in (list(enumerate(unvisited_neighbor))):
                        if (item.x == maze_list[i][j+1].x and item.y == maze_list[i][j+1].y):
                            unvisited_neighbor[k].Neighbor_Count = counter
                            unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                            unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
    if j > 0:
        if bottomWall(mazeMap[i][j]) == False and mazeMap[i][j-1].Checked == False and mazeMap[i][j-1].Available == True:
                neighbor = True
                count = count +1
                if (mazeMap[i][j-1] not in unvisited_neighbor):
                    maze_list[i][j-1].Neighbor_X = maze_list[i][j].x
                    maze_list[i][j-1].Neighbor_Y = maze_list[i][j].y
                    #maze_list[i][j-1].Neighbor_Count = maze_list[i][j].Count
                    maze_list[i][j-1].Neighbor_Count = counter
                    unvisited_neighbor.append(mazeMap[i][j-1])
                else:
                    for k, item in (list(enumerate(unvisited_neighbor))):
                        if (item.x == maze_list[i][j-1].x and item.y == maze_list[i][j-1].y):
                            unvisited_neighbor[k].Neighbor_Count = counter
                            unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                            unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
    if i > 0:
        if leftWall(mazeMap[i][j]) == False and mazeMap[i-1][j].Checked == False and mazeMap[i-1][j].Available == True:
                neighbor = True
                count = count +1
                if (mazeMap[i-1][j] not in unvisited_neighbor):
                    maze_list[i-1][j].Neighbor_X = maze_list[i][j].x
                    maze_list[i-1][j].Neighbor_Y = maze_list[i][j].y
                    #maze_list[i-1][j].Neighbor_Count = maze_list[i][j].Count
                    maze_list[i-1][j].Neighbor_Count = counter
                    unvisited_neighbor.append(mazeMap[i-1][j])
                else:
                    for k, item in (list(enumerate(unvisited_neighbor))):
                        if (item.x == maze_list[i-1][j].x and item.y == maze_list[i-1][j].y):
                            unvisited_neighbor[k].Neighbor_Count = counter
                            unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                            unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
    if i < 15:
        if rightWall(mazeMap[i][j]) == False and mazeMap[i+1][j].Checked == False and mazeMap[i+1][j].Available == True:
                neighbor = True
                count = count +1
                if (mazeMap[i+1][j] not in unvisited_neighbor):
                    maze_list[i+1][j].Neighbor_X = maze_list[i][j].x
                    maze_list[i+1][j].Neighbor_Y = maze_list[i][j].y
                    #maze_list[i+1][j].Neighbor_Count = maze_list[i][j].Count
                    maze_list[i+1][j].Neighbor_Count = counter
                    unvisited_neighbor.append(mazeMap[i+1][j])
                else:
                    for k, item in (list(enumerate(unvisited_neighbor))):
                        if (item.x == maze_list[i+1][j].x and item.y == maze_list[i+1][j].y):
                            unvisited_neighbor[k].Neighbor_Count = counter
                            unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                            unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
    return neighbor


"""For loop that runs through the maze solving algorithm twice, once using
the fresh maze generated from the maze creation algorithm, the second iteration
uses the information about the visited cells, and unavailable cells to solve the
maze more efficiently."""
for q in range(2):
    if q == 0:
        maze_list = Maze_Creation()
    
    setDistance(maze_list)
    
#Sets the inner cells to be empty
    maze_list[7][7].Top = False
    maze_list[7][7].Right = False
    maze_list[7][8].Bottom = False
    maze_list[7][8].Right = False
    maze_list[8][7].Top = False
    maze_list[8][7].Left = False
    maze_list[8][8].Bottom = False
    maze_list[8][8].Left = False
            
    #Sets outside walls 
    for i in range(16):
        maze_list[i][0].Bottom = True
        maze_list[15][i].Right = True
        maze_list[0][i].Left = True
    
    
    #Sets right walls equal to cells to the right left walls, 
    #Sets Top walls equal to cells above below walls
    for i in range(16):
        for j in range(16):
            if i+1 < 16:
                maze_list[i+1][j].Left = maze_list[i][j].Right 
            if j+1 <16:
                maze_list[i][j+1].Bottom = maze_list[i][j].Top
            maze_list[i][j].Checked = False #Marks cells that were marked true from mazecreation algorithm back to false
    
    
    """Initializes i, j - i corresponds to X position, j corresponds to Y,
    counter increments after each move in the maze and gets assigned to the
    latest cell after each move. """
    i = 0
    j = 0
    counter = 0
    printMaze(maze_list, counter, i, j)
    
    
    """Main loop of the solving algorithm, runs until it reaches one of the inner
    4 cells"""  
    while(maze_list[i][j].Distance !=0):
        Path = ''
        counter = counter +1                
        maze_list[i][j].Count = counter
        maze_list[i][j].Checked = True
        printMaze(maze_list, counter, i, j)
        #if  len(unvisited_neighbor) !=0:
        #    print(str(unvisited_neighbor[-1].x) + "," + str(unvisited_neighbor[-1].y))
        time.sleep(.25)
        Shortest = 1000
        if maze_list[i][j] in unvisited_neighbor:
            unvisited_neighbor.remove(maze_list[i][j])
            
        """Checks if there is a move to a cell that hasn't been explored, if there
        is then it chooses the cell it can move to with the lowest distance from
        the center, if there isn't it moves to the else so it can backtrack"""
        if availableNeighbor(maze_list,i,j):
            if i < 15:
                if maze_list[i][j].Right !=True and maze_list[i+1][j].Checked !=True and maze_list[i+1][j].Available == True:
                    Shortest = maze_list[i+1][j].Distance
                    Temp = maze_list[i][j].Distance
                    Path = 'right'
            if i > 0:
                if maze_list[i][j].Left !=True and maze_list[i-1][j].Checked !=True and maze_list[i-1][j].Available == True:
                    Temp = maze_list[i-1][j].Distance 
                    if Temp < Shortest:
                        Shortest = Temp
                        Path = 'left'
            if j < 15:
                if maze_list[i][j].Top !=True and maze_list[i][j+1].Checked !=True and maze_list[i][j+1].Available == True:
                    Temp = maze_list[i][j+1].Distance
                    if Temp < Shortest:
                        Shortest = Temp
                        Path = 'up'
            if j > 0:
                if maze_list[i][j].Bottom !=True and maze_list[i][j-1].Checked !=True and maze_list[i][j-1].Available == True:
                    Temp = maze_list[i][j-1].Distance
                    if Temp < Shortest:
                        Shortest = Temp
                        Path = 'down'
                
            if Path == 'up':
                j = j+1
            elif Path == 'down':
                j = j-1
            elif Path == 'right':
                i = i +1
            elif Path == 'left':
                i = i -1
            



    
    #If there wasnt an adjacent cell that wasnt explored, it will begin
    #backtracking to the latest cell added to the stack, it makes backtracks
    #according to the count assigned to each cell, moving to the available
    #cell with the closest absolute value to the desired neighbor cell to the cell
    #in the stack
    
        else:
            while ((maze_list[i][j].x != unvisited_neighbor[-1].Neighbor_X) or (maze_list[i][j].y != unvisited_neighbor[-1].Neighbor_Y)):
                time.sleep(.5)
                Shortest = 1000
                maze_list[i][j].Available = False
                if maze_list[i][j].Right != True and maze_list[i+1][j].Available == True and abs(maze_list[i][j].Count - unvisited_neighbor[-1].Neighbor_Count) > abs(maze_list[i+1][j].Count - unvisited_neighbor[-1].Neighbor_Count):
                    if (abs(maze_list[i+1][j].Count - unvisited_neighbor[-1].Neighbor_Count) < Shortest):
                        Path = "right"
                        Shortest = abs(maze_list[i+1][j].Count - unvisited_neighbor[-1].Neighbor_Count)
                if maze_list[i][j].Left != True and maze_list[i-1][j].Available == True and abs(maze_list[i][j].Count - unvisited_neighbor[-1].Neighbor_Count) > abs(maze_list[i-1][j].Count- unvisited_neighbor[-1].Neighbor_Count):
                    if (abs(maze_list[i-1][j].Count - unvisited_neighbor[-1].Neighbor_Count) < Shortest):
                        Path = "left"
                        Shortest = abs(maze_list[i-1][j].Count - unvisited_neighbor[-1].Neighbor_Count)
                if maze_list[i][j].Top != True and maze_list[i][j+1].Available == True and abs(maze_list[i][j].Count - unvisited_neighbor[-1].Neighbor_Count) > abs(maze_list[i][j+1].Count- unvisited_neighbor[-1].Neighbor_Count):
                    if (abs(maze_list[i][j+1].Count - unvisited_neighbor[-1].Neighbor_Count) < Shortest):
                        Path = 'up'
                        Shortest = abs(maze_list[i][j+1].Count - unvisited_neighbor[-1].Neighbor_Count)
                if maze_list[i][j].Bottom != True and maze_list[i][j-1].Available == True and abs(maze_list[i][j].Count - unvisited_neighbor[-1].Neighbor_Count) > abs(maze_list[i][j-1].Count- unvisited_neighbor[-1].Neighbor_Count):
                    if (abs(maze_list[i][j-1].Count - unvisited_neighbor[-1].Neighbor_Count) < Shortest):
                        Path = "down"
                        Shortest = abs(maze_list[i][j-1].Count - unvisited_neighbor[-1].Neighbor_Count)
                else:
                    print("error")
                
                    
                if Path == 'right':
                    i = i +1
                
                elif Path == 'left':
                    i = i -1
                elif Path == 'up':
                    j = j+1
                elif Path == 'down':
                    j = j-1
                        
                    
                #If it backtracks to the cell that added the cell to the stack, break
                if(maze_list[i][j].x == unvisited_neighbor[-1].Neighbor_X) and (maze_list[i][j].y == unvisited_neighbor[-1].Neighbor_Y):
                    maze_list[i][j].Checked = True
                    if maze_list[i][j] in unvisited_neighbor:
                        unvisited_neighbor.remove(maze_list[i][j])
                    break
                maze_list[i][j].Available = False #Marks backtracked cells as not available
                #maze_list[i][j].Distance = 1000
                counter = counter +1             
                maze_list[i][j].Count = counter
                maze_list[i][j].Checked = True
                printMaze(maze_list, counter, i, j)
            
    
    counter = counter +1                
    maze_list[i][j].Count = counter
    maze_list[i][j].Checked = True
    printMaze(maze_list, counter, i, j)
    #for i in range(len(unvisited_neighbor)):
    #    print(str(unvisited_neighbor[i].x) + "," + str(unvisited_neighbor[i].y))
    time.sleep(1)
    Shortest = 1000
    
    
    #After first iteration if it hasn't explored a cell, mark it as inaccessible
    #Update corresponding neighboring cells to match walls
    for r in range(16):
        for c in range(16):
            if maze_list[r][c].Checked == False or maze_list[r][c].Available == False:
                maze_list[r][c].Top = True
                maze_list[r][c].Left = True
                maze_list[r][c].Right = True
                maze_list[r][c].Bottom = True
                maze_list[r][c].Distance = 1000
            if maze_list[r][c].Checked == True and maze_list[r][c].Available == True:
                if c < 15:
                    maze_list[r][c].Top = maze_list[r][c+1].Bottom
                if c > 0:
                    maze_list[r][c].Bottom = maze_list[r][c-1].Top
                if r > 0:
                    maze_list[r][c].Left = maze_list[r-1][c].Right
                if r < 15:
                    maze_list[r][c].Right = maze_list[r+1][c].Left
                
    printMaze(maze_list, counter, i, j)