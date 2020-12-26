# import mini_checkers as m1
import mini as m
import ai
import os , time

class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'

board= [[colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
        [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
        [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
        [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
        [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
        [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-']]

# empty = board.copy()

if (os.name == "nt"):
    os.system("cls")
if (os.name =="posix"):
    os.system("clear")


print("===========================\n")
print("WELCOME TO MINI CHECKERS \n")
print("===========================\n")
print("BEFORE STARTING REMEMBER FEW RULES \n")
print("YOU CAN MOVE DIAGONALLY \n")
print("YOU CAN KILL DIAGONALLY BY JUMPING OVER THE ENEMY \n")
print("DON'T EXPECT TO GET A BONUS AFTER YOU KILL AN ENEMY \n")
print("BE SURE , YOU CANNOT MOVE BACKWARDS , SO CHOOSE YOUR MOVE WISELY !!!!!!!!!\n ")
print("ONCE YOU START THE GAME , YOU CAN'T EXIT , PLAY AT YOUR OWN RISK XD")
print("THERE IS NO DRAW IN THIS GAME !!!!")
print("GAME ENDS WHEN 3 PAWNS REACHES THE OTHER SIDE \n")
print("GAME ENDS IF YOU ONLY HAVE 2 PAWNS LEFT \n")
print("YOU HAVE A 30 SECONDS TIME LIMIT. IF YOU HAVE NO PLACE TO MOVE , YOU WILL AUTOMATICALLY LOSE")
print("BONUS: COMPUTER IS NOT SO INTELLIGENT , IT WILL GET OUTWITTED IF YOU PLAY TOO WELL \n")
print("BONUS: FIND LOOPHOLES TO DEFEAT THE COMPUTER...\n")
print("ENJOY \n")


choice = ""


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

while True:
    choice = input("Select your color side (" + colors.RED + "Red" + " " + colors.BLUE + "Blue" + colors.DEF + ") --> ").lower()
    if choice == "red" or choice == "blue":
        board_reset(choice)
        break
    else:
        print("Choose Red or Blue\n")

m.board_show(board)

# rpoint = 0
# bpoint = 0


def clear():
    if (os.name == "nt"):
        os.system("cls")
    if (os.name =="posix"):
        os.system("clear")


while True:


    player_pawn = 0
    comp_pawn = 0
    for i in range (6):
        for j in range(6):
            if choice == "blue":
                if board[i][j] == colors.BLUE + "o" + colors.DEF:
                    player_pawn = player_pawn + 1
                if board[i][j] == colors.RED + "x" + colors.DEF:
                    comp_pawn = comp_pawn + 1
            if choice == "blue":
                if board[i][j] == colors.RED + "x" + colors.DEF:
                    player_pawn = player_pawn + 1
                if board[i][j] == colors.BLUE + "o" + colors.DEF:
                    comp_pawn = comp_pawn + 1


    if player_pawn == 2 :
        print("YOU LOSE , COMPUTER WINS !!")
        break
    elif comp_pawn == 2 :
        print("YOU WIN , CONGRATS !!")
        break

    print("YOUR TURN\n \n ")
    try:
        board = m.player_board(choice , board)
    except:
        print("YOU LOSE !!!!!!!!!! \nYOU HAVE EXCEEDED 30 SECONDS , MAYBE YOU NEVER HAD A CHANCE")
        break


    clear()

    m.board_show(board)
    print("\n")



    
    print("COMPUTER IS THINKING ...\n \n ")
    time.sleep(2)
    

    try:
        board = ai.board_update(choice , board)
    except Exception as e:
        print("YOU WIN !!! YOU HAVE OUTWITTED COMPUTER")
        break

    clear()
    print("COMPUTER IS DONE WITH IT'S TURN \n \n")
    m.board_show(board)
    print("\n")

    player = 0
    comp = 0

    for j in range(6):
        if choice == "blue":
            if board[0][j] == colors.BLUE + "o" + colors.DEF:
                player = player+1
            if board[5][j] == colors.RED + "x" + colors.DEF:
                comp = comp+1
        if choice == "red":
            if board[0][j] == colors.RED + "x" + colors.DEF:
                player = player+1
            if board[5][j] == colors.BLUE + "o" + colors.DEF:
                comp = comp+1


    if player == 3:
        clear()
        m.board_show(board)
        print("YOU WIN , CONGRATS !! \n")
        break
    if comp == 3:
        clear()
        m.board_show(board)
        print("YOU LOSE , COMPUTER WINS \n")
        break