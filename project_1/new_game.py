"""Guess the number
The computer makes a guess and guesses the number itself"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: The number of attempts.
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break # exit the loop if you guessed right
    return(count)
print(f"The number of attempts is {random_predict()}")

