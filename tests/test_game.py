from models.game import Game
from unittest.mock import patch
import io

def test_game(monkeypatch):
    # Set a fixed secret number for testing
    with monkeypatch.context() as m:
        m.setattr('random.randint', lambda a, b: 3)
        
        game_instance = Game()
        
        # Set up input for human player guesses
        inputs = ['2', '4']
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
                game_instance.play()
        
        output = fake_out.getvalue()
        
        assert "Welcome to Guess the Number!" in output
        assert "Player, your guess is too low." in output
        assert "Computer guesses: 3" in output
        assert "Computer, your guess is correct." in output
        assert "Congratulations, Computer! You guessed the number 3." in output