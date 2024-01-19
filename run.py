from random import randint


"""
On this board the ships are placed out and hidden
"""
hidden_board_user = [[" "] * 5 for x in range(5)]
hidden_board_computer = [[" "] * 5 for x in range(5)]

"""
This board is updated during the game by showing the misses and
hits of the ships
"""
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


def create_ships(board):
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
    row = input("Enter the row of the ship(1-5):\n").upper()
    while not row or row not in "12345":
        print('Please choose a valid row(1-5)')
        row = input("Enter the row of the ship:\n").upper()
    column = input("Enter the column of the ship(A-E):\n").upper()
    while not column or column not in "ABCDE":
        print('Please choose a valid column(A-E)')
        column = input("Enter the column of the ship:\n").upper()
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


def setup_game():
    """
    This function sets up the game by placing ships on the hidden boards
    of both the user and the computer.
    """
    create_ships(hidden_board_user)
    create_ships(hidden_board_computer)


def play():
    """
    This function manages turns and checks for correct input by both player
    and computer. In the end of the game it announces the winner, or if there's
    a tie.
    """
    turns = 10
    while turns > 0:
        # Player's turn
        print('Your turn!')
        print("Computer's board:")
        print_board(visible_board_computer)
        while True:
            row, column = get_ship_location()

            if visible_board_computer[row][column] == "-":
                print("You guessed that one already. Try again.")
            elif visible_board_computer[row][column] == "X":
                print("You already hit this ship. Try again.")
            else:
                break

        if hidden_board_computer[row][column] == "X":
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

        # Computer's turn
        print("\nComputer's turn!")
        print("Your board:")
        print_board(visible_board_user)
        while True:
            guess_row, guess_column = computer_guess()

            if visible_board_user[guess_row][guess_column] in ["-", "X"]:
                continue
            else:
                break

        if hidden_board_user[guess_row][guess_column] == "X":
            print("Computer hit one of your battleships!")
            visible_board_user[guess_row][guess_column] = "X"
        else:
            print("Computer MISS!")
            visible_board_user[guess_row][guess_column] = "-"

        if count_hit_ships(visible_board_user) == 5:
            print("All your battleships are sunk! You lose!")
            break

        if turns == 0:
            player_hits = count_hit_ships(visible_board_computer)
            computer_hits = count_hit_ships(visible_board_user)
            print("Game over! Counting the number of hits...")
            print(f"Your hits: {player_hits}")
            print(f"Computer's hits: {computer_hits}")

            if player_hits > computer_hits:
                print("You won by sinking more ships!")
            elif computer_hits > player_hits:
                print("Computer won by sinking more ships!")
            else:
                print("It's a tie! Both sunk the same number of ships.")
            break


def start_game():
    """
    This function makes it possible for the player to play the game again.
    """
    global hidden_board_user, hidden_board_computer, \
    visible_board_user, visible_board_computer

    hidden_board_user = [[" "] * 5 for _ in range(5)]
    hidden_board_computer = [[" "] * 5 for _ in range(5)]
    visible_board_user = [[" "] * 5 for _ in range(5)]
    visible_board_computer = [[" "] * 5 for _ in range(5)]

    setup_game()
    play()


intro_text = [
    "**************************************************",
    "* Welcome to Sink Battleships! Try to guess     *",
    "* where the five ships are hiding on the        *",
    "* computer board. All five ships are 1x1 in the *",
    "* grid and are randomly placed if you choose to *",
    "* play. You have 10 tries to guess where all    *",
    "* the ships exist. Good luck!                   *",
    "**************************************************"
]


"""
Main logic and initial interaction.
"""
if __name__ == "__main__":
    for line in intro_text:
        print(line)
    while True:
        response = input("Wanna play Sink Battleships? (Y/N):\n").upper()
        if response == "Y":
            print("Starting game...")
            start_game()
            play_again = input("Do you want to play again? (Y/N):\n").upper()
            if play_again == "Y":
                print("Starting a new game...")
                start_game()
            else:
                print("Thanks for playing! Goodbye!")
                break
        elif response == "N":
            print("Okay, maybe another time.")
            break
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
