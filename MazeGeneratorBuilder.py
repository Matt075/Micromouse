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
    
    if j < 15:
        if mazeMap[i][j+1].Checked == False:    
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i][j+1])
         
    if j > 0:
        if mazeMap[i][j-1].Checked == False:    
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i][j-1])

    if i > 0:
        if mazeMap[i-1][j].Checked == False:    
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i-1][j])

    if i <15:
        if mazeMap[i+1][j].Checked == False:    
                neighbor = True
                count = count +1
                unvisited_neighbor.append(mazeMap[i+1][j])

    return neighbor


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
    time.sleep(.1)
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
                Path.append('right')
        if i >0:
            if maze_list[i-1][j].Checked != True:
                Path.append('left')
        if j <15:
            if maze_list[i][j+1].Checked != True:
                Path.append('up')
        if j >0:
            if maze_list[i][j-1].Checked != True:
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