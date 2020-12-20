import time
import os 
import ai

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
    global board
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

    return board

# Initial board setup
def board_reset(choice):
    global board
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
    global board
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
# We fetch pawn for the column indexing
def out_of_bounds(pos, pawn, r):  
    global board                                             
    if pos == "left":
        if pawn == 1:
            print("You can't move your pawn outside the board!\nAuto moving right ...")
            pos = "right"
        if choice == "red":                                                                 ########## ADDED TRY BLOCK , THE PAWN VALUE SOMETIMES EXCEED 6 OR BECOMES LESS THAN 0
            try:
                if board[r - 1][pawn - 2] == colors.RED + 'x' + colors.DEF:
                    print("You can't move your pawn here! Moving to the right.")
                    pos = "right"
            except:
                pass
        if choice == "blue":
            try:
                if board[r - 1][pawn - 2] == colors.BLUE + 'o' + colors.DEF:
                    print("You can't move your pawn here! Moving to the right.")
                    pos = "right"
            except:
                pass
        return pos

    if pos == "right":
        if pawn == 6:
            print("You can't move your pawn outside the board!\nAuto moving left ...")
            pos = "left"
        if choice == "red":
            try:
                if board[r - 1][pawn] == colors.RED + 'x' + colors.DEF:
                    print("You can't move your pawn here! Moving to the left.")
                    pos = "left"

            except:
                pass

        if choice == "blue":
            try:
                if board[r - 1][pawn] == colors.BLUE + 'o' + colors.DEF:
                    print("You can't move your pawn here! Moving to the left.")
                    pos = "left"
            except:
                pass

        return pos

# Check whether the move allows player to kill opponent pawn
def kill_check(pos, pawn, r):
    global board
    kill_count = 0
    if pos == "left":
        if choice == "red":
            if r - 2 >= 0 and pawn - 3 >= 0:
                if board[r - 1][pawn - 2] == colors.BLUE + 'o' + colors.DEF and board[r - 2][pawn - 3] == '-':
                    print("You scored a point by eliminating your opponent's pawn!")
                    kill_count += 1
        if choice == "blue":
            if r - 2 >= 0 and pawn - 3 >= 0:
                if board[r - 1][pawn - 2] == colors.RED + 'x' + colors.DEF and board[r - 2][pawn - 3] == '-':
                    print("You scored a point by eliminating your opponent's pawn!")
                    kill_count += 1
        return kill_count

    if pos == "right":
        if choice == "red":
            if r - 2 >= 0 and pawn + 1 <= 5:
                if board[r - 1][pawn] == colors.BLUE + 'o' + colors.DEF and board[r - 2][pawn + 1] == '-':
                    print("You scored a point by eliminating your opponent's pawn!")
                    kill_count += 1
        if choice == "blue":
            if r - 2 >= 0 and pawn + 1 <= 5:
                if board[r - 1][pawn] == colors.RED + 'x' + colors.DEF and board[r - 2][pawn + 1] == '-':
                    print("You scored a point by eliminating your opponent's pawn!")
                    kill_count += 1
        return kill_count

def kill_move(pos, pawn, r):
    global board
    r -= 1
    if choice == "red":
        if pos == "left":
            pawn -= 1
            board[r - 1][pawn - 2] = colors.RED + board[r][pawn - 1] + colors.DEF
            board[r][pawn - 1] = colors.DEF + '-'
        if pos == "right":
            pawn += 1
            board[r - 1][pawn] = colors.RED + board[r][pawn - 1] + colors.DEF
            board[r][pawn - 1] = colors.DEF + '-'

    if choice == "blue":
        if pos == "left":
            pawn -= 1
            board[r - 1][pawn - 2] = colors.BLUE + board[r][pawn - 1] + colors.DEF
            board[r][pawn - 1] = colors.DEF + '-'
        if pos == "right":
            pawn += 1
            board[r - 1][pawn] = colors.BLUE + board[r][pawn - 1] + colors.DEF
            board[r][pawn - 1] = colors.DEF + '-'

