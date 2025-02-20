import input_type

# Global variable list to make the tic-tac-toe board
board_new = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of winning combinations (rows, columns, diagonals)
winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

# Function to display the board nicely in the console
def current_board_new(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to get the position the user wants to go in
def get_player_input():
    while True:
        position = input("Enter position (1 - 9) ")
        position_type_and_value = input_type.InputTypeChecker(position)
        if position_type_and_value.get_value() == "exit":
            exit()
        if position_type_and_value.get_type() == "Integer" and position_type_and_value.get_value() in range(1, 10):
            return position_type_and_value.get_value()
        else:
            print("Not valid. Try Again")

# Function to update the board with the player's move
def update_board(position, player):
    if board_new[position - 1] not in ["x", "o"]:
        board_new[position - 1] = player
        return True
    else:
        return False

# Function to check if there is a winner
def check_winner():
    for a, b, c in winning_combinations:
        if board_new[a] == board_new[b] == board_new[c]:
            return True
    return False

# Main game loop
i = 0
x = 9
winner = False
while i in range(x):
    current_board_new(board_new)
    if i % 2 == 0:
        player = "x" 
        print("Player x turn. Please enter a position")
    else:
        player = "o"
        print("Player o turn. Please enter a position")
    position = get_player_input()
    if update_board(position, player):
        i += 1
    else:
        print("Position already taken please try again")
        continue
    if check_winner():
        x = i + 1
        print(f"Player {player} wins!!!")
        break
else:
    print("It's a draw!")




