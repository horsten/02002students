"""Exercise 2.5: Calculate the normal weight range for a given height."""
import math

def normal_weight(height:float):
    """Calculate and print the range of normal weights for a given height.

    :param height: the height.
    """
    wlo = 18.5 * pow(height,2)
    whi = 25 * pow(height, 2)
    print("Normal weight is between %d and %d kg." % (math.ceil(wlo), math.floor(whi)))