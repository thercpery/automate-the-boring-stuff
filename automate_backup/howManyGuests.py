name = ""
while not name:
    print("Enter your name.")
    name = input()
    print("How many guests will you have?")
    numOfGuests = int(input())
    if numOfGuests:
        print("Be sure you have enough room for all of your guests.")
print("Done.")