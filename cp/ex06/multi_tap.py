"""Exercise 6.9: Multi-tap."""

keypad_dict = {0: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']}

def multi_tap(keys : list, times : list) -> str:
    """Return the string corresponding to the multi-tap key presses.

    :param keys: The list of keys pressed.
    :param times: The list of times of when the keys were pressed.
    :return: The string corresponding to the key presses.
    """
    state = {   'last_key': None,
                'last_key_count': 0,
                'last_time': 0,
                'output': ''
            }
    def keypress(key: chr, time: float):
        if time is None or key != state['last_key'] or time > state['last_time'] + .5:
            if not state['last_key'] is None:
                state['output'] += keypad_dict[state['last_key']][(state['last_key_count']-1)%len(keypad_dict[state['last_key']])]
            state['last_key'] = key
            state['last_key_count'] = 1
        else:
            state['last_key_count'] += 1
        state['last_time'] = time
        return

    while len(keys) > 0:
        keypress(keys.pop(0), times.pop(0))
    keypress(None, None) # Flush output
    return state['output']

if __name__ == "__main__":
    # Tests
    keys = [7, 7, 7, 7, 6, 6, 6]
    times = [0, 0.7, 0.8, 0.9, 1, 1.1, 1.2]
    print(multi_tap(keys, times), '==', 'PRO')
    keys = [7, 7, 7, 7, 6, 6, 6, 4, 7, 7, 7, 2, 6]
    times = [0.4, 1.5, 1.8, 2.0, 2.2, 2.6, 2.9, 3.0, 3.3, 3.6, 3.9, 4.2, 4.3]
    print(multi_tap(keys, times), '==', 'PROGRAM')

    print(multi_tap([5, 5, 5, 4, 4, 4, 8, 8, 8, 3, 3, 0, 5, 5, 5, 2, 8, 8, 4, 4, 4, 0, 5, 5, 5, 4, 4, 4, 7, 7, 
7, 7, 8], [0.7, 0.9, 1.2, 1.6, 1.7, 2.0, 2.4, 2.5, 2.8, 3.2, 3.5, 3.7, 3.9, 4.3, 4.6, 4.8, 5.0, 5.3, 5.6, 6.3, 6.7, 6.8, 7.1, 7.3, 7.5, 7.8, 8.0, 8.1, 8.3, 8.5, 8.7, 8.9, 9.3]))