import curses
import io, json, os

def main(stdscr):
    # Clear screen
    stdscr.clear()

    rulesetManifest = io.open("rulesets/manifest.json", "r")
    rulesetManifest = json.load(rulesetManifest)

    stdscr.addstr(1,2,"Select a game:")

    for slot in rulesetManifest["availableGames"]:

        stdscr.addstr(int(slot.replace("slot",""))+2,2,slot.replace("slot","")+". "+rulesetManifest["availableGames"][slot]["callName"])

        stdscr.refresh()
        slotID = stdscr.getkey()

        # Get ruleset object from json

        for slot in rulesetManifest["availableGames"]:
            if rulesetManifest["availableGames"]["slot"+slotID]["callName"] == rulesetManifest["availableGames"][slot]["callName"]:
                # TODO: Add try/except for ruleset.json
                rules = io.open(rulesetManifest["availableGames"][slot]["manifestLocation"])
                rules = json.load(rules)
                break
            else:
                continue

        stdscr.clear()
        stdscr.addstr(1,2,rules["gameInfo"]["title"]+" Version "+str(rules["gameInfo"]["version"])+" Branch "+rules["gameInfo"]["branch"])
        stdscr.addstr(2,2,"Rules by "+rules["gameInfo"]["author"])

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
