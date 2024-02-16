#Import for generating random ship locations
from random import randint

#Headline for the game - stays always on screen
print("Battleships Showdown")
#User chooses their own name and will be adressed by it.  
#Their board will also be referred to by the entered name.
player_name = input("Please enter your name:")
print(player_name)