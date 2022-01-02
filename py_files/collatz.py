def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

def __init__():
    n = int(input("Enter a number\n"))
    ans = collatz(n)
    print(ans)
    while ans != 1:
        ans = collatz(ans)
        print(ans)

try:
    __init__()
except ValueError:
    print("Please enter an integer!")
    __init__()