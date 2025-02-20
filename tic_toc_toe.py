import imput_type


# global variable list to make the tic toc toe board
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
i = 0

# function to display board nicely in console 
def current_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

# function to get whatever position the user wants to go in
def get_player_input():
    position = input("Enter position (1 - 9) ")
    position_type_and_value = imput_type.InputTypeChecker(position)
    if position_type_and_value.get_value == "exit":
        exit()
    return position_type_and_value.get_value() if position_type_and_value.get_type() == "Integer" and position_type_and_value.get_value() in range(1, 10) else print("Not valid Try Again") and get_player_input()



def update_board(position, player):
    if position in [1, 2, 3]:
        row, col = 0, position - 1
    elif position in [4, 5, 6]:
        row, col = 1, position - 4
    elif position in [7, 8, 9]:
        row, col = 2, position - 7
    else:
        return False

    if board[row][col] not in ["x", "o"]:
        board[row][col] = player
        return True
    else:
        return False



# transposing board to make the columns rows to be able to check for winner in the columns
def transpose_board():
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]


#check if there is a winner 
def check_winner():
    # checking each row if all are x or o to determine winner 
    try:
        for row in board:
            for player in ("x", "o"):
                if all(cells == player for cells in row):
                    return f"Player {player} wins!!"

        # checking columns by first transposing board with the transpose_board function and making the code more condensed
        for rows in transpose_board():
            for player in ("x", "o"):
                if all(cells == player for cells in rows):
                    return f"Player {player} wins!!"

        diagnole = []
        diagnole2 = []
        for rows in range(len(board)):
            diagnole.append(board[rows][rows])
            diagnole2.append(board[rows][-(rows + 1)])

        for player in ("x", "o"):
            if all(cell == player for cell in diagnole):
                return f"Player {player} wins!!"
            elif all(cell == player for cell in diagnole2):
                return f"Player {player} wins!!"
    except Exception as e:
        print(f"There was a problem checking results {e}")
    return None

# Modified while loop
while i in range(9):
    current_board(board)
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
    winner = check_winner()
    if winner:
        print(winner)
        break




