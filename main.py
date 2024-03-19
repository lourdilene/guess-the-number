# from models.game import Game

# def main():
#     game = Game()
#     game.play()

# if __name__ == "__main__":
#     main()

import numpy as np
from sklearn.linear_model import LinearRegression

# Palpites anteriores dos jogadores
human_guesses = np.array([20, 30, 40, 45, 46, 47, 60, 90])
computer_guesses = np.array([25, 32, 35, 37, 38, 33, 66, 99])
possible_guesses = np.array([48,49,50])

# Concatenar os palpites dos dois jogadores em uma única lista
all_guesses = np.concatenate((human_guesses, computer_guesses))

# Remover os palpites repetidos
all_guesses = np.unique(all_guesses)

# Criar os rótulos para cada palpite (o próximo palpite)
next_guess_label = all_guesses[-1] + 1

# Remover o último palpite, pois não temos um rótulo para ele
all_guesses = all_guesses[:-1]

# Reshape dos dados para o formato esperado pelo modelo
X = human_guesses.reshape(-1, 1)
y = np.roll(computer_guesses, -1).reshape(-1, 1)  # Rótulos deslocados uma posição para frente

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Remover os palpites que já foram feitos da lista de palpites possíveis
possible_guesses_filtered = np.setdiff1d(possible_guesses, all_guesses)

# Fazer a previsão do próximo palpite apenas com base nos palpites possíveis restantes
next_guess = model.predict([[next_guess_label]])
next_guess = int(round(next_guess[0, 0]))

# Garantir que o próximo palpite esteja entre os palpites possíveis restantes
next_guess = np.clip(next_guess, possible_guesses_filtered[0], possible_guesses_filtered[-1])

print("Next guess predicted by linear regression model:", next_guess)


