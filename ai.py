class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'

import random
def ai_choice(choice):
    if choice == "red":
        return "RED"
    else:
        return "BLUE"


def board_update(choice , board):

    ai_turn = ["left" , "right"]

    if choice == "red":
        choice = "blue"
    else:
        choice = "red"
    # r = random.choice(ai_turn)
    # print (r)

    for i in range(6):
        for j in range(6):
            if choice =="blue":
                if board[i][j] == colors.BLUE+ 'o' + colors.DEF:
                    (flag , board) = kill_check(choice , board)

                # if board[r - 1][pawn - 2] == colors.BLUE + 'o' + colors.DEF and board[r - 2][pawn - 3] == '-':


def kill_check(choice , board):

    update = False
    for i in range(6):
        for j in range(6):
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF:
                try:
                    if board[i+1][j+1] == colors.RED+ 'x' + colors.DEF and board[i+2][j+2] == '-':
                        board[i][j] = "-"
                        board[i+1][j+1] = "-"
                        board[i+2][j+2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                    
                    if board[i+1][j-1] == colors.RED+ 'x' + colors.DEF and board[i+2][j-2] == '-':
                        board[i][j] = "-"
                        board[i+1][j-1] = "-"
                        board[i+2][j-2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                except:
                    continue

            if choice == "red" and board[i][j] == colors.RED+ 'x' + colors.DEF:
                try:
                    if board[i+1][j+1] == colors.BLUE+ 'o' + colors.DEF and board[i+2][j+2] == '-':
                        board[i][j] = "-"
                        board[i+1][j+1] = "-"
                        board[i+2][j+2] = colors.RED + 'x' + colors.DEF
                        update = True
                    
                    if board[i+1][j-1] == colors.BLUE+ 'o' + colors.DEF and board[i+2][j-2] == '-':
                        board[i][j] = "-"
                        board[i+1][j-1] = "-"
                        board[i+2][j-2] = colors.RED + 'x' + colors.DEF
                        update = True
                except:
                    continue
                
    if update == True:
        return board

    else:
        ai_turn = ["left" , "right"]

        def update_func():

            i = random.randint(0,5)
            j = random.randint(0,5)

            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                if j == 0 and board[i+1][1] == "-":
                    board[i][0] = "-"
                    board[i+1][1] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                
                elif j == 5 and board[i+1][4]=="-":
                    board[i][5] = "-"
                    board[i+1][4] = colors.BLUE+ 'o' + colors.DEF
                    update = True

                elif board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                    ch = random.choice([-1 , 1])
                    if board[i+1][j+ch] == "-":
                        board[i][j] = "-"
                        board[i+1][j+ch] = colors.BLUE+ 'o' + colors.DEF
                        update = True

                else:
                    update_func()
            
            if choice == "red" and board[i][j] == colors.RED+ 'x' + colors.DEF :
                if j == 0 and board[i+1][1] == "-":
                    board[i][0] = "-"
                    board[i+1][1] = colors.RED+ 'x' + colors.DEF
                    update = True
                
                elif j == 5 and board[i+1][4]=="-":
                    board[i][5] = "-"
                    board[i+1][4] = colors.RED+ 'x' + colors.DEF
                    update = True

                elif board[i][j] == colors.RED+ 'x' + colors.DEF :
                    ch = random.choice([-1 , 1])
                    if board[i+1][j+ch] == "-":
                        board[i][j] = "-"
                        board[i+1][j+ch] = colors.RED+ 'x' + colors.DEF
                        update = True

                else:
                    update_func()


