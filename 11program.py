board = [" " for _ in range(9)]
def print_board():
    print()
    print(board[0]+"|"+ board[1]+"|"+ board[2])
    print("-+-+-")
    print(board[3]+"|"+ board[4]+"|"+ board[5])
    print("-+-+-")
    print(board[6]+"|"+ board[7]+"|"+ board[8])
print_board()
    
def check_win(player):
    win_positions=[
        [0,1,2] , [3,4,5] , [6,7,8],
        [0,3,6] , [1,4,7] , [2,5,8],
        [0,4,7] , [2,4,6]
    ]

def play_game():
    current_player="X"
    for turn in range(9):
        print_board()
        move=int(input(f"Player {current_player},choose position(1-9): "))-1
        if board[move]!=" ":
            print("The spot is taken!Try again")
            continue

        board[move]=current_player
        if check_win(current_player):
            print_board()
            print(f"print {current_player} wins!")
            return
        current_player="O" if current_player== "X"else "X"
        print_board()
        print("It's a tie")
play_game()