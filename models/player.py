from abc import ABC, abstractmethod

class Player(ABC):  
    def __init__(self, name):
        self.name = name
        self.guesses = []

    @abstractmethod
    def make_guess(self):
        pass