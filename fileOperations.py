import json
import os
from datetime import datetime


def checkFile():
    try:
        open("officer_data.txt", "r")
        return 1
    except FileNotFoundError:
        return 0


def checkTrackerFile(fileName):
    try:
        open(fileName, "r")
        return 1
    except FileNotFoundError:
        return 0


def initFile():
    officerData = dict()
    if checkFile() == 0:
        print("Running first time setup...")
        officerData["firstName"] = input("First name: ")
        officerData["lastName"] = input("Last name: ")
        officerData["redRank"] = input("RED Rank: ")
        with open("officer_data.txt", "w") as f:
            json.dump(officerData, f)
        os.system("cls")
    else:
        with open("officer_data.txt", "r") as f:
            officerData = json.load(f)
    return officerData


def initTracker(fileName):
    if checkTrackerFile(fileName) == 0:
        with open(fileName, "w") as f:
            f.write("0\n")


def updatePoints(fileName, totalPoints):
    with open(fileName, "r") as f:
        lines = f.readlines()
        lines[0] = f"{totalPoints}\n"

    with open(fileName, "w") as f:
        f.writelines(lines)
