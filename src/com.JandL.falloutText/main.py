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

    ruleset = io.open("rulesets/fallout/v0.1/ruleset.json", "r")
    rules = json.load(ruleset)
    print(rules['gameInfo']['title']+' Version '+str(rules['gameInfo']['version'])+' Branch '+rules['gameInfo']['branch']+'\nRules by '+rules['gameInfo']['author'])

    # TODO: get ruleset object from json

    # TODO: run game

if __name__ == '__main__':
    main()
