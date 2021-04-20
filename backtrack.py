import math

#check to see if the puzzle has been solved
def check_state(board):
    for row in board:
        for num in row:
            if num == 0:
                return False
    return True


#look to see if value is already in the correlating row, column, or block
def check_value(board, row, col, val):
    # Check row
    for num in board[row]:
        if num != 0 and num == val:
            return False

    # Check column
    for rows in board:
        if rows[col] != 0 and rows[col] == val:
            return False

    # Check block
    n = int(math.sqrt(len(board)))
    block1 = int(row/n)
    block2 = int(col / n)
    x_range = range(n)
    for i in [block1 * n + x for x in x_range]:
        for j in [block2 * n + x for x in x_range]:
            if (i, j) != (row, col) and board[i][j] != 0 and board[i][j] == val:
                return False

    return True

#backtracking algorithm
def backtrack(board, select, check=None):
    if check_state(board):
        return board

    row, col, domain = select(board)

    for val in domain:
        if check:
            if type(check) is bool:
                if not check:
                    continue
            else:
                if not check(board, row, col, val):
                    continue
        else:
            if not check_value(board, row, col, val):
                continue

        board[row][col] = val
        result = backtrack(board, select)
        if result:
            return result
        board[row][col] = 0
