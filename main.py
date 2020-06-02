from fileOperations import initFile, initTracker
from os import system
from formatHandler import showFormats, showTracker, updateDetails
from datetime import datetime

system("cls")

print("Recruitment and Employment Division helper v0.1")
officerData = initFile()
trackerName = f"tracker/{datetime.now().month}-{datetime.now().year}.txt"
initTracker(trackerName)
totalPoints = []

with open(trackerName, "r") as f:
    totalPoints.append(int(f.readline()))

while True:
    print(f"{officerData['redRank']} {officerData['firstName']} {officerData['lastName']}")
    print("(1) Formats - (2) Point tracker - (3) Update Officer Details - (4) Exit")
    userResponse = input()
    if userResponse == "1":
        showFormats(officerData)
    elif userResponse == "2":
        showTracker(totalPoints, trackerName)
    elif userResponse == "3":
        updateDetails()
        officerData = initFile()
    elif userResponse == "4":
        break

    system("cls")
