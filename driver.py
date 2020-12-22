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


if (os.name == "nt"):
    os.system("cls")
if (os.name =="posix"):
    os.system("clear")
print("BE SURE , YOU CANNOT MOVE BACKWARDS , SO CHOOSE YOUR MOVE WISELY !!!!!!!!!")

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
        print("Choose Red or Blue")


m.board_show(board)


count = 0


while count <5 :
    count = count + 1

    print("YOUR TURN")
    board = m.player_board(choice , board)

    if (os.name == "nt"):
        os.system("cls")
    if (os.name =="posix"):
        os.system("clear")
    print("COMPUTER IS THINKING ... ")
    time.sleep(2)
    board = ai.board_update(choice , board)
    print("COMPUTER IS DONE WITH IT'S TURN")

    m.board_show(board)