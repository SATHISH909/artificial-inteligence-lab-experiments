import math

# Function to print the Tic Tac Toe board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check if a player has won
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

# Check if the board is full
def is_full(board):
    return all(space != " " for space in board)

# Evaluate board (score for AI)
def evaluate(board):
    if check_winner(board, "O"):
        return 1   # AI wins
    elif check_winner(board, "X"):
        return -1  # Human wins
    else:
        return 0   # Draw

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Terminal condition
    if score == 1 or score == -1 or is_full(board):
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = " "
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = " "
        return best_score

# Function to find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = [" "] * 9
    print("🎮 Welcome to Tic Tac Toe (AI Edition)!")
    print("You are 'X' and AI is 'O'")
    print_board(board)

    while True:
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        board[move] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("🏆 You win!")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("💻 AI wins!")
            break
        if is_full(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_game()
