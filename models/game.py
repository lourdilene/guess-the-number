from models.human_player import HumanPlayer
from models.smart_computer_player import SmartComputerPlayer
from models.constantes import Constantes
import pdb

import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, Constantes.MAX_GUESS_NUMBER.value)
        self.human = HumanPlayer("Player", self)
        self.computer = SmartComputerPlayer("Computer", self)
        self.all_guesses = []
        self.possible_guesses = list(range(1, Constantes.MAX_GUESS_NUMBER.value + 1))

    def start(self):
        print("Welcome to Guess the Number!")
        print(f"Try to guess the secret number between 1 and {Constantes.MAX_GUESS_NUMBER.value}")

    def check_guess(self, guess):
        all_possible_guesses = self.possible_guesses
        index_guess = all_possible_guesses.index(guess)
        if guess == self.secret_number:
            return "correct"
        elif guess < self.secret_number:
            self.possible_guesses = all_possible_guesses[1 + index_guess:]
            return "too low"
        else:
            self.possible_guesses = all_possible_guesses[:index_guess]
            return "too high"

    def play_make_guess(self, player):
        guess = player.make_guess()
        result = self.check_guess(guess)
        print(f"{player.name}, your guess is {result}.")

        # print(f"secret_number: {self.secret_number}")
        print(f"all_guesses: {self.all_guesses}")
        print(f"possible_guesses: {self.possible_guesses}")

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