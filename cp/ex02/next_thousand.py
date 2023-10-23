"""Exercise 2.2: Round a number to the next nearest thousand."""
import math

def next_thousand(a:int):
    """Round a number to the next nearest thousand and print.

    :param a: the number to be rounded.
    """
    print( ((a+999)//1000)*1000 )