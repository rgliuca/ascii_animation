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
    
print(Fore.GREEN + f'\033[{1};{15}H'+'Hello World')
  
for i in range(1,10):
  print(Fore.GREEN + f'\033[{i};{15}H' + 'Hello World')
  sleep(1)

for i in range(1,10):
  print(Fore.RED + f'\033[{i};{15}H' + 'Hello World')
  sleep(1)
