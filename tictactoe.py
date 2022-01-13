'''
Game: Tic-Tac-Toe
Author: Carina Aguero
CSE210: Programming with classes
'''

def main():
    board = new_board
    while not (has_winner(board) or tie(board)):
        new_board(board)
        turn (player_1, board)
        player_1= player_2(player_1)
    new_board(board)
    print ('Good game. Thanks for playing!')

def create_board(board):
    for file in board:
        for i in range(len(file)):
            if i == len(file) - 1:
                print(file[i], end='\n')
            else:
                print(file[i], end='  ')

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def tie(board):
    for square in range(9):
        if board[square] != 'x' and board[square] != 'o':
            return False
    return True 

def move(player_1, player_2):
    while turn < 9:
        if player_1 == '':
            print('Name of player_1 (x)')
            player_1 = input()
            print('Name of player_2 (o)')
            player_2 = input()
        else:
            if turn_1:
                print(player_1 + ', choose a square')
            else:
                print(player_2 + ', choose a square')

turn_1 = True
player_1= ''
player_2= ''
turn = 0

def new_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

if __name__ == "__main__":
    main()