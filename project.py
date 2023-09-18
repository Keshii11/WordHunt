import string
import random
from PIL import Image, ImageDraw, ImageFont


def main():
    level = start_game()
    words, size, directions = create_game(level)
    grid = create_grid(size)

    for word in words:
        insert_word(grid, word.upper(), directions)

    fill_grid(grid)

    if level == 'easy':
        print_grid_easy(grid, words)
    elif level == 'medium':
        print_grid_medium(grid, words)
    elif level == 'hard':
        print_grid_hard(grid, words)


def start_game():
    print('Easy(12 words)\n A 10x10 grid - Words hidden across and down.\n')
    print('Medium(16 words)\n A 15x15 grid - Words hidden across, down, and diagonally, with no backwards.\n')
    print('Hard(28 words)\n A 20x20 grid - Words hidden across, down, and diagonally, with backwards.\n')
    while True:
        try:
            level = input('Choose the level: ').lower()
            if level == 'easy' or level == 'medium' or level == 'hard':
                break
            raise NameError
        except:
            print('Wrong name')
    return level


def create_game(level):
    if level == 'easy':
        number_words = 12
        size = 10
        directions = [(0, 1), (1, 0)]
    elif level == 'medium':
        number_words = 16
        size = 15
        directions = [(0, 1), (1, 0), (1, 1)]
    elif level == 'hard':
        number_words = 28
        size = 20
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    with open('words.txt', 'r') as file:
        words = []
        lines = file.readlines()
        while len(words) != number_words:
            word = random.choice(lines).rstrip()
            if word not in words and len(word) < size:
                words.append(word.capitalize())
        return words, size, directions


def create_grid(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def can_insert_word(grid, word, x, y, direction):
    for letter in word:
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid)) or grid[x][y] not in [' ', letter]:
            return False
        x += direction[0]
        y += direction[1]
    return True

def get_valid_positions(grid, word, directions):
    valid_positions = []

    for x in range(len(grid)):
        for y in range(len(grid)):
            for direction in directions:
                if can_insert_word(grid, word, x, y, direction):
                    valid_positions.append((x, y, direction))

    return valid_positions


def insert_word(grid, word, directions):
    valid_positions = get_valid_positions(grid, word, directions)

    if len(valid_positions) > 0:
        x, y, direction = random.choice(valid_positions)
        for letter in word.upper():
            grid[x][y] = letter
            x += direction[0]
            y += direction[1]


def fill_grid(grid):
    for x, row in enumerate(grid):
        for y, space in enumerate(row):
            if space == ' ':
                grid[x][y] = random.choice(string.ascii_uppercase)


def print_grid_easy(grid, words):
    image = Image.new('RGB', (595, 842), color='white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Fonts/Melinda script.ttf", 36)
    draw.text((173, 23), 'Word Hunt', fill=(0, 0, 0), font=font, align='center')

    font = ImageFont.truetype("Fonts/RobotoMono-Thin.ttf", 30)
    rows_y = 105
    for row in grid:
        draw.text((45, rows_y), '  '.join(row), fill=(0, 0, 0), font=font, align='center')
        rows_y += 54.5

    draw.line([(30, 645), (564, 645)], fill=(150, 150, 150), width=1)

    font = ImageFont.truetype("Fonts/RobotoMono-Thin.ttf", 18)
    words_y = 663
    for i in range(len(words) // 3):
        try:
            draw.text((52, words_y), words[i], fill=(0, 0, 0), font=font, align='left')
            draw.text((264, words_y), words[i + 4], fill=(0, 0, 0), font=font, align='left')
            draw.text((454, words_y), words[i + 8], fill=(0, 0, 0), font=font, align='left')
            words_y += 25
        except:
            continue

    image.save('Word Hunt.png')


def print_grid_medium(grid, words):
    image = Image.new('RGB', (595, 842), color='white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Fonts/Melinda script.ttf", 36)
    draw.text((173, 23), 'Word Hunt', fill=(0, 0, 0), font=font, align='center')

    font = ImageFont.truetype("Fonts/RobotoMono-Thin.ttf", 20)
    rows_y = 106
    for row in grid:
        draw.text((39, rows_y), '  '.join(row), fill=(0, 0, 0), font=font, align='center')
        rows_y += 35.85

    draw.line([(30, 645), (564, 645)], fill=(150, 150, 150), width=1)

    font = ImageFont.truetype("Fonts/RobotoMono-Thin.ttf", 14)
    words_y = 665
    for i in range(len(words) // 4):
        try:
            draw.text((36, words_y), words[i], fill=(0, 0, 0), font=font, align='left')
            draw.text((187, words_y), words[i + 4], fill=(0, 0, 0), font=font, align='left')
            draw.text((340, words_y), words[i + 8], fill=(0, 0, 0), font=font, align='left')
            draw.text((492, words_y), words[i + 12], fill=(0, 0, 0), font=font, align='left')
            words_y += 22.5
        except:
            continue

    image.save('Word Hunt.png')


def print_grid_hard(grid, words):
    image = Image.new('RGB', (595, 842), color='white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Fonts/Melinda script.ttf", 36)
    draw.text((173, 23), 'Word Hunt', fill=(0, 0, 0), font=font, align='center')

    font = ImageFont.truetype("Fonts/RobotoMono-Thin.ttf", 15)
    rows_y = 107
    for row in grid:
        draw.text((36, rows_y), '  '.join(row), fill=(0, 0, 0), font=font, align='center')
        rows_y += 26.43

    draw.line([(30, 645), (564, 645)], fill=(150, 150, 150), width=1)

    font = ImageFont.truetype("Fonts/RobotoMono-Thin.ttf", 14)
    words_y = 665
    for i in range(len(words) // 4):
        try:
            draw.text((36, words_y), words[i], fill=(0, 0, 0), font=font, align='left')
            draw.text((187, words_y), words[i + 7], fill=(0, 0, 0), font=font, align='left')
            draw.text((340, words_y), words[i + 14], fill=(0, 0, 0), font=font, align='left')
            draw.text((492, words_y), words[i + 21], fill=(0, 0, 0), font=font, align='left')
            words_y += 20
        except:
            continue

    image.save('Word Hunt.png')


if __name__ == "__main__":
    main()