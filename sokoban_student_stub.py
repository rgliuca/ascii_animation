from random import randint
import msvcrt
import os, sys, time
from enum import Enum
from colorama import Fore, Back, Style, init 

TOTAL_GOALS = 3
BOARD_DISP_ROW = 5
BOARD_DISP_COL = 20 
BOARD_WIDTH = 16
BOARD_HEIGHT = 8 
BLANK_IMG = ' '
BLOCK_IMG = '▓'
GOAL_IMG = 'X'
PLAYER_IMG = 'Ö' # player
WALL_IMG = '▒'
game_board = [[BLANK_IMG] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

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
    row = 10
    col = 15
    #print(Fore.RED + f'\033[{row};{col}H' + 'Hello World')
    pass

def move_object(board, row, col, direction, obj):
    ''' 
    checks if object can be moved from current pos (row, col) to 
    the direction specified.  If the move is possible, the object is
    moved and returns True, otherwise return False and the object is 
    not moved
    '''
    pass

def get_object(board, row, col):
    '''
    Returns the object occupied in the given pos (row, col)
    If the pos (row, col) is out of bounds, the wall is returned!
    '''
    # If the pos (row, col) is out of bounds, the wall is returned!
    # If the pos (row, col) is a box, return the box text
    # if the pos (row, col) is empty, return the empty img
    # If the pos (row, col) is goal, return the goal img
    
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
