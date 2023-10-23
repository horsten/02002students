"""Exercise: Convert length in foot and inch to centimeter."""
import math

def unit_conversion(foot:int, inch:int):
    """Convert length in foot and inch to centimeter.

    :param foot: foot portion of the length in imperical unit.
    :param inch: inch portion of the length in imperical unit.
    """
    cm = round(2.54*(12*foot+inch))
    print("%d ft %d in is equal to %d cm." % (foot, inch, cm))