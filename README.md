# hangman but in Python

Welcome to **hangman**, a Python-based version of the classic word-guessing game.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [License](#license)

## Introduction

**Hangman** is a word-guessing game where the player tries to guess a secret word by suggesting letters. This version of Hangman includes several enhancements and is implemented in Python.

## Features

- Randomly selects a secret word from a predefined list.
- Displays the current progress of the guessed word.
- Provides a total of `length of the word + 3` attempts.
- Tracks and informs the player of previously guessed letters.
- Notifies the player of wins or losses.

## Installation

1. Ensure you have Python installed on your machine (Python 3.6 or higher).
2. Clone the repository or download the `hangman.py` script.

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory where the `hangman.py` file is located.
3. Run the script using the following command:

    ```bash
    python hangman.py
    ```

## Game Rules

1. The game randomly selects a secret word from a predefined list.
2. The player is given `length of the word + 3` attempts to guess the word.
3. The player guesses one letter at a time.
4. If the guessed letter is in the secret word, it will be revealed in its correct positions.
5. If the guessed letter is not in the secret word, the number of attempts remaining will decrease.
6. The game ends when the player either correctly guesses the word or runs out of attempts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy playing **hangman** and happy guessing!
