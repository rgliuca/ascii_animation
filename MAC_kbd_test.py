from kbd import KBD

kbd = KBD()
while True:
    if kbd.kbhit():
        ch = kbd.getch()

        if ch == 'a':
            print("It's an \"a\"")
        else:
            print("I got", ch)
