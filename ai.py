import time
import random

class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'





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


    board1 = board
    update = False


    while update == False:
        (board1 , update) = movement_kill_check(choice , board)

    return board1


def movement_kill_check(choice , board):
    
    update = False
    while(update != True):
        i = random.randint(0,5)
        j = random.randint(0,5)

        ## THIS IS FOR KILLING
        try:
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF:

                    if board[i+1][j+1] == colors.RED+ 'x' + colors.DEF and board[i+2][j+2] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+1] = colors.DEF + '-'
                        board[i+2][j+2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue
                    
                    elif board[i+1][j-1] == colors.RED+ 'x' + colors.DEF and board[i+2][j-2] == colors.DEF + '-':
                        if j-1 < 0 or j-2<0:
                            continue
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j-1] = colors.DEF + '-'
                        board[i+2][j-2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue

            if choice == "red" and board[i][j] == colors.RED + 'x' + colors.DEF:
                
                    if board[i+1][j+1] == colors.BLUE+ 'o' + colors.DEF and board[i+2][j+2] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+1] = colors.DEF + '-'
                        board[i+2][j+2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue
                    
                    elif board[i+1][j-1] == colors.BLUE + 'o' + colors.DEF and board[i+2][j-2] == colors.DEF + '-':
                        if j-1 < 0 or j-2 < 0:
                            continue
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j-1] = colors.DEF + '-'
                        board[i+2][j-2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue



    
        
        

            ## THIS IS FOR MOVEMENT
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                if j == 0 and board[i+1][1] == colors.DEF + '-':
                    board[i][0] = colors.DEF + '-'
                    board[i+1][1] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                    # continue
                
                elif j == 5 and board[i+1][4]==colors.DEF + '-':
                    board[i][5] = colors.DEF + '-'
                    board[i+1][4] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                    continue

                elif board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                    ch = random.choice([-1 , 1])
                    if j+ch < 0 :
                        continue
                    if board[i+1][j+ch] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+ch] = colors.BLUE+ 'o' + colors.DEF
                        update = True
                        continue

                else:
                    update = False
                    continue
            
            if choice == "red" and board[i][j] == colors.RED+ 'x' + colors.DEF :
                if j == 0 and board[i+1][1] == colors.DEF + '-':
                    board[i][0] = colors.DEF + '-'
                    board[i+1][1] = colors.RED+ 'x' + colors.DEF
                    update = True
                    continue
                
                elif j == 5 and board[i+1][4]==colors.DEF + '-':
                    board[i][5] = colors.DEF + '-'
                    board[i+1][4] = colors.RED+ 'x' + colors.DEF
                    update = True
                    continue

                elif board[i][j] == colors.RED+ 'x' + colors.DEF :
                    ch = random.choice([-1 , 1])
                    if j+ch < 0 : 
                        continue
                    if board[i+1][j+ch] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+ch] = colors.RED+ 'x' + colors.DEF
                        update = True
                        continue

                else:
                    update = False
                    continue
        except:
            update = False
            continue

    return (board , update)