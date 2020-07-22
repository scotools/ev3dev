#!/usr/bin/env python

from array import *
import random


class Cell():
    def __init__(self,f,g,h,x=0,y=0,label=""):
        self.x=x
        self.y=y
        self.f=f
        self.g=g
        self.h=h
        self.label = label

    def __str__(self):
        return "[%d,%d], f: %d, g: %d, h: %d, label: %s" % \
            (self.x, self.y, self.f, self.g, self.h, self.label)


class Grid():
    def __init__(self,col,row,init=0):
        self.col = col
        self.row = row
        self.init = init
        self.matrix = [[Cell(0,0,0,y,x) for x in range(row)] for y in range(col)]
           
    def setlabel(self,x,y,label):
        print(F"Setting [{x},{y}] label {label}")
        self.matrix[x][y].label = label
        print(F"Cell: {self.matrix[x][y]}")

    def print(self):
        print(F"Dim: {self.col}, {self.row}")
        for i in range(0,self.col):
            row_str=""
            for j in range(0,self.row):
                cell = self.matrix[i][j]
                label = str(cell.label)
                if label != "":
                    row_str += "|" + label 
                else:
                  val = cell.g + cell.h
                  row_str += "|" + str(val)
                if j == r-1:
                    row_str += "|"
            print(F"{row_str}")


if __name__ == '__main__':
    print("Hello")
    # initialize a 2D array
    
    c,r = 10,10
    grid = Grid(c,r)

    grid.print()

    obsticals = random.randint(5,9)
    for i in range(0,obsticals):
        grid.setlabel(random.randint(0,9),random.randint(0,9),"#")

    grid.setlabel(0,3,"S")
    grid.setlabel(9,7,"E")
    
    grid.print() 


