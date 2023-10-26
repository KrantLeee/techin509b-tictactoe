# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    print("TODO: take a turn!")
    while winner == None:
        
       

        # TODO: Show the board to the user.
        for a in range(len(board)):    
            print (board[a]) 

        # TODO: Input a move from the player.
        while True: 
            user_input = input('Please make your movement by typing x,y (e.g., 1,2):').split(',')
            if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit(): # Check if the input is legal
                x, y = int(user_input[0]), int(user_input[1])
                if 0 <= x <= 2 and 0 <= y <= 2: # Check if the input is within boundary
                    if board[x][y] is None:  # Check if the position is empty
                        break
                    else:
                        print("This position is already taken. Please choose another one.")
                else:
                    print("Invalid coordinates. Please enter values between 0 and 2.")
            else:
                print("Invalid input. Please enter in the format x,y.")

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
            break

        # TODO: Update the board.

        # TODO: Update who's turn it is.
        if winner is None:
          print("It's X's turn") if board[x][y] == 'O' else print("It's O's turn")
        else:
          break


    print ('The winner is', winner)
