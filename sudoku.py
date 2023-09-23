import random
from random import randint


def is_row_valid(row):
    unique_numbers = set()

    for num in row:
        if num != 0:

            if num in unique_numbers:
                return False
            unique_numbers.add(num)


    return len(unique_numbers) == 9 - row.count(0)


def are_columns_valid(board):
    not_unique_columns = []
    for col in range(0,8):
        column = [board[row][col] for row in range(9)]
        unique_numbers = set()
        
        for num in column:
                if num != 0:
                    if num in unique_numbers:
                        not_unique_columns.append(col)
                    unique_numbers.add(num)

    if not not_unique_columns:
        return True
    else: 
        return not_unique_columns

def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


game_mode = "easy"

if game_mode == "easy":
    min, max = 3, 7
elif game_mode == "normal":
    min, max = 3, 6
else:
    min, max = 2, 5

sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

for row in sudoku_board:
    ints_in_row = randint(min, max)
    available_numbers = list(range(1, 10))
    random.shuffle(available_numbers)

    for i in range(ints_in_row):
        cell_index = randint(0, 8)
        if row[cell_index] == 0:
            row[cell_index] = available_numbers.pop()

for row in sudoku_board:
    print(is_row_valid(row))

def fix_columns(board):
    columns_to_fix = are_columns_valid(sudoku_board)
    for col in columns_to_fix:
        column = [board[row][col] for row in range(9)]
        print(column)

fix_columns(sudoku_board)
print_sudoku(sudoku_board)
