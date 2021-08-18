from sys import platform
import random
import os

score = 0


def line_shift(line):
    global score
    new_row = []
    for num_line in line:
        if num_line != 0:
            if len(new_row) > 0:
                if new_row[-1][1] == 0:
                    if new_row[-1][0] == num_line:
                        new_row[-1] = [num_line * 2, 1]
                        score += num_line * 2
                    else:
                        new_row.append([num_line, 0])
                else:
                    new_row.append([num_line, 0])

            else:
                new_row.append([num_line, 0])

    # convert in stack
    stack_row = []
    for nun in new_row:
        if nun[0] != 0:
            stack_row.append(nun[0])
    size = 4 - len(stack_row)
    for num_line in range(size):
        stack_row.append(0)
    return stack_row


def gen_num():
    num = (random.choices([4, 2], weights=[10, 90]))[0]
    return num


def place_num_on_the_board():
    place_list = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                place_list.append((i, j))
    if len(place_list) == 0:
        print('GAME OVER!!!')
        exit(0)
    place = random.choice(place_list)
    board[place[0]][place[1]] = gen_num()


def gen_start_board(size_row=4, size_col=4):
    board2048 = [[i * 0] * size_row for i in range(size_col)]
    while True:
        gen_coordinate_num1 = [random.randint(0, 3), random.randint(0, 3)]
        gen_coordinate_num2 = [random.randint(0, 3), random.randint(0, 3)]
        if gen_coordinate_num1 != gen_coordinate_num2:
            break
    board2048[gen_coordinate_num1[0]][gen_coordinate_num1[1]] = gen_num()
    board2048[gen_coordinate_num2[0]][gen_coordinate_num2[1]] = gen_num()
    return board2048


def x_move(move_side):
    for index, row in enumerate(board):
        if move_side == 'left':
            board[index] = line_shift(row)
        if move_side == 'right':
            board[index] = line_shift(row[::-1])[::-1]


def y_move(move_side):
    for col_board in range(4):
        line = []
        for row_board in range(4):
            line.append(board[row_board][col_board])
        if move_side == 'down':
            line = line_shift(line[::-1])[::-1]
        if move_side == 'up':
            line = line_shift(line)
        for row_board in range(4):
            board[row_board][col_board] = line[row_board]


def print_game_screen():
    # clear console
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

    print(f'{"*" * 5} x - exit, r - restart {"*" * 5}')
    print('move: left, right, up, down')
    print(f'Score: {score}')
    for i in board:
        print(i)


board = gen_start_board()
while True:
    print_game_screen()
    step = input('Enter move: ').lower()
    tmp_board = [row[:] for row in board]
    if step in ('right', 'left'):
        x_move(step)
    elif step in ('down', 'up'):
        y_move(step)
    elif step == 'r':  # restart
        board = gen_start_board()
        score = 0
        continue
    elif step == 'x':
        print('You pressed x - exit the game')
        exit(0)
    else:
        continue
    if tmp_board == board:  # The move did not change the board
        continue
    place_num_on_the_board()