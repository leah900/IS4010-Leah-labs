# Part 1: The Mad Libs generator
#---------------------------------
def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "The silly cat jumped over the lazy dog and laughed."
    
    >>> generate_mad_lib("brave", "knight", "battled") 
    "Once upon a time, a brave knight battled dragons and saved the kingdom."
    """
    # TODO: Replace this with your creative story implementation
    # Must use f-string formatting and include all three parameters
    return(
        f"In the middle of the night, the {adjective} {noun} {verb} loudly and woke up the entire neighborhood."
    )

# Part 2: The number guessing game 
# ------------------------------

import random

def guessing_game():
    """
    Plays a number guessing game with the user.
    
    This interactive game demonstrates while loops, conditionals, and user input
    handling. The user attempts to guess a randomly generated number between
    1 and 100, receiving feedback after each guess.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    guess = None
    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")


# ------------------------------
# Runner code
# ------------------------------

if __name__ == '__main__':
    guessing_game()
