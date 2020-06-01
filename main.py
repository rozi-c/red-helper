from fileOperations import initFile, initTracker
from os import system
from formatHandler import showFormats, showTracker
from datetime import datetime

system("cls")

print("Recruitment and Employment Division helper v0.1")
officerData = initFile()
trackerName = f"tracker/{datetime.now().month}-{datetime.now().year}.txt"
initTracker(trackerName)
totalPoints = []

with open(trackerName, "r") as f:
    totalPoints.append(int(f.readline()))

print(f"{officerData['redRank']} {officerData['firstName']} {officerData['lastName']}")

while True:

    print("(1) Formats - (2) Point tracker - (3) Exit")
    userResponse = input()
    if userResponse == "1":
        showFormats(officerData)
    elif userResponse == "2":
        showTracker(totalPoints, trackerName)
    elif userResponse == "3":
        break

    system("cls")
