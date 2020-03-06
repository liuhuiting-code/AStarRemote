# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:46:53 2018

@author: duxiaoqin
Functions:
    (1)Maze class
"""
from priorityqueue import *
from random import *
from myarray2d import Array2D
import queue
import math
from mazedraw import *
start=(0,0)
class Maze:
    EMPTY = 0
    OBSTACLE = -1
    OCCUPIED = 1
    start = (0, 0)
   
    came_from={}
    def __init__(self, width, height):
        seed()
        self.maze = Array2D(width, height)
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.maze.clear(Maze.EMPTY)
        
        for count in range(int(width*height*0.1)):
            row = int(random()*100 % height)
            col = int(random()*100 % width)
            if (row, col) == self.start or (row, col) == self.goal:
                continue
            self.maze[row, col] = Maze.OBSTACLE
            
    def __getitem__(self, ndxTuple):
        return self.maze.__getitem__(ndxTuple)
    
    def __setitem__(self, ndxTuple, value):
        self.maze.__setitem__(ndxTuple, value)
        
    def getAllMoves(self, row, col):
        width = self.numCols()
        height = self.numRows()
        moves = []
        offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for x, y in offsets:
            x = col + x
            y = row + y
            if x < 0 or x > width-1 or \
               y < 0 or y > height-1:
                continue
            if self.maze[y, x] == Maze.EMPTY:
                moves.append((y, x))
        return moves
        
    def numRows(self):
        return self.maze.numRows()
    
    def numCols(self):
        return self.maze.numCols()

    def dfs(x,y,step):
        x=0
        y=0
        step=0
        
        
        
    def print(self):
        rows = self.numRows()
        cols = self.numCols()
        for row in range(rows):
            for col in range(cols):
                if self.maze[row, col] == Maze.EMPTY:
                    print('_', end=' ')
                elif self.maze[row, col] == Maze.OBSTACLE:
                    print('|', end=' ')
                else:
                    print('O', end=' ')
            print()

    def AStar(maze,v,came_from):
        frontier = PriorityQueue()
        goal=(19,19)
        frontier.enqueue(v,0)
        came_from[v]=None
        cost_so_far={}
        cost_so_far[v]=0
        while not frontier.is_empty():
            v=frontier.dequeue()
            if(maze[v[0],v[1]]==Maze.EMPTY):
                if v[0]==maze.goal[0]&v[1]==maze.goal[1]:
                    return v
                else:
                    maze[v[0],v[1]]=Maze.OCCUPIED;
                    moves=[]
                    moves=maze.getAllMoves(v[0],v[1])
                    newcost=cost_so_far[v]+1
                    for w in moves:
                        if(maze[w[0],w[1]]==0):
                            if(w not in cost_so_far or newcost<cost_so_far[w]):
                                cost_so_far[w]=newcost
                                frontier.enqueue(w,newcost+maze.heuristic(w,goal))
                                came_from[w]=v
        return None
    def heuristic(self, a, b):
        #return abs(a[0] - b[0]) + abs(a[1] - b[1])
        x=abs(a[0]-b[0])
        y=abs(a[1]-b[1])
        return math.sqrt(x*x+y*y)  
def main():
    win = GraphWin('MazeDraw', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    nextnode=Maze.AStar(maze,maze.start,maze.came_from)
    if(nextnode == None):
        print("not found right path")
    else:
        print("found the path")
    print()
    while maze.came_from[nextnode]!=None:
        print(maze.came_from[nextnode])
        nextnode=maze.came_from[nextnode]
        maze[nextnode[0],nextnode[1]]=3

    mazedraw = MazeDraw(win, maze)

    while win.checkKey() != 'Escape':
        mazedraw.draw()
    win.close()

if __name__ == '__main__':
    main()
