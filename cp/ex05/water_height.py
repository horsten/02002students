"""Exercise 5.10. Water height."""

def water_height(h0: int, r: list) -> int:
    """Calculate the water height after multiple days of rain.

    :param: h0: initial height of the water
    :param: r: list of rain showers
    :return: height of water after days of rain 
    """
    for rain in r:
        h0 += rain - 2
        if (h0 < 0):
            h0 = 0
    return h0

if __name__ == "__main__":
    testcases = [ 'water_height(0, [1])', 'water_height(0, [4, 2, 3])', 'water_height(5, [1, 0, 2, 1])' ]
    for t in testcases:
        print(f'{t}: {eval(t)}')
