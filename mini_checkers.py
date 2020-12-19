import time

# Welcome message :)
print("Welcome to Python Mini Checkers!\n")

# Define colors
class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'

# Prepare the board
board = [['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-']]

# Get the color input from the user
choice = input("Select your color side (" + colors.RED + "Red" + " " + colors.BLUE + "Blue" + colors.DEF + ") --> ").lower()

# Define function to show the checkerboard
def board_show():
    print("The checkerboard currently: \n")

    # Numbering columns in the top (Computer side)
    for i in range(6):
        print(i + 1, end='  ')

    print()

    # Main board
    for i in range(6):
        for j in range(6):
            print(board[i][j], end='  ')
        print()

    # Numbering columns in the bottom (User side)
    for i in range(6):
        print(i + 1, end='  ')

    print()

# Initial board setup
def board_reset(choice):
    for i in range(6):
        for j in range(6):
            if choice == "blue":
                board[0][j] = colors.RED + 'x' + colors.DEF
                board[5][j] = colors.BLUE + 'o' + colors.DEF

            if choice == "red":
                board[0][j] = colors.BLUE + 'o' + colors.DEF
                board[5][j] = colors.RED + 'x' + colors.DEF

# Validate input and assign starting priority
def check(choice):
    if choice == "red":
        print("\nYou chose red, " + colors.RED + "x" + colors.DEF)

    elif choice == "blue":
        print("\nYou chose blue, " + colors.BLUE + "o" + colors.DEF)

    else:
        choice = input("Invalid color selection, please enter correct choice: ").lower()
        check(choice) # Recursion
    return choice

choice = check(choice)
board_reset(choice)
board_show()

# Out of bounds validator to check if checker moves out from board
# We fetch c for the column indexing
def out_of_bounds(pos, c):
    if pos == "left":
        if c == 0:
            print("You can't move your pawn outside the board!\nAuto moving right ...")
            pos = "right"
        return pos

    if pos == "right":
        if c == 5:
            print("You can't move your pawn outside the board!\nAuto moving left ...")
            pos = "left"
        return pos

# Function to get input from player for checker to move
def player_move():
    pawn = int(input("Pawn column number: "))

    # Check whether the pawn column selection is more than 6
    if pawn >= 7 :
        print("Invalid Position, please enter again.")
        player_move() # Recursion

    counter = 1 # Counter for pawns in a column
    r = 5 # Default r value to 5 (Start value for player)

    # Check if there are multiple pawns same column
    for i in range(6):
        if choice == "red":
            if board[i - 1][pawn - 1] == 'x':
                counter += 1
        if choice == "blue":
            if board[i - 1][pawn - 1] == 'o':
                counter += 1

    # If count of pawns in the column is 2 or more prompt the user to choose which pawn to move by fetching the row index
    if counter > 1:
        r = input("You have more than one checker piece in this column, pick one to move: ")
    
    # If counter is 1 fetch the r value
    if counter == 1:
        for i in range(6):
            if choice == "red":
                if board[i - 1][pawn - 1] == 'x':
                    r = i
            if choice == "blue":
                if board[i - 1][pawn - 1] == 'o':
                    r = i

    # After passing previous validation, proceed with movement side selection - left or right
    # Team RED
    if choice == "red":
        def red_move():
            pos = input("Move left or right? ")
            pos = out_of_bounds(pos, pawn - 1)
            if pos == "left":
                board[r - 1][pawn - 2] = colors.RED + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
            elif pos == "right":
                board[r - 1][pawn] = colors.RED + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
            else:
                print("Sorry, invalid position to move")
                red_move() # Recursion
        red_move()

    # Team BLUE
    if choice == "blue":
        def blue_move():
            pos = input("Move left or right? ")
            pos = out_of_bounds(pos, pawn - 1)
            if pos == "left":
                board[r - 1][pawn - 2] = colors.BLUE + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
            elif pos == "right":
                board[r - 1][pawn] = colors.BLUE + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
            else:
                print("Sorry, invalid position to move.")
                blue_move() # Recursion
        blue_move()

print("The game will begin now ...\n")
player_move()
board_show()