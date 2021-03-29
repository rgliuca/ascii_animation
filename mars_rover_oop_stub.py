import msvcrt
import os, sys
import random
from time import sleep
from colorama import Fore, Back, Style, init 

init()  

BOULDER_IMAGE = [' O ',
                 'OOO',
                 ' O ']

ROVER_IMAGE = ['Ö▓▓▓▓▓Ö',
               ' ▓▓░▓▓ ',
               ' ▓░Ö░▓ ',
               'Ö▓▓▓▓▓Ö']
    
rover_row = 15
rover_col = 20

# clear the screen for Linux/Mac and Windows
if os.name == "nt":
    os.system("cls")
else:
    print(f"\033[2J ")

print("\033[?25l") # Hide the cursor

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


for n, line in enumerate(ROVER_IMAGE):
    print(Fore.RED+'\033[{};{}H'.format(rover_row + n, rover_col) + line)

while True:
    c = getch()
    print(c[0], ":", ord(c[0]))
    if ord(c[0]) == 3:
        break
        
    if ord(c[0]) == 49:
        print("The '1' key was pressed")
        # most likely the '1' key was pressed
