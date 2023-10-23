"""Exercise 3.7: Solar panel."""

def solar_panel(move : bool, swap : bool, hot : bool, empty : bool) -> str:
    """Print out whether it is a good idea to install solar panels on an object with the given properties.

    :param move: does the object move around?
    :param swap: does the object allow swapping or recharging battery?
    :param hot: is the object hot to the touch when it is running?
    :param empty: are there other empty places near the object?
    :return: Whether you should put solar panels on the object as a string.
    """
    
    decision_tree = (move, (swap, 'probably not', (hot, 'haha good luck', 'maybe')), (empty, 'probably not', 'sure'))
    traverse=lambda node: node if isinstance(node, str) else traverse(node[1 if node[0] else 2])
    return traverse(decision_tree)
