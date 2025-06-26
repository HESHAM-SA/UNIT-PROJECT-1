import curses, threading, time
from art import text2art

exit_event = threading.Event()

def animate_header(win):
    art_text = text2art("WELLCOME", font='alligator2')
    color_id = 1
    while not exit_event.is_set():
        try:
            win.erase()
            # Cycle through 6 colors and apply a BOLD style
            win.addstr(0, 0, art_text, curses.color_pair(color_id) | curses.A_BOLD)
            win.refresh()
            color_id = (color_id % 6) + 1
            time.sleep(0.5)
        except: pass # Ignore errors to keep it short

def app(stdscr):
    # Setup colors
    curses.start_color()
    curses.use_default_colors()
    for i in range(6):
        curses.init_pair(i + 1, i + 1, -1) # Assign pairs 1-6 to colors 1-6

    # Create windows (header_win for art, stdscr for input)
    header_win = curses.newwin(8, curses.COLS, 0, 0)
    threading.Thread(target=animate_header, args=(header_win,), daemon=True).start()

    # Get input from user
    stdscr.addstr(9, 2, 'What is your name? ')
    curses.echo()
    curses.curs_set(1)
    user_name = stdscr.getstr(9, 22).decode()
    curses.noecho()
    curses.curs_set(0)

    # Show final message and wait for exit
    stdscr.addstr(11, 2, f'Hello {user_name}, nice to see you here!')
    stdscr.addstr(13, 2, 'Press any key to exit...')
    stdscr.getch()
    exit_event.set()

curses.wrapper(app)