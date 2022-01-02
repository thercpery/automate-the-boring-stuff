import random, logging, sys
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")

def coinToss(guess):
    logging.debug(f"Start of coinToss({guess})")
    compGuess = ""
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    logging.debug(f"toss = {toss}")
    if toss == 0:
        compGuess = "tails"
    else:
        compGuess = "heads"
    logging.debug(f"compGuess = {compGuess}")
    if guess == compGuess:
        return True
    return False

def continueGame():
    print("Do you want to continue? y/n")
    cont = input()
    if cont == "Y" or cont == "y":
        return True
    elif cont == "N" or cont == "n":
        return False
    else:
        continueGame()

def __init__():
    guess = ""
    while guess not in ("heads", "tails"):
        print("Guess the coin toss! Heads or tails:")
        guess = input()
    if coinToss(guess):
        print("You got it!")
    else:
        print("Sorry man. Incorrect guess.")
    if continueGame():
        __init__()
    else:
        sys.exit()
    

__init__()
