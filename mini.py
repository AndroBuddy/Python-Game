import time , os

# Define the colors for the board
class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'

# Define row alphabets
rows = {
    "a" : 0 , 
    "b" : 1 ,
    "c" : 2 ,
    "d" : 3 ,
    "e" : 4 ,
    "f" : 5 ,
}

c = 0
start = 0

# Board updater
def player_board(choice , board):
    global c , start
    c = 1
    update = False
    board1 = board 
    start = time.time()
    while update == False:
        (board1 , update) = movement_kill_check(choice , board)
    return board1

# Function for pawn movement and killing
def movement_kill_check(choice , board):
    global c , start 
    update = False
    while(update != True):
        try:
            
            end = time.time()
            if (int(end - start) > 29):
                return None

            row = input("Enter the row Letter : ").lower()
            i = rows[row]
            j = int(input("Enter the column number : "))
            j = j-1
            move = input("Enter 'left' or 'right' to move to the respective places : ").lower()

            if i-1<0:
                print("Choose Your move correctly")



            if (int(end - start) > 29):
                return None

            ## Pawn movement
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF:
                if j == 0 and board[i-1][1] == colors.DEF + '-'  and move == "right":
                    board[i][0] = colors.DEF + '-'
                    board[i-1][1] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                    continue
                elif j == 5 and board[i-1][4]==colors.DEF + '-'  and move == "left":
                    board[i][5] = colors.DEF + '-'
                    board[i-1][4] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                    continue
                elif board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                    ch = 0
                    if move == "right":
                        ch = 1
                    elif move == "left":
                        ch = -1
                    else :
                        print("Choose your move correctly ! \n")
                        continue
                    if board[i-1][j+ch] == colors.DEF + '-':
                        if (j+ch) <0 :
                            print("CHOOSE YOUR MOVE CORRECTLY \n")
                            continue
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+ch] = colors.BLUE+ 'o' + colors.DEF
                        update = True
                        continue
                else:
                    update = False

            elif choice == "red" and board[i][j] == colors.RED+ 'x' + colors.DEF :
                if j == 0 and board[i-1][1] == colors.DEF + '-' and move == "right":
                    board[i][0] = colors.DEF + '-'
                    board[i-1][1] = colors.RED+ 'x' + colors.DEF
                    update = True
                    continue
                elif j == 5 and board[i-1][4]==colors.DEF + '-' and move == "left":
                    board[i][5] = colors.DEF + '-'
                    board[i-1][4] = colors.RED+ 'x' + colors.DEF
                    update = True
                    continue
                elif board[i][j] == colors.RED+ 'x' + colors.DEF :
                    ch = 0
                    if move == "right":
                        ch = 1
                    elif move == "left":
                        ch = -1
                    else :
                        print("Choose your move correctly ! \n")
                        continue
                    if board[i-1][j+ch] == colors.DEF + '-':
                        if (j+ch)< 0 :
                            print("CHOOSE YOUR MOVE CORRECTLY \n")
                            continue
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+ch] = colors.RED+ 'x' + colors.DEF
                        update = True
                        continue
                else:
                    update = False

            # Kill cases
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF:

                    if board[i-1][j-1] == colors.RED+ 'x' + colors.DEF and board[i-2][j-2] == colors.DEF + '-' and move == "left" and j-1 >-1 and j-2 > -1:
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j-1] = colors.DEF + '-'
                        board[i-2][j-2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue
                    elif board[i-1][j+1] == colors.RED+ 'x' + colors.DEF and board[i-2][j+2] == colors.DEF + '-' and move == "right":
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+1] = colors.DEF + '-'
                        board[i-2][j+2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue

            elif choice == "red" and board[i][j] == colors.RED + 'x' + colors.DEF:

                    if board[i-1][j-1] == colors.BLUE+ 'o' + colors.DEF and board[i-2][j-2] == colors.DEF + '-' and move == "left" and j-1 >-1 and j-2 > -1:
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j-1] = colors.DEF + '-'
                        board[i-2][j-2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue

                    elif board[i-1][j+1] == colors.BLUE+ 'o' + colors.DEF and board[i-2][j+2] == colors.DEF + '-' and move == "right":
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+1] = colors.DEF + '-'
                        board[i-2][j+2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue

            else:
                update = False
                print("CHOOSE YOUR MOVE CORECTLY")
                continue

        except Exception as e: 
            print(e)
            update = False
            print("CHOOSE YOUR MOVE CORRECTLY !!!!")
            continue

    return (board , update)

# Function to reset board
def board_reset(choice):
    for i in range(6):
        for j in range(6):
            if choice == "blue":
                board[0][j] = colors.RED + 'x' + colors.DEF
                board[5][j] = colors.BLUE + 'o' + colors.DEF

            if choice == "red":
                board[0][j] = colors.BLUE + 'o' + colors.DEF
                board[5][j] = colors.RED + 'x' + colors.DEF

# Define function to show board
def board_show(board):
    print("The checkerboard currently: \n")

    print(" ", end = "  ")

    # Numbering columns in the top (Computer side)
    for i in range(6):
        print(i + 1, end='  ')

    print()

    # Main board
    for i in range(6):
        print(list(rows.keys())[i] , end = '  ')
        for j in range(6):
            print(board[i][j], end='  ')
        print()

    # Numbering columns in the bottom (User side)
    print(" ", end = "  ")
    for i in range(6):
        print(i + 1, end='  ')

    print()