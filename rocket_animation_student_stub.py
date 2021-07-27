import os, sys
from time import sleep
from colorama import Fore, init
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear screen command as function of OS
    command = 'cls' if system_name().lower()=='windows' else 'clear'

    # Action
    system_call([command])
    
class TermPos:
    def __init__(self, row, col):
        self._row = row
        self._col = col
    
    def __str__(self):
        return f"\033[{self._row};{self._col}H"
   
    def __add__(self, other):
        return str(self) + str(other)

    def __radd__(self, other):
        return self + other


init() 

rocket=['     |      ',
        '     ^      ',
        '    / \     ',
        '   /   \    ',
        '  /_____\   ',
        '  |N    |   ',
        '  |A    |   ',
        '  |S    |   ',
        '  |A    |   ',
        '  /     \   ',
        ' / /| |\ \  ',
        '/_/ |_| \_\ ']
    

# for windows OS 
if os.name =="nt": 
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

    
# Students, start your animation code from here:

print(Fore.GREEN + TermPos(1, 15) +'Hello World')

  
for i in range(1,10):
  print(Fore.GREEN + TermPos(i, 15) + 'Hello World')
  sleep(1)

for i in range(1,10):
  print(Fore.RED + TermPos(i, 15) + 'Hello World')
  sleep(1)
