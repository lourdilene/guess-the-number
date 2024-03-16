from models.player import Player
from models.constantes import Constantes
from sklearn.linear_model import LinearRegression
import random
import pdb
import numpy as np

class SmartComputerPlayer(Player):
    def __init__(self, name, game):
        super().__init__(name)
        self.model = LinearRegression()
        self.game = game

    def make_guess(self):
        guess = np.median(self.game.possible_guesses)
        guess = max(1, min(int(round(guess)), Constantes.MAX_GUESS_NUMBER.value))
        self.guesses.append(guess)
        self.game.all_guesses.append(guess)
        print(f"{self.name}: your guess is: {guess}")
        return guess
