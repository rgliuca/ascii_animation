import msvcrt
import os, sys
import random
from time import sleep
from colorama import Fore, Back, Style, init 
#from getkey import getch  


init()  

boulder = [ ' O ',
            'OOO',
            ' O ']

car = [ 'Ö▓▓▓▓▓Ö',
        ' ▓▓░▓▓ ',
        ' ▓░Ö░▓ ',
        'Ö▓▓▓▓▓Ö']
    
car_row=40
car_col=20

# for windows OS 
if os.name =="nt": 
    os.system("cls")
    
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))


try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        """getch() -> key character
        Read a single keypress from stdin and return the resulting character. 
        Nothing is echoed to the console. This call will block if a keypress 
        is not already available, but will not wait for Enter to be pressed. 
        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#from getkey import getch

while True:
    c = getch()
    print(c[0], ":", ord(c[0]))
    if ord(c[0]) == 3:
        break
        
    if ord(c[0]) == 49:
        print("The '1' key was pressed")
        # most likely the '1' key was pressed 
