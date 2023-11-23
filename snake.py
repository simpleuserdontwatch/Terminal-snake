import curses,random,ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Terminal snake")
def main(stdscr):
    curses.curs_set(0)
    curses.resize_term(25,35)
    stdscr.clear()
    stdscr.keypad(1)
    applepos     = [10, 10]
    snakepos     = [2, 2]
    snakeheading = [1, 0]
    segments = []
    length = 2

    stdscr.border()
    stdscr.addstr(10, 6, 'Terminal snake!')
    stdscr.addstr(11, 6, 'Press any key to play')
    stdscr.refresh()
    stdscr.getkey()
    

    stdscr.nodelay(1)
    while True:
        stdscr.clear()
        for i in segments:
            stdscr.addstr(i[1],i[0], '#')
        if snakepos[0] < 0:
            snakepos[0] = 34
        if snakepos[1] < 0:
            snakepos[1] = 24
        if snakepos[0] > 34:
            snakepos[0] = 0
        if snakepos[1] > 24:
            snakepos[1] = 0
        stdscr.addstr(*snakepos[::-1], '@')
        stdscr.addstr(*applepos[::-1], 'O')
        stdscr.border()
        stdscr.addstr(0, 2, 'Terminal snake!')
        stdscr.addstr(0, 35-len('Score: '+str(length-2))-2, 'Score: '+str(length-2))
        stdscr.refresh()
        segments.append(snakepos.copy())
        if len(segments) > length:
            segments.pop(0)
        snakepos[0] += snakeheading[0]
        snakepos[1] += snakeheading[1]
        if snakepos in segments:
            stdscr.nodelay(0)
            stdscr.addstr((35//2)-3, (25//2)-2, 'Gameover!')
            stdscr.addstr((35//2)-2, (25//2)-2, 'Press any key')
            stdscr.getkey()
            break
        if snakepos == applepos:
            length+=1
            applepos = [random.randint(2,32),random.randint(2,22)]
        char = stdscr.getch()
        if char == ord('q'): break
        elif char == curses.KEY_DOWN and snakeheading != [0,-1]: snakeheading = [0,1]
        elif char == curses.KEY_UP and snakeheading != [0,1]: snakeheading = [0,-1]
        elif char == curses.KEY_LEFT and snakeheading != [1,0]: snakeheading = [-1,0]
        elif char == curses.KEY_RIGHT and snakeheading != [-1,0]: snakeheading = [1,0]
        curses.napms(100)

curses.wrapper(main)
