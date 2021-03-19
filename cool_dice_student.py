from time import sleep
from colorama import Fore, Style, init
from random import randint
import os

DICE_IMG = ["---------\n",
            ["|       |\n",
             "|   O   |\n",
             "|       |\n"],
            ["| O     |\n",
             "|       |\n",
             "|     O |\n"],
            ["| O     |\n",
             "|   O   |\n",
             "|     O |\n"],
            ["| O   O |\n",
             "|       |\n",
             "| O   O |\n"],
            ["| O   O |\n",
             "|   O   |\n",
             "| O   O |\n"],
            ["| O   O |\n",
             "| O   O |\n",
             "| O   O |\n"]]

init()

# clear the screen 
if os.name == "nt":
    os.system("cls")
else:
    print(f"\033[2J ")


class Dice:
    def __init__(self, row=1, col=1, color=Fore.RED):
        pass
    
    def roll(self):
        pass

    def set_color(self, color):
        pass

    def set_position(self, row, column):
        pass

    def print(self):
        pass

    '''
    You don't need to implement __str__ method for now
    '''
    def __str__(self):
        pass


if __name__ == "__main__":
    pass
