# Word Hunt
This code is a word search generator that creates word search puzzles of different levels of difficulty: easy, medium, and hard.
The puzzles are saved as images based on the selected level.\
The goal of the game is to find all of the hidden words.

## Usage
1. Run the Python script "word_hunt.py" in your Python environment.

        python word_hunt.py
2. Choose the difficulty level for the puzzle. You can choose from three levels: easy, medium, and hard.
3. The program will generate a Word Hunt puzzle with the specified level and save it as an image named "Word Hunt.png" in the current directory.

## Requirements

### Library
The code requires the following Python packages to be installed:

[string](https://docs.python.org/3/library/string.html): Used to access ASCII letters for filling the grid.\
[random](https://docs.python.org/3/library/random.html): Used to randomize word selection and grid generation.\
[PIL](https://pillow.readthedocs.io/en/stable/index.html): Python Imaging Library, used to create and save the image of the Word Hunt puzzle.

### Fonts
The code uses two fonts for generating image:

Melinda script.ttf: Used for the "Word Hunt" title on top of the puzzle image.\
RobotoMono-Thin.ttf: Used for displaying the grid and the list of words in different levels.

***Please ensure that the fonts "Melinda script.ttf" and "RobotoMono-Thin.ttf" are present in the "Fonts" folder, or update the font paths in the code if they are located elsewhere.***

## Difficulty Levels
The Word Hunt puzzles have the following characteristics for each difficulty level:

### Easy Level
- Number of Words: 12
- Grid Size: 10x10
- Words Hidden: Across and Down

### Medium Level
- Number of Words: 16
- Grid Size: 15x15
- Words Hidden: Across, Down, and Diagonally (no backward direction)

### Hard Level
- Number of Words: 28
- Grid Size: 20x20
- Words Hidden: Across, Down, and Diagonally (including backward direction)

## How it Works
1. The program reads a list of words from the file "words.txt" and randomly selects words (The amount is based on the chosen difficulty level).
2. It creates a grid of the specified size and fills it with random letters.
3. The words are inserted into the grid randomly in valid positions (following the specified directions) without overlapping with each other.
4. The final grid with the hidden words is displayed as an image using the Python Imaging Library (PIL) with the appropriate font and alignment.
