from word_hunt import start_game, create_game, create_grid
from unittest.mock import patch

@patch('builtins.input', side_effect=['Easy', 'Medium', 'Hard', 'EASY', 'MEDIUM', 'HARD'])
def test_create_game(mock_input):
    expected_outputs = ['easy', 'medium', 'hard']

    for output in expected_outputs:
        level = start_game()
        assert level == output

def test_create_game():
    words, size, directions = create_game('easy')
    assert len(words) == 12
    assert size == 10
    assert len(directions) == 2

    words, size, directions = create_game('medium')
    assert len(words) == 16
    assert size == 15
    assert len(directions) == 3

    words, size, directions = create_game('hard')
    assert len(words) == 28
    assert size == 20
    assert len(directions) == 4

def test_create_grid():
    grid = create_grid(10)
    assert len(grid) == 10

    grid = create_grid(15)
    assert len(grid) == 15

    grid = create_grid(20)
    assert len(grid) == 20

