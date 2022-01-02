#! python3
# dateDetection.py - detect dates in a string

import re, sys

dateRegex = re.compile(r"""(
    (\d{2})             # mm
    (/|-)?              # separator (/ or -)
    (\d{2})             # dd
    (/|-?)              # separator (/ or -)
    (\d{4})             # yyyy
)""", re.VERBOSE)

def dateValid(date):
    if len(date) != 0:
        mm = int(date[1])
        dd = int(date[3])
        yyyy = int(date[5])
        if mm != 0:
            if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
                if dd <= 31 and dd != 0:
                    print("You have a proper date.")
                else:
                    print("Wrong date.")
            elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
                if dd <= 30 and dd != 0:
                    print("You have a proper date.")
                else:
                    print("Wrong date.")
            elif mm == 2:
                if dd <= 28 and dd != 0:
                    print("You have a proper date.")
                elif dd == 29:
                    leapYearDivisibleBy400 = yyyy % 400
                    if leapYearDivisibleBy400 == 0:
                        print("You have a proper date.")
                    else:
                        leapYearDivisibleBy4 = yyyy % 4
                        leapYearDivisibleBy100 = yyyy % 100
                        if leapYearDivisibleBy4 == 0 and not leapYearDivisibleBy100 == 0:
                            print("You have a proper date.")
                        else:
                            print("Wrong date.")
                else:
                    print("Wrong date.")
        else:
            print("Wrong date.")
    else:
        print("Wrong date.")

def continueProgram():
    print("Do you want to continue? y/n")
    cont = input()
    if cont == "Y" or cont == "y":
        __init__()
    elif cont == "N" or cont == "n":
        print("Exiting program.")
        sys.exit()
    else:
        continueProgram()

def __init__():
    print("Please enter a date (or press CTRL + C to quit.)")
    sampleDate = input()
    if sampleDate == "":
        print("You have not entered anything.")
        continueProgram()
    dateDetect = list(dateRegex.findall(sampleDate))
    if len(dateDetect) == 0:
        print("Wrong input or date.")
    for i in range(len(dateDetect)):
        dateValid(dateDetect[i])
    continueProgram() 

try:
    __init__()
except KeyboardInterrupt:
    print("Exiting program.")
    sys.exit()
