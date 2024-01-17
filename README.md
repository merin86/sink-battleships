# Sink Battleships - Python Battleship Game

[The actual website](https://sink-battleships-0da166920aef.herokuapp.com/)

Welcome to Sink Battleships, a classic game created using Python. Try to guess where all the boats are hiding on the open sea!

![Mockup](docs/images/responsive.jpg)

## Content Index

- [Game Description](#game-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Validator](#validator)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

## Game Description

Sink Battleships is a textual version of the classic Battleship game. Players alternate turns with the computer, aiming to tactically locate and destroy the opponent's ships on a 5x5 grid. The user and the computer have 10 rounds each to try to sink all the ships. This game offers an easy and fun method to test your strategic skills and fortune against an artificial intelligence adversary.

If you've never played Battleship before, here's a description:
[Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

## Features

### Start The Game
- Before the game starts, a message appears asking if the user wants to play. Here the user can choose yes or no.

<img src="docs/images/start.jpg">

### Boards
- When the game starts, it is the user who starts selecting coordinates on the computers board. The user sees the board as a grid of cells and now has the option to first select a row (1-5) and then a column (A-E).
- After the player has made his choices, the application tells if there was a miss or a hit, as well as how many rounds the player has left. Then the user's board appears and the computer makes a randomized guess. The text below the user's board reveals if the computer had a miss or a hit. Then it's the user's turn again.

    <img src="docs/images/boards.jpg">

### Indicators
- During the game, the boards are updated according to the guesses that are made. If someone hits a ship this is shown as an "X" on the board and if they miss this is shown as a "-".

<img src="docs/images/indicators.jpg">

### Game Over
- When all 10 rounds are completed, the application says the game is over. Number of hits is counted and the winner is announced. If user and computer hit the same number of ships, it will be a tie.
- The user is then asked if they want to play again.

<img src="docs/images/gameover.jpg">

### Wrong Inputs
- If the user enters blank or incorrect data at the start of the game, a message appears and the game will prompt the user to re-enter a valid input.

<img src="docs/images/invalid1.jpg">

- If the user enters blank or incorrect data when a row is to be selected, a message appears and the game will prompt the user to re-enter a valid input.

<img src="docs/images/invalid2.jpg">

- If the user enters blank or incorrect data when a column is to be selected, a message appears and the game will prompt the user to re-enter a valid input.

<img src="docs/images/invalid3.jpg">

## Technologies Used

[Python](https://www.python.org/)  -  The programming language used for game development.

## Testing

- All the features mentioned above have been manually tested and work without hindrance.

## Validator

- Only one error message appeared when the code was tested through the [Pep8 Validator](https://pep8ci.herokuapp.com/). The code on this line is considered too long. However, this code is not visible in the terminal, so I assumed there should be no problem.

<img src="docs/images/linter.jpg">

## Bugs

## Deployment

## Credits