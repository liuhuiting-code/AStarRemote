# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:02:19 2018

@author: duxiaoqin
Functions:
    (1)MazeDraw class
"""

from graphics import *
from maze import *

class MazeDraw:
    def __init__(self, win, maze):
        self.width = maze.numCols()
        self.height = maze.numRows()
        self.win = win
        self.win.setCoords(0.0, 0.0, self.width + 2, self.height + 2)
        
        self.rect_points = []
        for row in range(self.height):
            for col in range(self.width):
                point1 = Point(col+1, self.height-row)
                point2 = Point(col+1+1, self.height-row+1)
                if maze[row, col] == Maze.EMPTY:
                    color = 'green'
                if maze[row, col] == Maze.OBSTACLE:
                    color = 'blue'
                if maze[row, col] == Maze.OCCUPIED:
                    color = 'red'
                if maze[row, col] == 3:
                    color = 'yellow'
                self.rect_points.append((point1, point2, color))
        self.rectangles = []
        for p1, p2, color in self.rect_points:
            rect = Rectangle(p1, p2)
            rect.setFill(color)
            self.rectangles.append(rect)
        
    def draw(self):
        for rect in self.rectangles:
            rect.undraw()
        for rect in self.rectangles:
            rect.draw(self.win)
        update(30)
                
def main():
    win = GraphWin('MazeDraw', 600, 600, autoflush=False)
    maze = Maze(20, 20)
    maze.print()
    mazedraw = MazeDraw(win, maze)

    while win.checkKey() != 'Escape':
        mazedraw.draw()
    win.close()
    
if __name__ == '__main__':
    main()
