# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:30:50 2020
@author: Matt-HP
"""

import time
import random
import math


unvisited_neighbor = []

class Cell():
    x = 0
    y = 0
    Checked = False
    Top = True
    Bottom = True
    Left = True
    Right = True
    Distance = 0
    Avaliable = True
    Count = 10000
    Neighbor_X = 0
    Neighbor_Y = 0
    Neighbor_Count = 0

#[checked?, up, bottom, left, right, distance to centre, available for reentry?]
maze_list = [[Cell() for y in range(16)] for x in range(16)]
visited_Stack = []

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
	return list.Avaliable

def printMaze(mazeMap):
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
                nextLine += ' X '
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
        
        

def availableNeighbor(mazeMap,i,j):
    neighbor = False
    count = 0
  #  if j< 15: 
   # if upWall(mazeMap[i][j]) == False and mazeMap[i][j+1].Checked == False:
    if j < 15:
        if mazeMap[i][j+1].Checked == False:    
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i][j+1])
                """
            if (mazeMap[i][j+1] not in unvisited_neighbor):
                maze_list[i][j+1].Neighbor_X = maze_list[i][j].x
                maze_list[i][j+1].Neighbor_Y = maze_list[i][j].y
                #maze_list[i][j+1].Neighbor_Count = maze_list[i][j].Count
                maze_list[i][j+1].Neighbor_Count = counter
                unvisited_neighbor.append(mazeMap[i][j+1])
            else:
                for k, item in reversed(list(enumerate(unvisited_neighbor))):
                    if (item.x == maze_list[i][j].x and item.y == maze_list[i][j].y):
                        unvisited_neighbor[k].Neighbor_Count = counter
                        unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                        unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
              """          
    if j > 0:
        if mazeMap[i][j-1].Checked == False:    
            #if bottomWall(mazeMap[i][j]) == False and mazeMap[i][j-1].Checked == False:
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i][j-1])
                """if (mazeMap[i][j-1] not in unvisited_neighbor):
                maze_list[i][j-1].Neighbor_X = maze_list[i][j].x
                maze_list[i][j-1].Neighbor_Y = maze_list[i][j].y
                #maze_list[i][j-1].Neighbor_Count = maze_list[i][j].Count
                maze_list[i][j-1].Neighbor_Count = counter
                unvisited_neighbor.append(mazeMap[i][j-1])
            else:
                for k, item in reversed(list(enumerate(unvisited_neighbor))):
                    if (item.x == maze_list[i][j].x and item.y == maze_list[i][j].y):
                        unvisited_neighbor[k].Neighbor_Count = counter
                        unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                        unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
                    """
    if i > 0:
        if mazeMap[i-1][j].Checked == False:    
            #if leftWall(mazeMap[i][j]) == False and mazeMap[i-1][j].Checked == False:
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i-1][j])
                """if (mazeMap[i-1][j] not in unvisited_neighbor):
                maze_list[i-1][j].Neighbor_X = maze_list[i][j].x
                maze_list[i-1][j].Neighbor_Y = maze_list[i][j].y
                #maze_list[i-1][j].Neighbor_Count = maze_list[i][j].Count
                maze_list[i-1][j].Neighbor_Count = counter
                unvisited_neighbor.append(mazeMap[i-1][j])
            else:
                for k, item in reversed(list(enumerate(unvisited_neighbor))):
                    if (item.x == maze_list[i-1][j].x and item.y == maze_list[i-1][j].y):
                        unvisited_neighbor[k].Neighbor_Count = counter
                        unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                        unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
                        """
    if i <15:
        if mazeMap[i+1][j].Checked == False:    
            #if rightWall(mazeMap[i][j]) == False and mazeMap[i+1][j].Checked == False:
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i+1][j])
                """if (mazeMap[i+1][j] not in unvisited_neighbor):
                maze_list[i+1][j].Neighbor_X = maze_list[i][j].x
                maze_list[i+1][j].Neighbor_Y = maze_list[i][j].y
                #maze_list[i+1][j].Neighbor_Count = maze_list[i][j].Count
                maze_list[i+1][j].Neighbor_Count = counter
                unvisited_neighbor.append(mazeMap[i+1][j])
            else:
                for k, item in reversed(list(enumerate(unvisited_neighbor))):
                    if (item.x == maze_list[i][j].x and item.y == maze_list[i+1][j].y):
                        unvisited_neighbor[k].Neighbor_Count = counter
                        unvisited_neighbor[k].Neighbor_X = maze_list[i][j].x
                        unvisited_neighbor[k].Neighbor_Y = maze_list[i][j].y
                        """
    return neighbor

"""        
maze_list[7][7].Top = False
maze_list[7][7].Right = False
maze_list[7][8].Top = False
maze_list[7][8].Right = False
maze_list[8][7].Top = False
maze_list[8][7].Left = False
maze_list[8][8].Top = False
maze_list[8][8].Bottom = False
maze_list[8][8].Left = False
"""
        
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
        maze_list[i][j].x = i
        maze_list[i][j].y = j
        
i = 0
j = 0
counter = 0
k = 0
printMaze(maze_list)

while k < (len(maze_list)*len(maze_list)-1):
    Path = []
    time.sleep(.5)
    counter = counter +1                
    maze_list[i][j].Count = counter
    maze_list[i][j].Checked = True
    printMaze(maze_list)
    if  len(unvisited_neighbor) !=0:
        print(str(unvisited_neighbor[-1].x) + "," + str(unvisited_neighbor[-1].y))
    #time.sleep(1)
    #Shortest = 1000
    if maze_list[i][j] in unvisited_neighbor:
        unvisited_neighbor.remove(maze_list[i][j])
    if availableNeighbor(maze_list,i,j):
        visited_Stack.append(maze_list[i][j])
        if i<15:
            if maze_list[i+1][j].Checked != True:
        #if maze_list[i][j].Right !=True and maze_list[i+1][j].Checked !=True:
            ##Shortest = maze_list[i+1][j].Distance
            ##Temp = maze_list[i][j].Distance
                Path.append('right')
        if i >0:
            if maze_list[i-1][j].Checked != True:
        #if maze_list[i][j].Left !=True and maze_list[i-1][j].Checked !=True:
            ##Temp = maze_list[i-1][j].Distance 
            ##if Temp < Shortest:
               ## Shortest = Temp
                Path.append('left')
        if j <15:
            if maze_list[i][j+1].Checked != True:
        #if maze_list[i][j].Top !=True and maze_list[i][j+1].Checked !=True:
            ##Temp = maze_list[i][j+1].Distance
            ##if Temp < Shortest:
            ## Shortest = Temp
                Path.append('up')
        if j >0:
            if maze_list[i][j-1].Checked != True:
        #if maze_list[i][j].Bottom !=True and maze_list[i][j-1].Checked !=True:
            ##Temp = maze_list[i][j-1].Distance
            ##if Temp < Shortest:
              ## Shortest = Temp
                Path.append('down')
        
        if len(Path) > 0:
            destination = random.choice(Path)
        
        if destination == 'up':
            maze_list[i][j].Top = False
            maze_list[i][j+1].Bottom = False
            j = j+1
        elif destination == 'down':
            maze_list[i][j].Bottom = False
            maze_list[i][j-1].Top = False
            j = j-1
        elif destination == 'right':
            maze_list[i][j].Right = False
            maze_list[i+1][j].Left = False
            i = i +1
        elif destination == 'left':
            maze_list[i][j].Left = False
            maze_list[i-1][j].Right = False
            i = i -1
        k = k+1
        
    elif len(visited_Stack) !=0:
            i = visited_Stack[-1].x
            j = visited_Stack[-1].y 
            visited_Stack.pop()