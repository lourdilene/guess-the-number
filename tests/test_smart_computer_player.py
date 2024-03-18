import unittest
from unittest.mock import Mock, patch
import numpy as np
from models.smart_computer_player import SmartComputerPlayer

class TestSmartComputerPlayer(unittest.TestCase):
    def test_make_guess_first_guess(self):
        game_mock = Mock()
        game_mock.possible_guesses = [1, 2, 3, 4, 5]
        game_mock.all_guesses = []
        player = SmartComputerPlayer("Computer", game_mock)

        with patch('random.choice', return_value=3):
            guess = player.make_guess()

        self.assertEqual(guess, 3)
        self.assertEqual(player.guesses, [3])
        self.assertEqual(game_mock.all_guesses, [3])

    def test_make_guess_subsequent_guess(self):
        game_mock = Mock()
        game_mock.possible_guesses = [1, 5]
        game_mock.all_guesses = [2, 3, 4]
        player = SmartComputerPlayer("Computer", game_mock)
        player.guesses = [2, 3]

        with patch.object(player.model, 'predict', return_value=np.array([4])):
            guess = player.make_guess()
        
        self.assertEqual(guess, 5)
        self.assertEqual(player.guesses, [2, 3, 5])
        self.assertEqual(game_mock.all_guesses, [2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
