import sys

birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}
try:
    while True:
        print("Enter a name: (blank or CTRL + C to quit)")
        name = input()
        if name == "":
            break

        if name in birthdays:
            print(birthdays[name] + " is the birthday of " + name)
        else:
            print("I do not have a birthday information for " + name)
            print("What is their birthday?")
            bday = input()
            birthdays[name] = bday
            print("Birthday database updated.")

except KeyboardInterrupt:
    sys.exit()