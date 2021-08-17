from subprocess import call
from time import sleep

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]
game_is_running = True
current_player = 'X'
winner = ''
tictactoe_ascii = '''===============================================================
---------------------------TicTacToe---------------------------
===============================================================
'''


def play_game():
    init_reset()
    print(tictactoe_ascii)
    while game_is_running:
        display_board()
        fill_board(get_input(), current_player)
        check_winner()
        celebrate()  # conditional
        change_player()
        _ = call('cls', shell=True)
        print(tictactoe_ascii)


def display_board():
    print("         |         |                       |         |         ")
    print(f"    {board[0]}    |    {board[1]}    |    {board[2]}             1    |    2    |    3")
    print("_________|_________|_________      ________|_________|_________")
    print("         |         |                       |         |         ")
    print(f"    {board[3]}    |    {board[4]}    |    {board[5]}             4    |    5    |    6")
    print("_________|_________|_________      ________|_________|_________")
    print("         |         |                       |         |         ")
    print(f"    {board[6]}    |    {board[7]}    |    {board[8]}             7    |    8    |    9")
    print("         |         |                       |         |         ")


def get_input():
    print(f'Its {current_player}s turn!'.center(63))
    while True:
        print('Choose a position between 1-9:'.center(63), end='\b' * 15)
        chosen_cell = input()
        if validate_input(chosen_cell):
            chosen_cell = int(chosen_cell) - 1  # fixing the number because of indexing
            return chosen_cell


def validate_input(chosen_cell):
    try:
        chosen_cell = int(chosen_cell)
        if chosen_cell in range(1, 10):
            if board[chosen_cell - 1] == 'X' or board[chosen_cell - 1] == 'O':
                return False
            else:
                return True
        else:
            return False
    except ValueError:
        return False


def fill_board(cell, value):
    board[cell] = value


def change_player():
    global current_player
    if game_is_running:
        if current_player == 'X':
            current_player = 'O'
        elif current_player == 'O':
            current_player = 'X'


def check_winner():
    global winner, game_is_running
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if row1 or row2 or row3 or col1 or col2 or col3 or diagonal1 or diagonal2:
        game_is_running = False
        winner = current_player
    elif '-' not in board:
        game_is_running = False
        winner = 'Tie'


def celebrate():
    if not game_is_running and winner != '':
        _ = call('cls', shell=True)
        display_board()
        if winner == 'X' or winner == 'O':
            print('\n', f'{current_player} won the game...!'.center(63))
            input()
        elif winner == 'Tie':
            print('\n', 'No one won! Its a Tie!'.center(63))
            input()


def init_reset():
    global winner, game_is_running, board
    _ = call('cls', shell=True)
    winner = ''
    game_is_running = True
    board = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-'
    ]


while True:
    play_game()
    while True:
        print('Play again?(Y/n)'.center(63), end='\b' * 22)
        reset = input().lower()
        if reset in ('', 'y', 'yes', 'hell yeah'):
            for i in range(4)[::-1]:
                print(f'Game starts in...{i}'.center(63), end='\r')
                sleep(1)
            break
        elif reset in ['n', 'no', 'hell no', 'exit', 'quit']:
            print('\n\n', 'OK! we had FUN!'.center(63))
            for i in range(5)[::-1]:
                print(f'{i}'.center(63), end='\r')
                sleep(1)
            break
    if reset in ['n', 'no', 'hell no', 'exit', 'quit']:
        break