#! python3

import pyinputplus as pyip
def getSandwichPrice(bread, protein, cheese, cheeseType, mayo, mustard, lettuce, tomato, sandwiches):
    finalPrice = 0

    # Determine price based on bread type.
    if bread == "wheat":
        finalPrice += 0.2
    elif bread == "white":
        finalPrice += 0.15
    elif bread == "sourdough":
        finalPrice += 0.5
    
    # Determine price based on protein type.
    if protein == "chicken":
        finalPrice += 2.25
    elif protein == "turkey":
        finalPrice += 3.00
    elif protein == "ham":
        finalPrice += 1.25
    elif protein == "tofu":
        finalPrice += 2.00
    
    # Determine price based on cheese type.
    if cheese == "yes":
        if cheeseType == "cheddar":
            finalPrice += 1.00
        elif cheeseType == "Swiss":
            finalPrice += 5.00
        elif cheeseType == "mozzarella":
            finalPrice += 2.50
    else:
        finalPrice += 0

    if mayo == "yes":
        finalPrice += 0.25

    if mustard == "yes":
        finalPrice += 0.50

    if lettuce == "yes":
        finalPrice += 0.25
    
    if tomato == "yes":
        finalPrice += 0.25

    finalPrice *= sandwiches

    return finalPrice
    

print("Welcome to World's Famous Jameis Turnover Bakery!")
bread = pyip.inputMenu(choices = ["wheat","white","sourdough"], prompt = "What bread do you want?\n", numbered = True)
protein = pyip.inputMenu(choices = ["chicken","turkey","ham","tofu"], prompt = "What fillings do you want?\n", numbered = True)
cheese = pyip.inputYesNo("Do you want cheese?\n")
if cheese == "yes":
    cheeseType = pyip.inputMenu(choices = ["cheddar", "Swiss", "mozzarella"], prompt = "What cheese do you want?\n", numbered = True)
else:
    cheeseType = ""
mayo = pyip.inputYesNo("Do you want some mayonnaise?\n")
mustard = pyip.inputYesNo("Do you want some mustard?\n")
lettuce = pyip.inputYesNo("Do you want some lettuce?\n")
tomato = pyip.inputYesNo("Do you want some tomatoes?\n")
sandwiches = pyip.inputInt("How many sandwiches do you want?\n", min = 1)

print(f"You'll pay $ {getSandwichPrice(bread, protein, cheese, cheeseType, mayo, mustard, lettuce, tomato, sandwiches)}.")


