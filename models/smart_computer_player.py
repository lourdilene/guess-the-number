from models.player import Player
from models.constantes import Constantes
from sklearn.linear_model import LinearRegression
import random
import numpy as np

class SmartComputerPlayer(Player):
    def __init__(self, name, game):
        super().__init__(name)
        self.model = LinearRegression()
        self.game = game

    def make_guess(self):
        if len(self.guesses) == 0:
            guess = random.choice(self.game.possible_guesses)
            self.guesses.append(guess)
            self.game.all_guesses.append(guess)
            print(f"{self.name}: your guess is: {guess}")
            return guess
        else:
            all_guesses = np.array(self.game.all_guesses).reshape(-1, 1)  # Transforma a lista de palpites em uma matriz 2D
            possible_guesses = self.game.possible_guesses[:len(self.guesses)]  # Ajusta o número de palpites possíveis

            if len(all_guesses) != len(self.guesses):
                all_guesses = all_guesses[:len(possible_guesses)]

            self.model.fit(all_guesses, possible_guesses)  # Ajusta o modelo aos palpites e aos palpites possíveis

            # Previsão do próximo palpite
            # Faz a previsão para o próximo número após o último palpite
            next_guess = self.model.predict([[self.guesses[-1] + 1]])[0]
            
            # Garante que o palpite esteja dentro do intervalo [1, 50]
            next_guess = min(possible_guesses, key=lambda x: abs(x - next_guess))

            # Adiciona o palpite à lista de palpites e imprime
            self.guesses.append(next_guess)
            self.game.all_guesses.append(next_guess)
            print(f"{self.name}: your guess is: {next_guess}")

            return next_guess
