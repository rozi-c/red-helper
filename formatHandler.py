from os import system
from time import sleep
import pyperclip
from fileOperations import updatePoints, updateName, updateRank
from datetime import datetime, timedelta


def monthFormat(month):
    if month == 1:
        return "JAN"
    elif month == 2:
        return "FEB"
    elif month == 3:
        return "MAR"
    elif month == 4:
        return "APR"
    elif month == 5:
        return "MAY"
    elif month == 6:
        return "JUN"
    elif month == 7:
        return "JUL"
    elif month == 8:
        return "AUG"
    elif month == 9:
        return "SEP"
    elif month == 10:
        return "OCT"
    elif month == 11:
        return "NOV"
    else:
        return "DEC"


def processFormat(officerData, appFormat, date=False):
    applicantName = input("Applicant name: ")
    gender = input("M/F: ")
    gender = gender.upper()
    if gender == "M":
        appFormat = appFormat.replace("%GND%", "Mr. ")
    else:
        appFormat = appFormat.replace("%GND%", "Ms. ")
    appFormat = appFormat.replace("%ANAME%", applicantName)
    appFormat = appFormat.replace("%FNAME%", officerData["firstName"])
    appFormat = appFormat.replace("%LNAME%", officerData["lastName"])
    appFormat = appFormat.replace("%REDRANK%", officerData["redRank"])
    if date:
        finalDate = datetime.now() + timedelta(days=14)
        appFormat = appFormat.replace("%DATE%", f"{finalDate.day}/{monthFormat(finalDate.month)}/{finalDate.year}")
    pyperclip.copy(appFormat)
    print("Format copied!")
    sleep(1)


