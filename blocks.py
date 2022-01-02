name = "Mary"
password = "Swordfish"
if name == "Mary":
    print("Hello Mary!")
    if password == "Swordfish":
        print("Access granted")
    else:
        print("Wrong password")

name = "Alicse"
age = 23
if name == "Alice":
    print("Hi Alice!")
elif name != "Alice" or age < 12:
    print("You are not Alice, kiddo.")
else:
    print("Hello stranger!")