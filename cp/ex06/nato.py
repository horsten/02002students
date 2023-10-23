"""Exercise 6.1: The NATO alphabet."""

def text_to_nato(plaintext : str, hamradio : bool = False) -> str:
    """Return the NATO version of a word separated by dashes.

    :param plaintext: The word to replace with its phrase according to the NATO alphabet.
    :return: The NATO representation of the input word.
    """
    nato_alphabet = {
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
        'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliet', 'k': 'Kilo',
        'l': 'Lima', 'm': 'Mike','n': 'November', 'o': 'Oscar', 'p': 'Papa', 'q': 'Quebec',
        'r': 'Romeo', 's': 'Sierra', 't': 'Tango', 'u': 'Uniform', 'v': 'Victor',
        'w': 'Whiskey', 'x': 'Xray', 'y': 'Yankee', 'z': 'Zulu',
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Niner'
    }
    if hamradio:
        nato_alphabet.update({'r': 'Radio'})
    output = []
    for c in plaintext:
        if c.lower() in nato_alphabet.keys():
            output.append(nato_alphabet[c.lower()])
        else:
            output += c
    return '-'.join(output)

if __name__ == "__main__":
    testcases = ['Hello','M0TRN',('M0TRN',True),'warzone','AF7BE','OZ5TN']
    for t in testcases:
        if (type(t) is tuple):
            print(f"text_to_nato('{t[0]}', {t[1]}): {text_to_nato(t[0],t[1])}")
        else:
            print(f"text_to_nato('{t[0]}'): {text_to_nato(t)}")
