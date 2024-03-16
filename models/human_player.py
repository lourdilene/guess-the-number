from models.player import Player

class HumanPlayer(Player):
    def __init__(self, name, game):
        super().__init__(name)
        self.game = game

    def make_guess(self):
        guess = int(input(f"{self.name}, enter your guess: "))
        self.guesses.append(guess)
        self.game.all_guesses.append(guess)
        return guess