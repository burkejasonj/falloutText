import curses
from collections import deque
import io, json, os


class logicEngine:
    # TODO: init classes
    class playerCharacter:
        def __init__(self, name, lvl, _class, attributes):
            self.name = name
            self.lvl = lvl
            self._class = _class
            self.attributes = attributes

        def createCharacter(characterType="NPC"):
            if characterType == "PC":
                pass
            elif characterType == "NPC":
                pass
            else:
                raise ValueError

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
        elif outputLevel == "DEBUG":
            colorPair = 4
        elif outputLevel == "DEBUG-BAR":
            colorPair = 5

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