def pbaFormats(officerData):
    while True:
        system("cls")
        print("(1) PBA Accepted - (2) PBA Approved - (3) PBA Pending - (4) PBA Denied - (5) PBA Review Approved - (6) "
              "PBA Banned - (0) Back")
        userResponses = input()
        if userResponses == "1":
            with open("formats/pba_accepted.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponses == "2":
            with open("formats/pba_approved.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponses == "3":
            with open("formats/pba_pending.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponses == "4":
            with open("formats/pba_denied.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponses == "5":
            with open("formats/pba_review_approved.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponses == "6":
            with open("formats/pba_banned.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponses == "0":
            break


def diFormats(officerData):
    while True:
        system("cls")
        print("(1) DI Conducted - (2) IPT Conducted - (3) DI+IPT Conducted - (4) DI+IPT Passed - (5) DI+IPT Failed - ("
              "0) Back")
        userResponse = input()
        if userResponse == "1":
            with open("formats/diipt_di_conducted.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "2":
            with open("formats/diipt_ipt_conducted.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "3":
            with open("formats/diipt_both_conducted.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "4":
            with open("formats/diipt_passed.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "5":
            with open("formats/diipt_failed.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "0":
            break


def paeFormats(officerData):
    while True:
        system("cls")
        print("(1) PAE Passed - (2) PAE Failed - (0) Back")
        userResponse = input()
        if userResponse == "1":
            with open("formats/pae_passed.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "2":
            with open("formats/pae_failed.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "0":
            break


def raFormats(officerData):
    while True:
        system("cls")
        print("(1) RideAlong Accepted - (2) RideAlong Denied - (3) RideAlong Expired - (0) Back")
        userResponse = input()
        if userResponse == "1":
            with open("formats/ra_accepted.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat, True)
        elif userResponse == "2":
            with open("formats/ra_denied.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "3":
            with open("formats/ra_expired.txt", "r") as f:
                appFormat = f.read()
            processFormat(officerData, appFormat)
        elif userResponse == "0":
            break


def showFormats(officerData):
    while True:
        system("cls")
        print("(1) PBA - (2) DI/IPT - (3) PAE - (4) RideAlong - (0) Back")
        userResponse = input()
        if userResponse == "1":
            pbaFormats(officerData)
        elif userResponse == "2":
            diFormats(officerData)
        elif userResponse == "3":
            paeFormats(officerData)
        elif userResponse == "4":
            raFormats(officerData)
        elif userResponse == "0":
            break


def pbaPoints(fileName, totalPoints):
    while True:
        system("cls")
        print("Add PBA-related points:")
        print("(1) Accept - (2) Pending - (3) Deny - (4) Ban - (5) Approve - (0) Back")
        userResponse = input()
        link = "NULL"
        if userResponse != "0":
            link = input("Link to application: ")
        if userResponse == "1":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Accepting PBA (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "2":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Placing PBA on Pending (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "3":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Denying PBA (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "4":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Banning Applicant (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "5":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Approving PBA (3 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 3
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "0":
            break


def diPoints(fileName, totalPoints):
    while True:
        system("cls")
        print("Add DI/IPT-related points:")
        print("(1) Conducting DI - (2) Conducting IPT - (3) Approving DI+IPT - (4) Conducting DI(/w Probie) (5) "
              "Conducting IPT (/w Probie) - (0) Back")
        userResponse = input()
        link = "NULL"
        if userResponse != "0":
            link = input("Link to application: ")
        if userResponse == "1":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Conducting DI (3 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 3
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "2":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Conducting IPT (3 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 3
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "3":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Approving DI+IPT (2 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 2
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "4":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Conducting DI with Probationary Officer (4 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 4
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "5":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Conducting IPT with Probationary Officer (4 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 4
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "0":
            break


def paePoints(fileName, totalPoints):
    while True:
        system("cls")
        print("Add PAE-related points:")
        print("(1) Marking PAE - (2) Issuing PAE - (3) Reviewing PAE - (0) Back")
        userResponse = input()
        link = "NULL"
        if userResponse != "0":
            link = input("Link to examination: ")
        if userResponse == "1":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Marking PAE (3 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 3
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
            print("Point added!")
            sleep(1)
        elif userResponse == "2":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Issuing PAE (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "3":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Reviewing PAE (3 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 3
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "0":
            break


def raPoints(fileName, totalPoints):
    while True:
        system("cls")
        print("Add PAE-related points:")
        print("(1) Accepting Ride Along - (2) Denying Ride Along - (3) Expiring Ride Along - (0) Back")
        userResponse = input()
        link = "NULL"
        if userResponse != "0":
            link = input("Link to application: ")
        if userResponse == "1":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Accepting Ride Along application (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "2":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Denying Ride Along application (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "3":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Expiring Ride Along application (1 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 1
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "0":
            break


def indPoints(fileName, totalPoints):
    while True:
        system("cls")
        print("Add Induction-related points:")
        print("(1) Assisting induction - (2) Conducting induction - (3) Conducting private induction- (0) Back")
        userResponse = input()
        if userResponse == "1":
            points = input("Points (2 per 20 min): ")
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Assisting with induction ({points} pt.)\n")
            totalPoints[0] += int(points)
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "2":
            points = input("Points (2 per 15 min): ")
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Conducting induction ({points} pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += int(points)
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "3":
            with open(fileName, "a") as f:
                f.write(f"[*] RED - Conducting private induction (4 pt.) - [url={link}]ACCESS[/url]\n")
            totalPoints[0] += 4
            updatePoints(fileName, totalPoints[0])
            print("Point added!")
            sleep(1)
        elif userResponse == "0":
            break


def addPoint(fileName, totalPoints):
    while True:
        system("cls")
        print("Select point category:s")
        print("(1) PBA - (2) DI/IPT - (3) PAE - (4) RideAlong - (5) Induction - (0) Back")
        userResponse = input()
        if userResponse == "1":
            pbaPoints(fileName, totalPoints)
        elif userResponse == "2":
            diPoints(fileName, totalPoints)
        elif userResponse == "3":
            paePoints(fileName, totalPoints)
        elif userResponse == "4":
            raPoints(fileName, totalPoints)
        elif userResponse == "5":
            indPoints(fileName, totalPoints)
        elif userResponse == "0":
            break


def copyPoints(fileName):
    with open(fileName, "r") as f:
        pyperclip.copy(f.read())
        print("Points copied!")
        sleep(1)


def showTracker(totalPoints, fileName):
    while True:
        system("cls")
        print("Point tracker:")
        print("(1) Add point - (2) Copy points - (0) Back")
        userResponse = input()
        if userResponse == "1":
            addPoint(fileName, totalPoints)
        elif userResponse == "2":
            copyPoints(fileName)
        elif userResponse == "0":
            break


def updateDetails():
    while True:
        system("cls")
        print("Update details:")
        print("(1) Name - (2) Rank - (0) Back")
        userResponses = input()
        if userResponses == "1":
            updateName()
        elif userResponses == "2":
            updateRank()
        elif userResponses == "0":
            break
