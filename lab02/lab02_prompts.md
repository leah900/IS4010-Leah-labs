### Problem 1: debugging
The prompt I used to ask an AI to debug the code was: 
Persona: Act as a senior Python developer who is skilled at debugging and explaining logical mistakes.
Task: Please identify the function's bug also explain the occurrence reason and provide the code's corrected version.
Format: show explanation then corrected code in code block.

The final, corrected code that AI provided was:
```python
def sum_of_evens(numbers):
    """Calculates the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        if num % 2 == 0:  
         total += num
    return total
```
### Problem 2: Refactoring an unreadable function
The prompt I used to ask AI to refactor the code was:
Persona: You are senior Python developer who improves code readability and style.
Task: Refactor the code to make it clear and pythonic.
Format: Provide the improved version of the code in a code block. 

```python 
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users who are 18 or older."""
    return [user['name'] for user in users if user['age'] >= 18]
```
### Problem 3: Documenting a function
The prompt I used to ask AI to document the code was: "I have a Python function that calculates the area of a rectangle. The function works correctly but has no documentation."
Task: Write a high-quality NumPy-style docstring for this function, including parameters, returns, and raises sections.
Persona: Act as a senior Python developer who follows professional documentation standards.
Format: Return the function with the NumPy-style docstring included.
The code that AI provided is:
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The area of the rectangle (length * width).

    Raises
    ------
    ValueError
        If `length` or `width` is less than or equal to 0.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width


