#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class Token(Enum):
    CROSS = 1
    CIRCLE = 2


class Point():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Board():

    __COLUMN = 3  # X
    __ROW = 3  # Y

    def __init__(self):
        '''
        ToDo: try with Numpy array for better performance ?
        '''
        self._grid = [[None for x in range(Board.__COLUMN)]
                      for x in range(Board.__ROW)]
        self._free_cell_count = Board.__COLUMN * Board.__ROW

    def has_free_cell(self):
        return self._free_cell_count > 0
    
    @property
    def grid(self):
        return self._grid

    def play(self, point, token):

        if point.x >= Board.__COLUMN or point.y >= Board.__ROW:
            return False

        # Check free cell
        if self._grid[point.x][point.y] is not None:
            return False

        # Add token to grid
        self._grid[point.x][point.y] = token
        self._free_cell_count -= 1

        return True

    def undo(self, point):
        if point.x >= Board.__COLUMN or point.y >= Board.__ROW:
            return False

        self._grid[point.x][point.y] = None
        self._free_cell_count += 1

        return True