# Function to get input from player for checker to move
def player_move():
    global board
    def pawn_prompt():
        global board
        pawn = int(input("Pawn column number: "))

        # Check whether the pawn column selection is more than 6
        if pawn >= 7 :
            print("Invalid Position, please enter again.")
            pawn_prompt() # Recursion

        return pawn
    pawn = pawn_prompt()

    counter = 0 # Counter for pawns in a column
    r = 5 # Default r value to 5 (Start value for player)

    # Check if there are multiple pawns same column
    for i in range(6):                                                        #### i SHOULD bE ZERO I GUESS , LET'S SEE
        # print(counter)
        if choice == "red":
            print (counter)
            if board[i][pawn - 1] == colors.RED + 'x' + colors.DEF:
                counter =counter + 1
                # print(counter)

        if choice == "blue":
            if board[i][pawn - 1] == colors.BLUE + 'o' + colors.DEF:
                counter += 1

    print("PRINTS IT HERE" , counter)
    board_show()

    # If number of pawns in the column is 2 or more, prompt the user to choose which pawn to move by fetching the row index
    if counter > 1:
        def multi_pawn():
            global board
            row = int(input("You have %i checker pieces in this column, pick one to move (Count from bottom): " % counter))
            if board[6 - row][pawn - 1] == '-':
                print("You chose a position with no pawn, try again")
                multi_pawn() # Recursion
            if choice == "red" and board[6 - row][pawn - 1] == colors.BLUE + 'o' + colors.DEF:
                print("You chose a position with no pawn, try again")
                multi_pawn() # Recursion
            if choice == "blue" and board[6 - row][pawn - 1] == colors.RED + 'x' + colors.DEF:
                print("You chose a position with no pawn, try again")
                multi_pawn() # Recursion
            return row
        row = multi_pawn()
        r = 6 - row

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
        if pawn < 6 and pawn > 1:
            if board[r - 1][pawn] == colors.RED + 'x' + colors.DEF and board[r - 1][pawn - 2] == colors.RED + 'x' + colors.DEF:
                print("\nYou can't move this pawn! Try choosing another one.")
                pawn = pawn_prompt()

        if pawn == 6:
            if board[r - 1][pawn - 2] == colors.RED + 'x' + colors.DEF:
                print("\nYou can't move this pawn! Try choosing another one.")
                pawn = pawn_prompt()

        if pawn == 1:
            if board[r - 1][pawn - 1] == colors.RED + 'x' + colors.DEF:
                print("\nYou can't move this pawn! Try choosing another one.")
                pawn = pawn_prompt()

        def red_move():
            global board
            pos = input("Move left or right? ")
            pos = out_of_bounds(pos, pawn, r)
            if pos == "left":
                kcount = kill_check(pos, pawn, r)
                board[r - 1][pawn - 2] = colors.RED + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
                if kcount == 1:
                    kill_move(pos, pawn, r)
            elif pos == "right":
                kcount = kill_check(pos, pawn, r)
                board[r - 1][pawn] = colors.RED + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
                if kcount == 1:
                    kill_move(pos, pawn, r)
            else:
                print("Sorry, invalid position to move.\n")
                red_move() # Recursion
        red_move()

    # Team BLUE
    if choice == "blue":
        if pawn < 6 and pawn > 1:
            if board[r - 1][pawn] == colors.BLUE + 'o' + colors.DEF and board[r - 1][pawn - 2] == colors.BLUE + 'o' + colors.DEF:
                print("\nYou can't move this pawn! Try choosing another one.")
                pawn = pawn_prompt()

        if pawn == 6:
            if board[r - 1][pawn - 2] == colors.BLUE + 'o' + colors.DEF:
                print("\nYou can't move this pawn! Try choosing another one.")
                pawn = pawn_prompt()

        if pawn == 1:
            if board[r - 1][pawn - 1] == colors.BLUE + 'o' + colors.DEF:
                print("\nYou can't move this pawn! Try choosing another one.")
                pawn = pawn_prompt()

        def blue_move():
            global board
            pos = input("Move left or right? ")
            pos = out_of_bounds(pos, pawn, r)
            if pos == "left":
                kcount = kill_check(pos, pawn, r)
                board[r - 1][pawn - 2] = colors.BLUE + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
                if kcount == 1:
                    kill_move(pos, pawn, r)
            elif pos == "right":
                kcount = kill_check(pos, pawn, r)
                board[r - 1][pawn] = colors.BLUE + board[r][pawn - 1] + colors.DEF
                board[r][pawn - 1] = colors.DEF + '-'
                if kcount == 1:
                    kill_move(pos, pawn, r)
            else:
                print("Sorry, invalid position to move.\n")
                blue_move() # Recursion
        blue_move()

print("The game will begin now ...\n")
# player_move()
# board_show()