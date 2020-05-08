from colorama import init
from colorama import Fore, Back, Style
from collections import deque
import io, json, os


class logicEngine:
    pass
    # TODO: break up input

    # TODO: define command interpreter by json files

    # TODO: parse commands without arguments first

    # TODO: parse commands with arguments last


class renderEngine:
    # TODO: define screen buffer

    screenBuffer = deque()

    # TODO: define color defaults based on output level (WARN,INFO,ERROR,DEBUG)

    class outputLevel:
        WARN = Fore.YELLOW + Style.BRIGHT
        INFO = Fore.WHITE + Style.BRIGHT
        ERROR = Fore.RED + Style.DIM
        DEBUG = Fore.CYAN + Style.NORMAL

    # TODO: define calls to screen buffer

    def writetoBuffer(message, row=0, column=0, outputLevel="INFO", formatting=""):
        # Process output level into proper formatting
        if outputLevel == "INFO":
            outputFormatting = renderEngine.outputLevel.INFO
        elif outputLevel == "WARN":
            outputFormatting = renderEngine.outputLevel.WARN
        elif outputLevel == "ERROR":
            outputFormatting = renderEngine.outputLevel.ERROR
        elif outputLevel == "DEBUG":
            outputFormatting = renderEngine.outputLevel.DEBUG

        renderEngine.screenBuffer.append([("\033[0m\033[3h" + outputFormatting + formatting + message + "\033[0m"),[row, column]])

    # TODO: write to screen (LOOP)

    def executeBuffer():

        # TODO: add reset commands

        # empty screenBuffer
        while not len(renderEngine.screenBuffer) <= 0:
            print(renderEngine.screenBuffer.popleft())

    # TODO: define input calls and pass to logicEngine (LOOP)
