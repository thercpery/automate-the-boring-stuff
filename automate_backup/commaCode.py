import sys
spam = ["apples", "bananas", "tofu", "cats"]
something = []
comma = ""

def gatherEverything(things):
    gatherIntoOne = ""
    for i in range(len(things)):
        if i != len(things) - 1:
            gatherIntoOne += things[i] + ", "
        else:
            gatherIntoOne += "and " + things[i]
    return gatherIntoOne

try:
    while True:
        print("What do you have? Press ENTER or CTRL + C to exit.")
        thing = input()
        if thing != "":
            something += [thing]
        else:
            if len(something) == 0:
                print("You have nothing! Get out!")
                break
            break

    getThings = gatherEverything(something)
    print(f"You have {getThings}.")

except KeyboardInterrupt:
    if len(something) == 0:
        print("You have nothing! Get out!")
    else:
        print(f"You have {gatherEverything(something)}")
    sys.exit()