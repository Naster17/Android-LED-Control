import os 
import curses
import time
import random

def torch_on():
    os.popen("echo 0 > /sys/class/leds/red/brightness")
    os.popen("echo 255 > /sys/class/leds/red/brightness")

def torch_off():
    os.popen("echo 0 > /sys/class/leds/red/brightness")

def flashlight_on():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")
    os.popen("echo 255 > /sys/class/leds/flashlight/brightness")

def flashlight_off():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")


def disco(stdscr):
    curses.curs_set(0)

    max_y, max_x = stdscr.getmaxyx()

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)
    curses.init_pair(6, curses.COLOR_CYAN, -1)

    colors = [curses.color_pair(i) for i in range(1, 7)]

    while True:
        stdscr.clear()

        try:
            for i in range(75):
                x = random.randint(0, max_x - 1)
                y = random.randint(0, max_y - 1)
                color = random.choice(colors)
                stdscr.addstr(y, x, u'0'.encode('utf-8'), color)
        except:
            pass
        
        stdscr.refresh()
        
        # Controling 
        time.sleep(0.1)
        flashlight_on()
        torch_off()
        time.sleep(0.1)
        flashlight_off()
        torch_on()

curses.wrapper(disco)