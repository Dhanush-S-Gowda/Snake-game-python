# Snake Game

A classic Snake Game implemented in Python using the Turtle library.

## Introduction

This project is a simple implementation of the Snake Game using Python's Turtle library. The game involves controlling a snake to eat food pellets, growing longer with each pellet eaten, while avoiding collisions with the walls or itself.

## Features

- Classic Snake gameplay experience.
- Colorful visuals with Turtle graphics.
- Score tracking and display.
- Game over screen upon collision with walls or itself.
- Simple controls using arrow keys.

## Requirements

- Python 3.x
- Turtle library (Usually comes pre-installed with Python)

## Installation

1. Clone the repository to your local machine:

## How to Play

- Use the arrow keys to control the direction of the snake.
- The snake will continuously move in the current direction.
- Eat food pellets to grow longer and increase your score.
- Avoid collisions with the walls or the snake's own body.
- The game ends when the snake collides with a wall or itself.

# Snake Game - Documentation

This document provides an overview of the methods available in the Python files `food.py`, `scoreboard.py`, and `snake.py`, which are used in the Snake game.

## food.py

### Methods

#### `__init__(self)`

- Initializes a new instance of the `Food` class.
- Sets up attributes such as shape, color, size, and initial position of the food.

#### `refresh(self)`

- Generates random coordinates within the screen boundaries and moves the food to that position.

## scoreboard.py

### Constants

- `ALIGN`: Center alignment for text display.
- `FONT`: Font specifications for text display.

### Methods

#### `__init__(self)`

- Initializes a new instance of the `Scoreboard` class.
- Sets up attributes such as current score, font, color, and initial position of the scoreboard.

#### `game_over(self)`

- Displays "GAME OVER" message at the center of the screen.

#### `update_score(self)`

- Updates the displayed score on the scoreboard.

#### `increase_score(self)`

- Increments the score by 1 and updates the scoreboard display.

## snake.py

### Constants

- `MOVE_DIST`: Distance the snake moves in one step.
- `UP`, `DOWN`, `LEFT`, `RIGHT`: Directional constants for snake movement.
- `STARTING_POSITIONS`: Initial positions for the segments of the snake.

### Methods

#### `__init__(self)`

- Initializes a new instance of the `Snake` class.
- Sets up attributes such as segments list and the snake's head.

#### `create_snake(self)`

- Creates initial segments of the snake at predefined positions.

#### `add_segment(self, position)`

- Adds a new segment to the snake at the specified position.

#### `extend_segment(self)`

- Extends the length of the snake by adding a new segment to its tail.

#### `move(self)`

- Moves the snake forward by updating the positions of its segments.

#### Movement Methods: `up(self)`, `down(self)`, `left(self)`, `right(self)`

- Change the direction of the snake's head based on user input.

