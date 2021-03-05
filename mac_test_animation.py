from time import sleep
import sys, os

if os.name == "nt":
    os.system("cls")
else:
    print(f"\033[2J ")

delay = 0.5
r = 10 # 1-indexed
c = 50 # 1-indexed

print("\033[?25l") # Hide cursor

for i in range(10):
    # Clear screen, move to position, write character.
    #print(f"\033[2J \033[{r};{c}H" + str(i))
    print(f"\033[{r};{c}H" + str(i))
    sleep(delay)
