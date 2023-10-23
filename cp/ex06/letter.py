"""Exercise 6.2: Letter histogram."""

def letter_histogram(input_string : str) -> dict:
    """Return the histogram of letter occurrences.
    
    :param input_string: The word based on which the letter histogram is calculated.
    :return: The alphabet characters as keys with their corresponding occurrences as values.
    """
    histogram = {}
    for c in range(ord('a'),ord('z')+1):
        histogram.update({chr(c): 0})
    for c in input_string.lower():
        if c in histogram.keys():
            histogram[c] += 1
    return histogram

if __name__ == "__main__":
    # here you can try out your functions
    print("What is the letter histogram of the word banana?",  letter_histogram('banana'))
