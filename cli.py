# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logic

# User Interaction
def show_board(board):
    for row in board:
        print(row)

def get_user_move(board):
    while True:
        user_input = input('Please make your movement by typing x,y (e.g., 1,2):').split(',')
        if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit(): # Check if the input is legal
            x, y = int(user_input[0]), int(user_input[1])
            if 0 <= x <= 2 and 0 <= y <= 2: # Check if the input is within boundary
                if board[x][y] is None:  # Check if the position is empty
                    return x, y
                else:
                    print("This position is already taken. Please choose another one.")
            else:
                print("Invalid coordinates. Please enter values between 0 and 2.")
        else:
            print("Invalid input. Please enter in the format x,y.")

# Reminder to check all the tests

if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    print("TODO: take a turn!")
    show_board(board)
    while winner == None:
        next_player = logic.next_player(board)

        # TODO: Input a move from the player.
        x, y = get_user_move(board)
        board[x][y] = next_player

        #TODO: Check winner.
        winner = logic.get_winner(board, next_player)

        # Check for a draw
        logic.check_draw(board)

        # TODO: Update the board.
        show_board(board)

        # TODO: Update who's turn it is.
        print(f"It's {logic.next_player(board)}'s turn!")

    print ('The winner is', winner)
