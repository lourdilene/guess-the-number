from models.human_player import HumanPlayer
from models.smart_computer_player import SmartComputerPlayer
from models.constantes import Constantes
from utils.clear_console import clear_console
import pdb
import os

import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, Constantes.MAX_GUESS_NUMBER.value)
        self.human = HumanPlayer("Player", self)
        self.computer = SmartComputerPlayer("Computer", self)
        self.all_guesses = []
        self.result_guesses = []
        self.possible_guesses = list(range(1, Constantes.MAX_GUESS_NUMBER.value + 1))

    def start(self):
        print("Welcome to Guess the Number!")
        print(f"Try to guess the secret number between 1 and {Constantes.MAX_GUESS_NUMBER.value}")

    def check_guess(self, guess):
        if guess not in self.possible_guesses:
            return "too distance"
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

        #clear_console()

        self.result_guesses.append(f"{player.name}, your guess {guess} is {result}.")

        for result_guess in self.result_guesses:
            print(result_guess)

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