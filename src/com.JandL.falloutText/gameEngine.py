import json
import io
import os
from collections import deque


class logicEngine:
    pass
    # TODO: break up input

    # TODO: define command interpreter by json files

    # TODO: parse commands without arguments first

    # TODO: parse commands with arguments last


class renderEngine:
    # TODO: define screen buffer

    screenBuffer = deque([])

    # TODO: define color defaults based on output level (WARN,INFO,ERROR,DEBUG)

    class outputLevel:
        WARN = "\033[31;40m"
        INFO = ""
        ERROR = ""
        DEBUG = ""

    # TODO: define calls to screen buffer

    def writetoBuffer(message, row=0, column=0, outputLevel="INFO", formatting=""):
        # TODO: Process output level into proper formatting
        screenBuffer.append(
            {
                ("\033[0m\033[3h" + formatting + message + "\033[0m"),
                [row, column],
            }
        )

    # TODO: write to screen (LOOP)

    # TODO: define input calls and pass to logicEngine (LOOP)
