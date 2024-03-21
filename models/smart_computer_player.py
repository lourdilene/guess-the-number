from models.player import Player
from models.constantes import Constantes
from sklearn.linear_model import LinearRegression
import random
import numpy as np

class SmartComputerPlayer(Player):
    def __init__(self, name, game, human):
        super().__init__(name)
        self.model = LinearRegression()
        self.all_guesses = []
        self.game = game
        self.human = human

    def make_guess(self):
        if len(self.guesses) <= 3:
            # first_guess_result = self.all_guesses[0]
            # print(f"first_guess_result : {first_guess_result['result']}")
            # if first_guess_result['result'] == "too low":
            #     guess = first_guess_result['guess'] + 1
            # else: 
            #     guess = first_guess_result['guess'] -1
            guess = random.choice(self.game.possible_guesses)
            self.guesses.append(guess)
            # self.game.all_guesses.append(guess)
            print(f"{self.name}: your guess is: {guess}")
            print("Entrou aqui")
            return guess
        # else:
        # if len(self.guesses) == 0:
        #     print("entro aqui")
        #     self.guesses.append(99)
        #     return 99
        else:
            human_guesses = np.array(self.human.guesses)
            computer_guesses = np.array(self.guesses)

            all_guesses = np.concatenate((human_guesses, computer_guesses))

            all_guesses = np.unique(all_guesses)
            print(f"all_guesses: {all_guesses}")

            print(f"human_guesses: {human_guesses}")
            print(f"computer_guesses: {computer_guesses}")
            print(f"all_guesses: {all_guesses}")

            print(f"all_guesses[-1] + 1: {all_guesses[-1] + 1}")

            next_guess_label = all_guesses[-1] + 1

            X = human_guesses[:-1].reshape(-1, 1)
            y = np.roll(computer_guesses, -1).reshape(-1, 1)  # Rótulos deslocados uma posição para frente

            # Criar e treinar o modelo de regressão linear
            model = LinearRegression()
            model.fit(X, y)

            next_guess = model.predict([[next_guess_label]])
            next_guess = int(round(next_guess[0, 0]))
            print(f"next_guess: {next_guess}")

            self.guesses.append(next_guess)
            print(f"{self.name}: your guess is: {next_guess}")

            return next_guess
