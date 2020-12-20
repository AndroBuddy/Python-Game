import mini_checkers as m
import ai

count = 0
while count <5 :
    m.player_move()
    # m.board_show()
    print("THIS ONE IS DRIVER")
    for i in range(6):
        for j in range(6):
            print(m.board[i][j], end='  ')
        print()
    count = count+1