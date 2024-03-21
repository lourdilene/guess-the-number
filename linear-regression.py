import numpy as np
from sklearn.linear_model import LinearRegression

# Palpites anteriores dos jogadores
human_guesses = np.array([1, 2, 3, 4])
computer_guesses = np.array([56, 49,  6, 31])
possible_guesses = np.array([48,49,50, 55])

# Concatenar os palpites dos dois jogadores em uma única lista
all_guesses = np.concatenate((human_guesses, computer_guesses))

# Remover os palpites repetidos
all_guesses = np.unique(all_guesses)
print(f"all_guesses: {all_guesses}")

# Criar os rótulos para cada palpite (o próximo palpite)
next_guess_label = all_guesses[-1] + 1
print(f"all_guesses[-1] + 1: {all_guesses[-1] + 1}")

# Remover o último palpite, pois não temos um rótulo para ele
all_guesses = all_guesses[:-1]

# Reshape dos dados para o formato esperado pelo modelo
X = human_guesses.reshape(-1, 1)
y = np.roll(computer_guesses, -1).reshape(-1, 1)  # Rótulos deslocados uma posição para frente

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Remover os palpites que já foram feitos da lista de palpites possíveis
#possible_guesses_filtered = np.setdiff1d(possible_guesses, all_guesses)

# Fazer a previsão do próximo palpite apenas com base nos palpites possíveis restantes
print(f"[[next_guess_label]]: {[[next_guess_label]]}")
next_guess = model.predict([[next_guess_label]])
next_guess = int(round(next_guess[0, 0]))

print(f"human_guesses: {human_guesses}")
print(f"computer_guesses: {computer_guesses}")
# print(f"all_guesses: {all_guesses}")
print(f"next_guess: {next_guess}")

# Garantir que o próximo palpite esteja entre os palpites possíveis restantes
next_guess = np.clip(next_guess, possible_guesses[0], possible_guesses[-1])

print("Next guess predicted by linear regression model:", next_guess)