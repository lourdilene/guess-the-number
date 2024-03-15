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
        self.last_result = None

    def make_guess(self):
        all_guesses = self.game.all_guesses
        print(f"all_guesses: {all_guesses}")

        pdb.set_trace()

        X = np.array([[i] for i in range(1, len(all_guesses) + 1)])  # Números de tentativas
        y = np.array(all_guesses)  # Palpites correspondentes

        # Treinar o modelo de regressão linear
        model = LinearRegression()
        model.fit(X, y)

        # Fazer uma previsão do próximo palpite
        next_guess_round = round(model.predict([[len(all_guesses) + 1]])[0])
        next_guess = max(1, min(next_guess_round, 50))  # Garantir que o palpite esteja dentro do intervalo [1, 50]

        print(f"Próximo palpite previsto: {next_guess}")

        print(f"{self.name} guesses: {self.guesses}")
        #self.game.all_guesses.append(next_guess)
        return next_guess
