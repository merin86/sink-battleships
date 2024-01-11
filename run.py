import random


# On this board the ships are placed out and hidden
hidden_board_user = [[" "] * 5 for x in range(5)]
hidden_board_computer = [[" "] * 5 for x in range(5)]

# This board is updated during the game by showing the misses and hits of the ships
visible_board_user = [[" "] * 5 for x in range(5)]
visible_board_computer = [[" "] * 5 for x in range(5)]