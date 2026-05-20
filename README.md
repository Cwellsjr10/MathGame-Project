# Math Game

A simple Python math quiz game that demonstrates object-oriented programming concepts like classes, inheritance, and encapsulation.

## Project Overview

This game is designed to help players practice basic math skills while showcasing a class-based implementation.

Key features:
- Multiple question rounds
- Encapsulated `Question` objects
- A base `Round` class with inherited round types
- Game state management through a `MathGame` class

## Files

- `Mathgame.py` — main game script

## Requirements

- Python 3.8 or newer

## How to Run

From the project folder, run:

```bash
python3 Mathgame.py
```

Then follow the prompts in the terminal.

## How the Game Works

- The player starts with `0` points.
- Correct answers add `100` points.
- Incorrect answers subtract `50` points.
- The player wins by reaching the target points (default `1000`).
- The game is split into rounds, each with its own question set.

## Object-Oriented Concepts Used

- `Question` class encapsulates a single math question and its correct answer.
- `Round` is a base class for shared round behavior.
- `AdditionRound`, `MultiplicationRound`, and `MixedRound` inherit from `Round`.
- `MathGame` manages the player score, target points, and the ordered rounds.

## Notes

- Make sure you enter numeric answers only.
- If you type invalid input, the game will ask you again.
