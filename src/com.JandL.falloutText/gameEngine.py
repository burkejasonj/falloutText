import curses
from collections import deque
import io, json, os


class logicEngine:
    pass
    # TODO: break up input

    # TODO: define command interpreter by json files

    # TODO: parse commands without arguments first

    # TODO: parse commands with arguments last


class renderEngine:
    # define screen buffer

    screenBuffer = deque()

    # Define color defaults based on output level (WARN,INFO,ERROR,DEBUG)

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # WARN
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # INFO
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # ERROR
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)  # DEBUG

    # TODO: define calls to screen buffer

    # TODO: Process output level into proper formatting

<<<<<<< HEAD
    def writetoBuffer(message, row=0, column=0, outputLevel="INFO"):
        renderEngine.screenBuffer.append([message, [row, column]])
=======
        renderEngine.screenBuffer.append(
            [
                (
                    "\033[0m\033[3h"
                    + outputFormatting
                    + formatting
                    + message
                    + "\033[0m"
                ),
                [row, column],
            ]
        )
>>>>>>> 48add2c8f7260c5b3a9ea7fa3f4ce2f8f48af5d4

    #     renderEngine.screenBuffer.append([("\033[0m\033[3h" + outputFormatting + formatting + message + "\033[0m"),[row, column]])

    def executeBuffer():
        # Empty Buffer
        while not len(renderEngine.screenBuffer) <= 0:
            writeBuffer = renderEngine.screenBuffer.popleft()
            stdscr.addstr(writeBuffer[2][1], writeBuffer[2][2], writeBuffer[1])

    # TODO: define input calls and pass to logicEngine (LOOP)
