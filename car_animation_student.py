import os, sys
import random
from time import sleep
from colorama import Fore, Back, Style, init 
from getkey import getch  

init()  

car=[ 'Ö▓▓▓▓▓Ö',
      ' ▓▓░▓▓ ',
      ' ▓░Ö░▓ ',
      'Ö▓▓▓▓▓Ö']
    
car_row=40
car_col=20

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

for n, line in enumerate(car):
  print(Fore.RED+'\033[{};{}H'.format(car_row+n, car_col)+' '+line+' ')
