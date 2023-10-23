"""Exercise 6.8: Spell check."""

def spell_check(text: str, corrections: dict) -> str:
    """Return the corrected text for spelling errors according to a set of rules.

    :param text: The sentence to check for spelling.
    :param corrections: The dictionary of wrongly spelled words and their equivalent corrected version.
    :return: The correctly spelled sentence.
    """
    pos = 0
    output = ''
    while True:
        separator = ''
        while (pos < len(text)) and not text[pos].isalpha():
            separator += text[pos]
            pos = pos + 1
        word = ''
        while (pos < len(text)) and text[pos].isalpha():
            word += text[pos]
            pos = pos + 1
        if word.lower() in corrections.keys():
            corrected = corrections[word.lower()]
            if word.isupper(): # Alle bogstaver i ordet er kapitaler
                word = corrected.upper()
            elif word[0].isupper(): # Første bogstav med stort..
                word = corrected.capitalize()
            else:
                word = corrected
        output += separator + word
        if (pos >= len(text)):
            break
    return output
    # pos = 0
    # word_start = None
    # while pos < len(text):
    #     if text[pos].isAlpha():
    #         if word_start is None:
    #             word_start = pos
    #     elif not word_start is None:
    #         word = text[word_start:pos-1]
    #         if word in corrections.keys():
    # ...                

if __name__ == "__main__":
    # here you can try out your functions
    text = "California State Capitol Museum  -  TEH REVIEW: A beautiful statehouse. Enjoyed teh architecture and historic rooms. Teh gift shop in the basement has limited wheelchair acsess."
    corrections = {
    'apsolute': 'absolute',
    'teh': 'the',
    'acsess': 'access', 
    'occured': 'occurred',
    'exampel': 'example'
    }
    #text = "The apsolute acsess to teh data occured in this exampel."

    print(spell_check(text, corrections))
