# Landscaping Business Game

This is a simple text-based game where the player starts a landscaping business with just their teeth and aims to earn money, buy tools, and eventually hire a team of starving students to win the game.

## Game Rules

1. The player starts with $0 and their teeth as the only tool.
2. The player can spend the day cutting lawns and earn money based on the tools they own.
3. The player can buy tools to increase their earning potential:
    - Rusty Scissors: $5, earns $5 per day
    - Old-timey Push Lawnmower: $25, earns $50 per day
    - Fancy Battery-powered Lawnmower: $250, earns $100 per day
    - Team of Starving Students: $500, earns $250 per day
4. The player can sell tools for half their purchase price.
5. The player wins the game when they have a team of starving students and $1000.

## How to Play

1. Run the `landscaping_game.py` script.
2. Follow the on-screen prompts to make choices:
    - Spend the day cutting lawns to earn money.
    - Buy tools to increase your earning potential.
    - Sell tools to get some money back.
    - Reset the game to start over.
    - Quit the game when you're done playing.
3. Keep playing until you reach the winning condition of having a team of starving students and $1000.

## Prerequisites

-   Python 3.x

## How to Run

1. Clone the repository or download the `landscaping_game.py` script.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the following command:

    ```
    python landscaping_game.py
    ```

4. The game will start, and you can follow the on-screen prompts to play.

## Game Features

-   Multiple tools to buy and use for earning money
-   Ability to sell tools for half their purchase price
-   Game reset option to start over
-   Win condition: Having a team of starving students and $1000

## Code Structure

-   `main()`: The main game loop that handles the game flow and user interactions.
-   `earn_money(tools)`: Calculates the player's earnings based on the tools they own.
-   `buy_tool(tools, money)`: Allows the player to buy tools and updates their tools and money.
-   `sell_tool(tools, money)`: Allows the player to sell tools and updates their tools and money.

# Hangman Game

This is a simple command-line implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list and the player must guess the word by suggesting letters within a limited number of attempts.

## How to Play

1. Run the Python script `hangman.py` in your terminal or command prompt.
2. The game will display a series of underscores representing the letters in the word to be guessed.
3. Enter a letter as your guess.
    - If the letter is in the word, it will be revealed in its correct position(s).
    - If the letter is not in the word, you will lose a life and the Hangman stage will be updated.
4. Keep guessing letters until you either guess the entire word or run out of lives.
5. If you guess the word correctly, you win the game. If you run out of lives, you lose and the correct word will be revealed.
6. After the game ends, you will be prompted to play again. Enter 'y' to play another round or 'n' to exit the game.

## Requirements

-   Python 3.x
-   `Hangman_words` module (contains the list of words for the game)
-   `Hangman_art` module (contains the ASCII art for the game logo and Hangman stages)

Make sure the `Hangman_words.py` and `Hangman_art.py` files are in the same directory as the `hangman.py` script.

## Code Structure

The code consists of the following main components:

1. `clear_screen()` function:

    - Clears the console screen for a better user experience.
    - Uses the appropriate command based on the operating system ('cls' for Windows, 'clear' for Linux and Mac).

2. `play_hangman()` function:

    - The main game loop that handles the gameplay.
    - Selects a random word from the word list and initializes variables.
    - Prompts the user to guess letters and updates the game state accordingly.
    - Checks for win or loss conditions and displays appropriate messages.
    - Offers the option to play again after the game ends.

3. Input validation:

    - Validates user input to ensure it is a single alphabetic character and not already guessed.
    - Prompts the user to enter a valid input if the input is invalid.

4. Game flow:
    - The game starts by displaying the game logo and the initial word with underscores.
    - The player is prompted to guess a letter in each iteration of the game loop.
    - If the guessed letter is in the word, it is revealed in the display.
    - If the guessed letter is not in the word, the player loses a life and the Hangman stage is updated.
    - The game ends when either the player guesses the entire word or runs out of lives.
    - The player is given the option to play again or exit the game.

## Customization

You can customize the game by modifying the following:

-   `Hangman_words.py`: Add or remove words from the `word_list` to change the words used in the game.
-   `Hangman_art.py`: Modify the ASCII art for the game logo and Hangman stages to personalize the game's appearance.

## Acknowledgements

This Hangman game implementation is inspired by the classic word-guessing game and is created as a fun programming exercise.

Feel free to contribute to the code, report any issues, or suggest enhancements on the GitHub repository.

Enjoy playing Hangman!


# Tic-Tac-Toe Game

This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns marking spaces on a 3x3 grid until one player wins or the game ends in a draw.

## How to Play

1. Run the Python script to start the game.
2. The game board will be displayed with labeled columns (1, 2, 3) and rows (A, B, C).
3. Players take turns entering their moves by specifying the cell they want to mark.
    - To make a move, enter the column letter (A, B, or C) followed by the row number (1, 2, or 3).
    - For example, to mark the cell in the first row and first column, enter "A1".
4. The game will validate each move and update the board accordingly.
5. The game continues until one of the following conditions is met:
    - A player wins by marking three cells in a row, column, or diagonal.
    - All cells are filled, resulting in a draw.
6. After the game ends, players can choose to play again or quit.

## Game Features

-   Player-friendly move input using column letters and row numbers.
-   Input validation to ensure valid moves within the board range.
-   Clear display of the game board after each move.
-   Detection of winning conditions and declaration of the winner.
-   Detection of a draw when all cells are filled without a winner.
-   Option to play multiple rounds or quit after each game.

## Requirements

-   Python 3.x

## How to Run

1. Clone the repository or download the Python script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the following command:

    ```
    python tic_tac_toe.py
    ```

    Replace `tic_tac_toe.py` with the actual filename if necessary.

4. Follow the on-screen instructions to play the game.

## Code Structure

The code is organized into several functions:

-   `display_board(board)`: Displays the current state of the game board.
-   `check_win(board, player)`: Checks if a player has won the game.
-   `make_move(board, player, row, col)`: Makes a move on the game board.
-   `play_game()`: Main function that orchestrates the gameplay.

The game logic is implemented in the `play_game()` function, which handles player turns, move validation, and game termination conditions. The game board is represented as a 3x3 matrix using a list of lists.

## Acknowledgments

This Tic-Tac-Toe game implementation is a beginner-friendly project inspired by various online tutorials and examples. It serves as a learning resource for those starting with Python programming and game development.

Feel free to modify and enhance the game as per your requirements. Enjoy playing Tic-Tac-Toe!
