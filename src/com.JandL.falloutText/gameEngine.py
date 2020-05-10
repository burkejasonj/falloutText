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

    # TODO: define calls to screen buffer

    # TODO: Process output level into proper formatting

    def writetoBuffer(message="", row=0, column=0, outputLevel="INFO"):
        # TODO: Add formatting support
        if outputLevel == "WARN":
            colorPair = 1
        elif outputLevel == "INFO":
            colorPair = 2
        elif outputLevel == "ERROR":
            colorPair = 3
        elif outputLevl == "DEBUG":
            colorPair = 4

        renderEngine.screenBuffer.append([message, [row, column], colorPair])

    def executeBuffer(stdscr):
        # Empty Buffer
        while not len(renderEngine.screenBuffer) <= 0:
            writeBuffer = renderEngine.screenBuffer.popleft()
            stdscr.addstr(
                writeBuffer[1][0],
                writeBuffer[1][1],
                writeBuffer[0],
                curses.color_pair(writeBuffer[2]),
            )

    # TODO: define input calls and pass to logicEngine (LOOP)
