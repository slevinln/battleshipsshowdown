# Import for generating random ship locations
from random import randint

# Headline for the game.
print("Battleships Showdown")

# User chooses their own name and will be adressed by it.
# Their board will also be referred to by the entered name.
player_name = input("Please enter your name: ")
print(player_name)

# The user chooses the size of the board in a specified range.


def board_size_battleships():
    grid_size = input("Please choose the grid size between 4 and 8: ")
    if int(grid_size) <= 3:
        print("The chosen size is too small. Please enter a valid number.")
    elif int(grid_size) >= 9:
        print("The chosen size is too big. Please enter a valid number.")
    else:
        print(f'The board size will be, {grid_size} x {grid_size}')


board_size_battleships()
