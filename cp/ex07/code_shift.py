"""Exercise 7.7: Code shift."""

def code_shift(code : tuple, turn : tuple) -> tuple:
    """Return the updated code pattern.

    :param code: Tuple with the initial code in the lock
    :param turn: Tuple with the turn on each lock dial
    :return: Updated lock code.
    """
    return tuple( (a+b) % 10 for a,b in zip(code,turn) )
