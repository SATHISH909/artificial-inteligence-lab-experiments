# Tic Tac Toe Game in Python (Two Players)

# Function to print the game board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(space != " " for space in board)

# Main game function
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    print("🎮 Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Take user input
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number (1-9).")
            continue

        # Make the move
        board[move] = current_player
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            print(f"🏆 Player {current_player} wins!")
            break

        # Check for draw
        if is_full(board):
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
