import sys
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " "}

def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
    print("-+-+-")
turn = "X"
moves = 0
try:
    while True:
        printBoard(theBoard)
        print("Turn for " + turn + ". Move on which space? (CTRL + C to quit)")
        move = input()
        if move not in theBoard.keys():
            print("Not a valid move!")
        else:
            theBoard[move] = turn
            moves += 1
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        # TODO: Determine the winner.
        
except KeyboardInterrupt:
    sys.exit()
printBoard(theBoard)