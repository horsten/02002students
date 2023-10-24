"""Exercise 7.8: Morse code."""

morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'
}
                                
def morse_to_text(morse_code : str) -> str:
    """Return the extracted message from its Morse code.

    :param morse_code: String with the initial message encoded in Morse. 
    :return: The decoded message.
    """
    output_words = []
    for word in morse_code.split('  '):
        output_word = ''
        for letter in word.split(' '):
            output_word+=morse_code_dict[letter] if letter in morse_code_dict else '#'
        output_words.append(output_word)
    return ' '.join(output_words)

if __name__ == '__main__':
    testcases = [
        ("-.. --- - ...  .- -. -..  -.. .- ... .... . ...  - . .-.. .-..  .- -. -.-. .. . -. -  - .- .-.. . ...", "DOTS AND DASHES TELL ANCIENT TALES"),
        ("..  --. ---  - ---  - .... .  -.. . -. - .. ... -", "I GO TO THE DENTIST"),
        ("- --- -.. .- -.--  .-- .- ...  -.-. .-.. . .- .-.", "TODAY WAS CLEAR"),
        ("- .... .  -- .- --. .. -.-.  --- ..-.  - .... .  ... ..- -.", "THE MAGIC OF THE SUN"),
        ("- .... .  .--- --- -.--  .. -.  -- -.--  .... . .- .-. -", "THE JOY IN MY HEART")
    ]
    for (code,expected) in testcases:
        print(f'Code: {code}\nExpected: {expected} - Got: {morse_to_text(code)}\n----\n')
