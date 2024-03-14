from models.player import Player

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_guess(self):
        guess = int(input(f"{self.name}, enter your guess: "))
        self.guesses.append(guess)
        return guess