import os

clear = lambda: os.system('cls')

listOfStrings = []


def filterStrings():
    clear()
    ctr = 0
    while (ctr < len(listOfStrings)):
        showStrings(listOfStrings[ctr].split('"'))
        ctr += 1


def showStrings(listOfFilteredStrings):
    ctr = 0
    while (ctr < len(listOfFilteredStrings)):
        if ctr == 1 or ctr % 2 == 1:
            print(listOfFilteredStrings[ctr])
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
