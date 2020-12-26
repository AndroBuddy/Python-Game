import time
import random

class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'


c = 0
start = 0

def ai_choice(choice):
    if choice == "red":
        return "RED"
    else:
        return "BLUE"


def board_update(choice , board):
    global c , start
    c = 1
    ai_turn = ["left" , "right"]

    if choice == "red":
        choice = "blue"
    else:
        choice = "red"


    board1 = board
    update = False

    start = time.time()
    while update == False:
        (board1 , update) = movement_kill_check(choice , board)

    return board1


def movement_kill_check(choice , board):

    global c , start 
    
    update = False

    while(update != True):
        
        end = time.time() 

        if (int(end - start) > 15):
            return None


        pos =[]

        

        for i in range(len(board)):
            for j in range(len(board[i])):
                if choice == "blue":
                    if board[i][j] == colors.BLUE+ 'o' + colors.DEF:
                        pos.append([i,j])
                if choice == "red":
                    if board[i][j] == colors.RED+ 'x' + colors.DEF:
                        pos.append([i,j])


        pawn = random.choice(pos)

        i = pawn[0]
        j = pawn[1]


        try:
             ## THIS IS FOR MOVEMENT
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                if j == 0 and board[i+1][1] == colors.DEF + '-':
                    board[i][0] = colors.DEF + '-'
                    board[i+1][1] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                    continue
                
                elif j == 5 and board[i+1][j-1] == colors.DEF + '-':
                    board[i][j] = colors.DEF + '-'
                    board[i+1][j-1] = colors.BLUE+ 'o' + colors.DEF
                    update = True
                    continue

                elif board[i][j] == colors.BLUE+ 'o' + colors.DEF :
                    ch = random.choice([-1 , 1])
                    if j+ch < 0 :
                        ch = 1
                    try:
                        if board[i+1][j+ch] == colors.DEF + '-':
                            board[i][j] = colors.DEF + '-'
                            board[i+1][j+ch] = colors.BLUE+ 'o' + colors.DEF
                            update = True
                            continue
                    except:
                        pass
                else:
                    update = False
                    
            
            if choice == "red" and board[i][j] == colors.RED+ 'x' + colors.DEF :

                if j == 0 and board[i+1][1] == colors.DEF + '-':
                    board[i][0] = colors.DEF + '-'
                    board[i+1][1] = colors.RED+ 'x' + colors.DEF
                    update = True
                    continue
                
                elif j == 5 and board[i+1][4] == colors.DEF + '-':
                    board[i][5] = colors.DEF + '-'
                    board[i+1][4] = colors.RED+ 'x' + colors.DEF
                    update = True
                    continue

                elif board[i][j] == colors.RED+ 'x' + colors.DEF :
                    ch = random.choice([-1 , 1])
                    if j+ch < 0 : 
                        ch = 1
                    if board[i+1][j+ch] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+ch] = colors.RED+ 'x' + colors.DEF
                        update = True
                        continue

                else:
                    # print("else")
                    update = False
                    # continue

            ## THIS IS FOR KILLING

            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF:

                    if board[i+1][j-1] == colors.RED+ 'x' + colors.DEF and board[i+2][j-2] == colors.DEF + '-':
                        if j-1 < 0 or j-2<0:
                            continue
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j-1] = colors.DEF + '-'
                        board[i+2][j-2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue

                    elif board[i+1][j+1] == colors.RED+ 'x' + colors.DEF and board[i+2][j+2] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+1] = colors.DEF + '-'
                        board[i+2][j+2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue
                    


            if choice == "red" and board[i][j] == colors.RED + 'x' + colors.DEF:
                    if board[i+1][j-1] == colors.BLUE + 'o' + colors.DEF and board[i+2][j-2] == colors.DEF + '-':
                        if j-1 < 0 or j-2 < 0:
                            continue
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j-1] = colors.DEF + '-'
                        board[i+2][j-2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue   
                    elif board[i+1][j+1] == colors.BLUE+ 'o' + colors.DEF and board[i+2][j+2] == colors.DEF + '-':
                        board[i][j] = colors.DEF + '-'
                        board[i+1][j+1] = colors.DEF + '-'
                        board[i+2][j+2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue
                    
        except Exception as e:
            print(e)
            update = False
            continue

    return (board , update)