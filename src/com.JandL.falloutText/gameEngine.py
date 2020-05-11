import curses
from collections import deque
import io, json, os


class logicEngine:
    pass
    # TODO: break up input

    # TODO: define command interpreter by json files

    # TODO: parse commands without arguments first

    # TODO: parse commands with arguments last

    # TODO: define input calls


class renderEngine:
    # Define screen buffer
    screenBuffer = deque()

    # define calls to screen buffer
    def writetoBuffer(message="", row=0, column=0, outputLevel="INFO"):
        # Formatting support
        if outputLevel == "WARN":
            colorPair = 1
        elif outputLevel == "INFO":
            colorPair = 2
        elif outputLevel == "ERROR":
            colorPair = 3
        elif outputLevl == "DEBUG":
            colorPair = 4

        # Add to queue for screenBuffer
        renderEngine.screenBuffer.append([message, [row, column], colorPair])

    def executeBuffer(stdscr):
        # Clear Screen
        stdscr.clear()

        # Write contents of buffer to screen memory
        while not len(renderEngine.screenBuffer) <= 0:
            writeBuffer = renderEngine.screenBuffer.popleft()
            stdscr.addstr(
                writeBuffer[1][0],
                writeBuffer[1][1],
                writeBuffer[0],
                curses.color_pair(writeBuffer[2]),
            )

        # Refresh screen
        stdscr.refresh()
