import random
from random import randint


def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def create_sudoku_board():
    sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
    return sudoku_board


sudoku_board = create_sudoku_board()


def get_random_num(sudoku_board, row, col):
    candidates = list(range(1, 10))

    i = 0
    while i < (len(sudoku_board[row])):
        if sudoku_board[row][i] in candidates:
            candidates.remove(sudoku_board[row][i])
        i += 1

    column = [sudoku_board[row][col] for row in range(9)]
    candidates = [x for x in candidates if x not in column]

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for _i in range(0, 3):
        for _j in range(0, 3):
            if sudoku_board[start_row + _i][start_col + _j] in candidates:
                candidates.remove(sudoku_board[start_row + _i][start_col + _j])

    if len(candidates) == 0:
        return None
    else:
        return random.choice(candidates)


def sudoku_generate_backtracking(sudoku_board, num_cells_to_fill):
    all_indices = [(row, col) for row in range(9) for col in range(9)]
    all_pairs = random.sample(all_indices, num_cells_to_fill)

    for row, col in all_pairs:
        original_value = sudoku_board[row][col]
        random_int = get_random_num(sudoku_board, row, col)

        while random_int == None:
            sudoku_board[row][col] = original_value
            row, col = all_pairs.pop()
            random_int = get_random_num(sudoku_board, row, col)

        sudoku_board[row][col] = random_int

def set_difficulty(dif):
    cells_to_fill = 0
    if dif == "easy":
        cells_to_fill = randint(32,36)
    elif dif == "normal":
        cells_to_fill = randint(26,31)
    elif dif == "hard":
        cells_to_fill = randint(22,25)
    return cells_to_fill

if __name__ == "__main__":
    
    cells_to_fill = set_difficulty("easy")

    sudoku_generate_backtracking(sudoku_board, cells_to_fill)

    print(print_sudoku(sudoku_board))
