from backtrack import backtrack

# function to iterate through the board
def select(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return row, col, range(1, len(board) + 1)

#search driver
def search(board):
    return backtrack(board, select)
