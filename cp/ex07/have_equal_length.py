"""Exercise 7.1: Have equal length."""

def have_equal_length(a : tuple, b : tuple) -> bool:
    """Check whether two tuples have equal length.

    :param a: Tuple.
    :param b: Tuple.
    :return: A boolean value.
    """
    return len(a)==len(b)