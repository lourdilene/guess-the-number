import pytest
from models.smart_computer_player import SmartComputerPlayer

@pytest.fixture
def smart_computer_player():
    return SmartComputerPlayer("Computer")

def test_make_guess(smart_computer_player, monkeypatch):
    monkeypatch.setattr('random.randint', lambda a, b: 3)

    guess = smart_computer_player.make_guess()
    assert 1 <= guess <= 5

    smart_computer_player.guesses = [1, 2, 3, 4]
    guess = smart_computer_player.make_guess()
    assert 1 <= guess <= 5

    smart_computer_player.guesses = [5]
    guess = smart_computer_player.make_guess()
    assert 1 <= guess <= 5

    smart_computer_player.guesses = [1]
    guess = smart_computer_player.make_guess()
    assert 1 <= guess <= 5

    smart_computer_player.guesses = [3]
    guess = smart_computer_player.make_guess()
    assert 1 <= guess <= 5
