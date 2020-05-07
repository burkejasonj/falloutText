import json
import io
import os


def main():
    # TODO: init variables

    # TODO: init screen

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # TODO: ask for ruleset name and version

    rulesetManifest = io.open("rulesets/manifest.json", 'r')
    rulesetManifest = json.load(rulesetManifest)
    print("Please select one of the following:")
    for slot in rulesetManifest['availableGames']:
        print(rulesetManifest['availableGames'][slot]['callName'])
    slotID = input("? ")
    for slot in rulesetManifest['availableGames']:
        if slotID == rulesetManifest['availableGames'][slot]['callName']:
            print(rulesetManifest['availableGames'][slot]['manifestLocation'])
            rules = io.open(rulesetManifest['availableGames'][slot]['manifestLocation'])
            rules = json.load(rules)
            break
        else:
            continue

    print(rules['gameInfo']['title']+' Version '+str(rules['gameInfo']['version'])+' Branch '+rules['gameInfo']['branch']+'\nRules by '+rules['gameInfo']['author'])

    # TODO: get ruleset object from json

    # TODO: run game

if __name__ == '__main__':
    main()
