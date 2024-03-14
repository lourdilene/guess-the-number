from models.player import Player
from models.human_player import HumanPlayer
import random
from sklearn.linear_model import LinearRegression

class SmartComputerPlayer(Player):
    def __init__(self, name, human_player):
        super().__init__(name)
        self.model = LinearRegression()
        self.human_player = human_player
    
    def make_guess(self):
        all_guesses = self.guesses + self.human_player.guesses
        if len(self.guesses) == 0:
            guess = random.randint(1, 5)
        else:
            X = [[guess] for guess in all_guesses]
            y = list(range(1, len(all_guesses) + 1))
            self.model.fit(X, y)
            last_guess = all_guesses[-1]
            guess = round(self.model.predict([[last_guess]])[0])
            guess = max(1, min(guess, 5))  # Ensure guess is within range
        print(f"{self.name} guesses: {guess}")
        self.guesses.append(guess)
        return guess