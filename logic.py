# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

#Business Logic
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board, player):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    
    # Check rows, columns, and diagonals
    winning = any(
        (board[i][0] == board[i][1] == board[i][2] == player) or  # rows
        (board[0][i] == board[1][i] == board[2][i] == player) or  # columns
        (board[0][0] == board[1][1] == board[2][2] == player) or  # top-left to bottom-right diagonal
        (board[0][2] == board[1][1] == board[2][0] == player)    # top-right to bottom-left diagonal
        for i in range(3)
    )
    return player if winning else None

def check_draw(board):
    return all(cell is not None for row in board for cell in row)

def next_player(board):
    """Count the current X and O numbers to find the next player."""
    num_X = sum(row.count('X') for row in board)
    num_O = sum(row.count('O') for row in board)
    return 'X' if num_X == num_O else 'O'

