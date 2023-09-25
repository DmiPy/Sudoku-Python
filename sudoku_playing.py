from sudoku_board import sudoku_generate_backtracking, create_sudoku_board, print_sudoku, set_difficulty


def are_elements_unique(input_list):
    unique_numbers = set()
    for element in input_list:
        if element != 0:
            if element in unique_numbers:
                return False
            unique_numbers.add(element)
    return True


def is_column_valid(board, col):
    column = [board[row][col] for row in range(9)]
    return are_elements_unique(column)


def is_row_valid(board, row):
    row_list = board[row]
    return are_elements_unique(row_list)


def is_square_valid(board, row, col):
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    unique_numbers = set()
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] != 0:
                if board[i][j] in unique_numbers:
                    return False
                unique_numbers.add(board[i][j])
    return True


if __name__ == "__main__":
    cells_to_fill = set_difficulty("easy")

    sudoku_board = create_sudoku_board()
    sudoku_generate_backtracking(sudoku_board, cells_to_fill)

    print(is_column_valid(sudoku_board, 0))
    print(is_row_valid(sudoku_board, 0))
    print(is_square_valid(sudoku_board, 3, 4))
    print_sudoku(sudoku_board)

