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
    pass


def get_ship_location():
    pass


def computer_guess():
    pass


def count_hit_ships():
    pass

create_ships()
turns = 10