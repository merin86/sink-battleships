from random import randint


# On this board the ships are placed out and hidden
hidden_board_user = [[" "] * 5 for x in range(5)]
hidden_board_computer = [[" "] * 5 for x in range(5)]

# This board is updated during the game by showing the misses and hits of the ships
visible_board_user = [[" "] * 5 for x in range(5)]
visible_board_computer = [[" "] * 5 for x in range(5)]

def print_board(board):
    """
    This function prints the board with row numbers on the left
    and column labels on the top, creating a visual representation
    of the game board.
    """
    print("  A B C D E")
    print("  +-+-+-+-+")
    for row_number, row in enumerate(board, start=1):
        print(f"{row_number}|{'|'.join(row)}|")

# Converts a letter to its corresponding numerical value
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}


def create_ships():
    """
    This function places five ships randomly on the board, making
    sure not to overlap them by checking if a chosen position is
    already occupied before placing a ship.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 4), randint(0, 4)
        board[ship_row][ship_column] = "X"


def get_ship_location():
    """
    This function ensures that the user provides valid row and column
    inputs for the location of a ship on the game board.
    """
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345":
        print('Please choose a valid row as the current selection is not suitable')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDE":
        print('Please choose a valid column as the current selection is not suitable')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def computer_guess():
    """
    This function generates a random guess for the computer's move
    on the game board.
    """
    guess_row, guess_column = randint(0, 4), randint(0, 4)
    return guess_row, guess_column


def count_hit_ships(board):
    """
    This function provides the count of hit ships on the game board
    by iterating through each element and counting the occurrences
    of the "X" symbol.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


"""
From here on is the main logic of the battleship game.
"""
if __name__ == "__main__":
    create_ships(hidden_board_user)
    create_ships(hidden_board_computer)

    turns = 10
    while turns > 0:
        # Player's turn
        print('Your turn!')
        print_board(visible_board_computer)
        row, column = get_ship_location()

        if visible_board_computer[row][column] == "-":
            print("You guessed that one already.")
        elif hidden_board_computer[row][column] == "X":
            print("HIT!")
            visible_board_computer[row][column] = "X"
            turns -= 1
        else:
            print("MISS!")
            visible_board_computer[row][column] = "-"
            turns -= 1
        
        if count_hit_ships(visible_board_computer) == 5:
            print("You sank all battleships! You win!")
            break

        print("You have " + str(turns) + " turns left")