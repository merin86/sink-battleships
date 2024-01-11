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


def count_hit_ships():
    pass

create_ships()
turns = 10