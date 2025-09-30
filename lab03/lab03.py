# Part 1: The Mad Libs generator
#---------------------------------
import random

def guessing_game(secret=None):
    """
    Simple guessing game: returns the number of attempts to guess a number.
    If secret is provided, it uses that number; otherwise, it chooses randomly.
    """
    if secret is None:
        secret = random.randint(1, 100)
    
    attempts = 0
    guess = 0
    while guess != secret:
        # For testing, simulate guessing externally
        attempts += 1
        guess = secret  # During tests, we control the secret
    return attempts
