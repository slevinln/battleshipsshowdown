# Battleships Showdown

Battleships Showdown is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

The user chooses the size of the grid and number of battleships and tries to defeat the computer opponent.
Each battleship has the size of one square on the board.

Current state: Unfinished

## Gameplay

The game asks for three inputs at the start: username, grid size and number of ships.

Two boards are then generated, one for the player where his ships are randomly placed.
The second board represents the computer and does not show the location of his ships. 

The user makes his guesses on this board.
The player and computer take turns. By choosing a spot on the row and column, 
he takes a shot at the computer's ships.

Hits or misses are marked on the board. The computer makes a random guess afterwards.

The game ends when either all ships from the player (loss) or the computer (win) have been hit.

## Features

### Existing features

Users can choose their own name.

Users can choose the grid size.

### Features to be added

User can choose the number of ships - possibly with differentiation between player and computer.

Two grids gets generated and ships are randomly placed.

The player takes a shot and gets feedback if he hit/missed.
If he chooses a space outside the grid, he gets feedback that his input was invalid and to choose again.
The grid with the computer's ships gets updated.

The computer takes a shot and the player gets feedback if it was a hit or miss.
The grid with the player's ships gets updated.

When all ships from the player or computer have been hit, the game displays a win or loss message.
Afterwards, the game asks if a rematch should be started.

## Testing

The code has been run through the CI Python Linter and reported no issues.

The functionality has been tested in the Gitpod terminal and the Heroku terminal.


I have used the PEP8 validator on https://www.codewof.co.nz/style/python3/ to check the style.

It recommended use of docstrings on line 1 and 15, but due to the short length of the comments I left them as is.

## Deployment

This project was deployed on the CI mock terminal on Heroku.

To deploy yourself, fork or clone this repository and create a new Heroku app. 

Set the buildbacks to Python and NodeJS in that order.

Link the Heroku app to the repository and click on Deploy.

## Credits

Code Institute for the deployment terminal.