# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    
    # Count X's and O's on the board
    num_X = sum(row.count('X') for row in board)
    num_O = sum(row.count('O') for row in board)

    board[x][y] = 'X' if num_X == num_O else 'O'

    #Check rows
    for row in board:
        if row[0] is not None and len(set(row)) == 1:
            winner = row[0]
            break

    #Check columns
    for col in range((len(board))):
        column = [board[i][col] for i in range(len(board))]
        if column[0] is not None and len(set(column)) == 1:
            winner = column[0] 
            break

    #Check diagonals
    if board[0][0] is not None and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] is not None and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        winner = board[0][2]

    # Check for a draw
    if all(cell is not None for row in board for cell in row) and winner is None:
        print("It's a draw!")


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O"  # FIXME
