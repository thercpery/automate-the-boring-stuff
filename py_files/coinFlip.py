import random
streaks = 0
headsOrTailsList = []
value = ""

def getStreakOf6(getList):
    streak = 0
    streakCounter = 0
    for i in range(len(getList)):
        prevValue = getList[i]
        # While i is not 100
        try:
            nextValue = getList[i+1]
            if prevValue == nextValue:
                streakCounter += 1
            else:
                streakCounter = 0
            if streakCounter == 6:
                streak += 1
                streakCounter = 0
        except IndexError:
            break
    return streak

for experimentNumber in range(10000):
    flip = random.randint(0, 1)
    if flip == 0:
        value = "H"
    else:
        value = "T"
    headsOrTailsList += [value]
    # If experimentNumber reaches 100 then get streaks of 6 from that list
    if experimentNumber % 100 == 0:
        streaks += getStreakOf6(headsOrTailsList)
        # Empty array
        headsOrTailsList = []


print('Chance of streak: %s%%' % (streaks / 100))