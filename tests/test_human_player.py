from models.human_player import HumanPlayer
from unittest.mock import patch
import io

def test_make_guess():
    player = HumanPlayer("TestPlayer")

    inputs = ['3']
    with patch('builtins.input', side_effect=inputs) as mocked_input:
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            guess = player.make_guess()

    assert player.guesses == [3]

    assert guess == 3

    assert mocked_input.call_args_list == [(('TestPlayer, enter your guess: ',),)]
