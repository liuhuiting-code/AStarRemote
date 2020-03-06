# -*- coding: utf-8 -*-
"""
Created on Mon Sep 9 19:25:08 2018

@author: duxiaoqin

Functions:
    (1) Array class;
"""

import random
import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, 'Array size must be > 0'
        self.size = size
        PyArrayType = ctypes.py_object * size
        self.elements = PyArrayType()
        self.clear(None)
        
    def clone(self):
        newa = Array(len(self))
        for index in range(len(self)):
            newa[index] = self[index]
        return newa
    
    def print(self):
        for index in range(len(self)):
            print(self.elements[index], end=' ')
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), \
               'Array subscript out of range'
        return self.elements[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), \
               'Array subscript out of range'
        self.elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value
            
    def __iter__(self):
        return ArrayIterator(self.elements)
    
class ArrayIterator:
    def __init__(self, theArray):
        self.arrayRef = theArray
        self.curNdx = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curNdx < len(self.arrayRef):
            entry = self.arrayRef[self.curNdx]
            self.curNdx = self.curNdx + 1
            return entry
        else:
            raise StopIteration
            
def main():
    a = Array(10)
    for i in range(len(a)):
        a[i] = random.random()
    a.print()
        
if __name__ == '__main__':
    main()