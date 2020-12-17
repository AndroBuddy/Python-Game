print("Welcome to Python Mini Checkers!\n")

# Define colors
class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'

# Checker sets for both colors (We keep removing checkers from these as game goes on)
red_set = ['o', 'o', 'o', 'o', 'o', 'o']
blue_set = ['o', 'o', 'o', 'o', 'o', 'o']

# Define function to show the checkerboard
def board_show(choice):
    board = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]

    print("The checkerboard currently: \n")
    for i in range(6):
        for j in range(6):
            if choice == "blue":
                board[0][j] = colors.RED + red_set[j] + colors.DEF
                board[5][j] = colors.BLUE + blue_set[j] + colors.DEF

            if choice == "red":
                board[0][j] = colors.BLUE + blue_set[j] + colors.DEF
                board[5][j] = colors.RED + red_set[j] + colors.DEF

            print(board[i][j], end='  ')
        print()

# Get the color input from the user
choice = input("Select your color side (" + colors.RED + "Red" + " " + colors.BLUE + "Blue" + colors.DEF + ") --> ").lower()

# Validate input and assign starting priority
def check(choice):
    if choice == "red":
        print("Your turn first\n")
        board_show(choice)
    elif choice == "blue":
        print("You go second, computer's turn\n")
        board_show(choice)
    else:
        choice = input("Invalid color selection, please enter correct choice: ").lower()
        check(choice)

# Call the validator
check(choice)