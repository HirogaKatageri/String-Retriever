import os
import re

clear = lambda: os.system('cls')

listOfStrings = []


def filterStrings():
    clear()
    ctr = 0
    while (ctr < len(listOfStrings)):
        showStrings(re.findall('\".*?\"', listOfStrings[ctr]))
        showStrings(re.findall("\'.*?\'", listOfStrings[ctr]))
        ctr += 1


def showStrings(listOfFilteredStrings):
    ctr = 0
    while (ctr < len(listOfFilteredStrings)):
        print(listOfFilteredStrings[ctr].replace('"', "").replace("'", ""))
        ctr += 1


def startInput():
    listOfStrings.clear()
    print("Input Strings; Type [done] when finished.")
    notDone = True

    while (notDone):
        stringInput = input()
        stringInput.replace(' ', '_')

        if stringInput.lower() == "done":
            notDone = False
            filterStrings()
        else:
            listOfStrings.append(stringInput)


startInput()
