from random import randint
import msvcrt
import os, sys, time
from enum import Enum
from colorama import Fore, Back, Style, init 

TOTAL_GOALS = 3
BOARD_POS_ROW = 5
BOARD_POS_COL = 20 
BOARD_WIDTH = 16
BOARD_HEIGHT = 8 
BLANK_IMG = ' '
BLOCK_IMG = '▓'
GOAL_IMG = 'X'
PLAYER_IMG = 'Ö' # player
WALL_IMG = '▒'
game_board = [[blank] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def randomly_place_object(board, obj):
    pass

def print_wall():
    pass

def print_board(board):
    pass

def move_object(board, row, col, direction, obj):
    ''' 
    checks if object can be moved from current pos (row, col) to 
    the direction specified.  If the move is possible, the object is
    moved and returns True, otherwise return False and the object is 
    not moved
    '''
    pass

# for windows OS 
os.system("cls")

import msvcrt
import ctypes

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]
ci = _CursorInfo()
handle = ctypes.windll.kernel32.GetStdHandle(-11)
ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
ci.visible = False
ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
