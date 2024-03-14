from models.human_player import HumanPlayer
from models.smart_computer_player import SmartComputerPlayer
import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 5)
        self.human = HumanPlayer("Player")
        self.computer = SmartComputerPlayer("Computer", self.human)

    def start(self):
        print("Welcome to Guess the Number!")
        print("Try to guess the secret number between 1 and 5.")

    def check_guess(self, guess):
        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            return "too low"
        else:
            return "too high"

    def play_make_guess(self, player):
        guess = player.make_guess()
        result = self.check_guess(guess)
        print(f"{player.name}, your guess is {result}.")
        return result

    def end_game(self, winner):
        print(f"Congratulations, {winner.name}! You guessed the number {self.secret_number}.")

    def play(self):
        self.start()
        while True:
            human_result = self.play_make_guess(self.human)
            if human_result == "correct":
                self.end_game(self.human)
                break
            computer_result = self.play_make_guess(self.computer)
            if computer_result == "correct":
                self.end_game(self.computer)
                break