from models.player import Player
import random
from sklearn.linear_model import LinearRegression

class SmartComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.model = LinearRegression()
    
    def make_guess(self):
        if len(self.guesses) == 0:
            guess = random.randint(1, 5)
        else:
            X = [[guess] for guess in self.guesses]
            y = list(range(1, len(self.guesses) + 1))
            self.model.fit(X, y)
            last_guess = self.guesses[-1]
            guess = round(self.model.predict([[last_guess]])[0])
            guess = max(1, min(guess, 5))  # Ensure guess is within range
        print(f"{self.name} guesses: {guess}")
        self.guesses.append(guess)
        return guess