from models.game import Game
from unittest.mock import patch
from models.constantes import Constantes
import io
import random

def test_start_prints():
    game_instance = Game()
    with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
        game_instance.start()
    output = fake_out.getvalue()
    assert "Welcome to Guess the Number!" in output
    assert f"Try to guess the secret number between 1 and {Constantes.MAX_GUESS_NUMBER.value}" in output

def test_check_guess():
    game_instance = Game()
    game_instance.secret_number = 5

    assert game_instance.check_guess(5) == "correct"
    assert game_instance.check_guess(3) == "too low"
    assert game_instance.check_guess(7) == "too high"
    assert game_instance.check_guess(20) == "too distance"

def test_play_make_guess():
    game_instance = Game()
    game_instance.secret_number = 5
    game_instance.possible_guesses = [1, 2, 3, 4, 5]

    with patch('builtins.input', return_value="4"):
        assert game_instance.play_make_guess(game_instance.human) == "too low"

    with patch('builtins.input', return_value="5"): 
        assert game_instance.play_make_guess(game_instance.human) == "correct"

def test_end_game():
    game_instance = Game()
    with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
        game_instance.end_game(game_instance.human)
    output = fake_out.getvalue()
    assert f"Congratulations, {game_instance.human.name}! You guessed the number {game_instance.secret_number}." in output