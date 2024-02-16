#Import for generating random ship locations
from random import randint

#Headline for the game - stays always on screen
print("Battleships Showdown")
#User chooses their own name and will be adressed by it.  
#Their board will also be referred to by the entered name.
player_name = input("Please enter your name: ")
print(player_name)
#The user chooses the size of the board in a specified range.
'''
def board_size_battleships(number):
    board_size_battleships(input("How big should the board grid be? Please choose between 4 and 8:"))
    if input <= 3:
        print("The chosen size is too small. Please enter a valid number.")
    elif input >= 9:
        print("The chosen size is too big. Please enter a valid number.")
    else:
        print("Thank you for choosing the board size. It will be", {board_size_battleships}, "x", {board_size_battleships})


board_size_battleships()
'''

#Creating the board
board = []
