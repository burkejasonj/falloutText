import json
import io
import os


def main():
    # TODO: init variables

    # Init screen

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Ask for ruleset name and version

    rulesetManifest = io.open("rulesets/manifest.json", 'r')
    rulesetManifest = json.load(rulesetManifest)
    print("Please select one of the following:")
    for slot in rulesetManifest['availableGames']:
        print(rulesetManifest['availableGames'][slot]['callName'])
    slotID = input("? ")

    # Get ruleset object from json

    for slot in rulesetManifest['availableGames']:
        if slotID == rulesetManifest['availableGames'][slot]['callName']:
            # TODO: Add try/except for manifest.json
            rules = io.open(rulesetManifest['availableGames'][slot]['manifestLocation'])
            rules = json.load(rules)
            break
        else:
            continue

    print(rules['gameInfo']['title']+' Version '+str(rules['gameInfo']['version'])+' Branch '+rules['gameInfo']['branch']+'\nRules by '+rules['gameInfo']['author'])

    # TODO: run game

if __name__ == '__main__':
    main()
