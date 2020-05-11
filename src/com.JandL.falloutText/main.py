import curses
import gameEngine as engine
import io, json, os


def getRules(stdscr, rulesetManifest):

    stdscr.refresh()
    slotID = stdscr.getkey()

    # Attempt get ruleset object from json

    try:
        rules = io.open(
            rulesetManifest["availableGames"]["slot" + slotID]["manifestLocation"]
        )
        rules = json.load(rules)
    except KeyError:
        stdscr.addstr(1, 2, "Please enter a number, silly", curses.color_pair(3))
        stdscr.refresh()
        rules = getRules(stdscr, rulesetManifest)

    return rules


def main(stdscr):
    # Clear screen
    stdscr.clear()
    # Debug Bar
    stdscr.addstr(
        0,
        0,
        "COLOR SUPPORT: "
        + str(curses.has_colors())
        + " FULL COLOR SUPPORT: "
        + str(curses.can_change_color())
        + " SUPPORTED COLORS: "
        + str(curses.COLORS)
        + " SUPPORTED COLOR PAIRS: "
        + str(curses.COLOR_PAIRS)
        + " LINES: "
        + str(curses.LINES)
        + " COLUMNS: "
        + str(curses.COLS),
        curses.color_pair(5),
    )

    # Define color defaults based on output level (WARN,INFO,ERROR,DEBUG)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # WARN
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # INFO
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # ERROR
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)  # DEBUG
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_WHITE)  # DEBUG-BAR

    # Load rulesetManifest
    rulesetManifest = io.open("rulesets/manifest.json", "r")
    rulesetManifest = json.load(rulesetManifest)

    # User prompt on what to do
    stdscr.addstr(2, 2, "Select a game:")

    # List possible games
    for slot in rulesetManifest["availableGames"]:

        stdscr.addstr(
            int(slot.replace("slot", "")) + 3,
            3,
            slot.replace("slot", "")
            + ". "
            + rulesetManifest["availableGames"][slot]["callName"],
        )

    # Ask player for ruleset to use and retrieve it from json
    rules = getRules(stdscr, rulesetManifest)

    # Clear screen and add debug info for game
    stdscr.clear()
    stdscr.addstr(
        1,
        2,
        rules["gameInfo"]["title"]
        + " Version "
        + rules["gameInfo"]["version"]
        + " Branch "
        + rules["gameInfo"]["branch"],
        curses.color_pair(4),
    )
    stdscr.addstr(2, 2, "Rules by " + rules["gameInfo"]["author"], curses.color_pair(4))

    # Test area for pre-game init

    pc = engine.logicEngine.createCharacter("TEST")

    # Test area for game loop



    stdscr.refresh()
    stdscr.getkey()


curses.wrapper(main)
