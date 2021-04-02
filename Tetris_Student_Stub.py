from random import randint
import msvcrt
import os, sys
from time import sleep, time
from enum import Enum
from colorama import Fore, Back, Style, init

if os.name == "nt":
    os.system("cls")
else:
    print(f"\033[2J ")

print("\033[?25l") # Hide cursor

BOARD_WIDTH = 30
BOARD_HEIGHT = 20 
BOARD_ROW = 1
BOARD_COL = 10
BLOCK_ROW = 1
BLOCK_COL = 15
ANIMATION_DELAY = 0.75 # 0.5 seconds

CHAR_IMG = "▓▓"
BLANK_IMG = "  "

BLOCK_IMGS = (
    (Fore.BLUE,
    ((0, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 1, 0, 0))),

    (Fore.RED,
    ((0, 0, 0, 0),
     (0, 1, 1, 0),
     (0, 1, 1, 0),
     (0, 0, 0, 0))),

    (Fore.GREEN,
    ((1, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 0, 0, 0))),

    (Fore.CYAN,
    ((0, 1, 1, 0),
     (0, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 0, 0, 0))),

    (Fore.MAGENTA,
    ((0, 1, 0, 0),
     (1, 1, 1, 0),
     (0, 0, 0, 0),
     (0, 0, 0, 0))),

    (Fore.LIGHTGREEN_EX,
    ((0, 1, 0, 0),
     (1, 1, 0, 0),
     (1, 0, 0, 0),
     (0, 0, 0, 0))),

    (Fore.LIGHTMAGENTA_EX,
    ((1, 0, 0, 0),
     (1, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 0, 0, 0))))

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class TetrisBlock:
    '''
    1. block shape
    2. block image
    3. block rotation
    4. block position on the screen

    Question: 
        - should the block object know the board dimension? so when rotate
          is called, it'll know NOT to rotate if it becomes out of bounds?
    '''
    def __init__(self,
                 image=None, # a tuple of color and 4x4 2D list of binary image of a block
                 pos_row=BLOCK_ROW,
                 pos_col=BLOCK_COL):
        pass

    def animate(self):
        ''' 
        animates the block by moving one row down
        should stop animating if the last row has reached the board_border
        '''
        pass
   
    def rotate(self, direction):
        '''
        rotates the block lef or right, need to pass in Direction Enum
        and must only be LEFT or RIGHT
        '''
        pass

    def clear(self):
        pass

    def print(self):
        pass

    def move(self, direction):
        pass

    def __str__(self):
        pass


class TetrisBoard:
    ''' 
    1. contains the blocks 
    2. knows the game screen dimension
    3. animates the screen
    4. removes the bottom line when they're completely filled 
        will remove up to the line that's not completely filled
    
    Implementation:
    1. dropped_blocks (a list of the blocks fallen to the bottom of the screen)
        - This list of blocks should be converted to raster images (for each line)
        - Sinc there's no rotation.  BUT, the "gaps" in the line can be filled
          by falling blocks
    2. falling_block: the block that's animating (falling) in the middle of the screen
    '''
    def __init__(
        self, 
        board_pos=(BOARD_ROW, BOARD_COL), 
        board_dimension=(BOARD_HEIGHT, BOARD_WIDTH),
        animation_delay=ANIMATION_DELAY):
        pass

    def play(self):
        pass

    def animate(self):
        '''
        1. animate the falling block down by one line
        2. clear the last rows (if more than one)
        '''
        pass

    def __str__(self):
        '''
        returns the text image of the board
        '''
        s = ""
        return s

class Tetris:
    '''
    owns 1. board
    plays the game
    '''
    def __init__(self):
        # creates a new board TetrisBoard
        # prints the board on the screen
        pass

    def play(self):
        '''
        Plays the tetris game

        1. checks for keyboard input: cursor up, down, left, right
            - calls TetrisBoard to play(direction)
        2. if no input, after a certain period, calls TetrisBoard.animate()
        '''
        pass


if __name__ == "__main__":
    block = TetrisBlock()
    block.print()

    '''
    sleep(1)
    block.rotate(Direction.LEFT)
    print(block)

    sleep(1)
    block.rotate(Direction.RIGHT)
    print(block)
    '''
    while True:
        if msvcrt.kbhit():
            c = msvcrt.getch()
            if c == b'\xe0':
                c = msvcrt.getch()
                if c == b'H':
                    print(Fore.GREEN+'\033[1;1H'+"up pressed     ")
                elif c == b'M':
                    print(Fore.GREEN+'\033[1;1H'+"right pressed    ")
                elif c == b'K':
                    print(Fore.GREEN+'\033[1;1H'+"left pressed     ")
                elif c == b'P':
                    block.rotate(Direction.DOWN)