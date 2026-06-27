
X = 'X'
O = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

available_slots = { 
    '1': [0, 0], '2': [0, 1], '3': [0, 2], 
    '4': [1, 0], '5': [1, 1], '6': [1, 2], 
    '7': [2, 0], '8': [2, 1], '9': [2, 2] 
}

def print_board():
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        print(line)

def play_move(player):
    print(f'Player {player}\'s turn, enter your slot (1-9):')

    while True:
        slot = input()
        
        if slot not in available_slots:
            print('Invalid slot. Try again.')
            continue

        row, column = available_slots[slot]
        if board[row][column] == ' ':
            board[row][column] = player
            break
        else:
            print('Slot is already taken. Try again.')
            continue


def check_win(board):
    #row check
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    #column check
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True

    #diagonal check
    for diagonal in [[0, 0], [1, 1], [2, 2]]:
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True

    for diagonal in [[0, 2], [1, 1], [2, 0]]:
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
    
    return False

def check_draw(board):
    for row in board:
        for slot in row:
            if slot == ' ':
                return False
    return True

def main():
    print('Welcome to Tic Tac Toe!')
    print_board()
    
    current_player = X
    
    while True:
        
        play_move(current_player)
        
        print_board()

        if check_win(board):
            print(f'{current_player} wins!')
            break

        if check_draw(board):
            print('Draw!')
            break

        if current_player == X:
            current_player = O
        else:
            current_player = X
        
if __name__ == '__main__':
    main()