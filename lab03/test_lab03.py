# test_lab03.py
import pytest
from lab03.lab03 import guessing_game

def test_guessing_game_fixed_number():
    # Test with a fixed secret number
    attempts = guessing_game(secret=42)
    assert attempts == 1

def test_guessing_game_random_number():
    # Should always return at least 1 attempt
    attempts = guessing_game(secret=5)
    assert attempts >= 1
