"""Exercise 7.5: Box packing."""

def box_packing(object : tuple, box : tuple)-> tuple:
    """Return the amount of object sticking in each dimension, or zero if sufficient space.
    
    :param object: Tuple (h,w) the dimensions of the object
    :param box: Tuple (H, W) the dimensions of the box.
    :return: Tuple
    """
    return tuple([0 if o<=b else o-b for (o,b) in zip(object,box)])
