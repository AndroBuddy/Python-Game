import time , os

class colors:
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    DEF = '\033[0m'


rows = {
    "a" : 0 , 
    "b" : 1 ,
    "c" : 2 ,
    "d" : 3 ,
    "e" : 4 ,
    "f" : 5 ,
}



def player_board(choice , board):

    update = False

    board1 = board 

    while update == False:
        (board1 , update) = movement_kill_check(choice , board)

    return board1


def movement_kill_check(choice , board):

    update = False

    while(update != True):

        try:

            row = input("Enter the row Letter : ").lower()
            i = rows[row]
            j = int(input("Enter the column number : "))
            j = j-1

            move = input("Enter 'left' or 'right' to move to the respective places : ").lower()



            ## THIS IS FOR MOVEMENT
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
                        print("Choose your move correctly ! ")
                        continue 
                    
                    if board[i-1][j+ch] == colors.DEF + '-':
                        if (j+ch) <0 :
                            print("CHOOSE YOUR MOVE CORRECTLY")
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
                        print("Choose your move correctly ! ")
                        continue

                    if board[i-1][j+ch] == colors.DEF + '-':
                        if (j+ch)< 0 :
                            print("CHOOSE YOUR MOVE CORRECTLY")
                            continue

                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+ch] = colors.RED+ 'x' + colors.DEF
                        update = True
                        continue

                else:
                    update = False

                    
            ## FOR KILLING ##
            if choice == "blue" and board[i][j] == colors.BLUE+ 'o' + colors.DEF:

                    ### FOR KILLING ###

                    if board[i-1][j+1] == colors.RED+ 'x' + colors.DEF and board[i-2][j+2] == colors.DEF + '-' and move == "right":
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+1] = colors.DEF + '-'
                        board[i-2][j+2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue

                    elif board[i-1][j-1] == colors.RED+ 'x' + colors.DEF and board[i-2][j-2] == colors.DEF + '-' and move == "left" and j-1 >-1 and j-2 > -1:
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j-1] = colors.DEF + '-'
                        board[i-2][j-2] = colors.BLUE + 'o' + colors.DEF
                        update = True
                        continue
            
            elif choice == "red" and board[i][j] == colors.RED + 'x' + colors.DEF:
                

                    ### FOR KILLING ###

                    if board[i-1][j+1] == colors.BLUE+ 'o' + colors.DEF and board[i-2][j+2] == colors.DEF + '-' and move == "right":
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j+1] = colors.DEF + '-'
                        board[i-2][j+2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue

                    elif board[i-1][j-1] == colors.BLUE+ 'o' + colors.DEF and board[i-2][j-2] == colors.DEF + '-' and move == "left" and j-1 >-1 and j-2 > -1:
                        board[i][j] = colors.DEF + '-'
                        board[i-1][j-1] = colors.DEF + '-'
                        board[i-2][j-2] = colors.RED + 'x' + colors.DEF
                        update = True
                        continue

            else:
                update = False
                print("CHOOSE YOUR MOVE CORECTLY")
                continue
        
        except : 
            update = False
            print("CHOOSE YOUR MOVE CORRECTLY !!!!")
            continue

    return (board , update)





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



############# BELOW IS THE CODE FOR TESTING #############

# board= [[colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
#         [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
#         [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
#         [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
#         [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-'],
#         [colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-', colors.DEF + '-']]





# choice = "blue"
# board_reset(choice)
# board_show(board)

# board1 = board
# for i in range(2):

#     board1 = player_board(choice , board1)
#     time.sleep(2)
#     board_show(board1)
