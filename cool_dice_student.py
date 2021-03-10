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

colors = [Fore.BLUE, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, 
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTCYAN_EX,
          Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX]

if __name__ == "__main__":
    pass
