# Tic-Tac-Toe

# Create the game board
board = [" " for _ in range(9)]

# Function to display the game board
def display_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if the game has been won
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combination in win_combinations:
        if all(board[index] == player for index in combination):
            return True
    return False

# Function to play the game
def play_game():
    current_player = "X"
    game_over = False

    while not game_over:
        display_board()
        print("It's", current_player, "turn.")
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == " ":
            board[position] = current_player

            if check_win(current_player):
                display_board()
                print(current_player, "wins!")
                game_over = True
            elif " " not in board:
                display_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()