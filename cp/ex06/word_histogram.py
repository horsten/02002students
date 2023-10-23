"""Exercise 6.3-6.4."""

def word_histogram(lines : list) -> dict:
    """Return the word count histogram from the input lines.

    :param lines: The lines that are analyzed for word count.
    :return: The histogram of word occurrences.
    """
    return (_:={},[_.update({w: 1+(w in _ and _[w])}) for w in [w.lower().strip(',.:?!') for w in ' '.join(lines).split()]])[0]
    #return (_:={},[w=='' or _.update({w: 1+(w in _ and _[w])}) for w in [w.lower().strip(',.:?!') for w in ' '.join(lines).split(' ')]])[0]

def extract_keyword(lines : str, ignore_list : list, max : int = 5) -> dict:
    """Return the most frequent words that are not on the ignore list and their occurrences.

    :param lines: The sentence to extract keywords from.
    :param ignore_list: The words that should ignored.
    :param max: The number of words to return.
    :return: The most frequent words in the sentence as keys with their count as values.
    """
    return dict(filter(lambda k,n=[max+1]: k[0] not in ignore_list and (n.append(c:=n.pop(0)-1) or c>0), sorted(word_histogram(lines).items(), key=lambda k:k[1], reverse=1)))

# https://chat.openai.com/share/478d639b-7ac9-46b0-b222-872d16360faa

if __name__ == "__main__":
    # here you can try out your functions
    lines = ['This is the first sentence of text for you', 'This is the second sentence of text', 'This is for you']
    print("word_histogram")
    print(word_histogram(lines))

    # Ignore list of common words
    ignore_list = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'is', 'have', 'I']

    # Print the 5 most occurring keywords
    print("extract_keywords")
    print(extract_keyword(lines, ignore_list))
    print(extract_keyword(lines, []))

    ignore_list2 = ['a', 'an', 'the', 'above', 'across', 'against', 'along', 'among', 'around',    'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'by',    'down', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'to', 'toward',    'under', 'upon', 'with', 'within','function', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so']
    lines2 = ["Words are flowing out like endless rain into a paper cup. They slither wildly as they slip away across the universe. Pools of sorrow, waves of joy are drifting through my opened mind. Possessing and caressing me. Images of broken light which dance before me like a million eyes. They call me on and on across the universe. Thoughts meander like a restless wind inside a letterbox they. They tumble blindly as they make their way across the universe. Jai guru deva, om. Sounds of laughter shades of life are ringing. Through my open ears inciting and inviting meLimitless undying love which shines around me like a million suns. It calls me on and on across the universe"]
    print(extract_keyword(lines2, ignore_list2))


    
    print(word_histogram(["Write the function word histogram."," which takes as argument a list containing lines of a text."]))
    print({'write': 1, 'the': 1, 'function': 1, 'word': 1, 'histogram': 1, 'which': 1, 'takes': 1, 'as': 1, 'argument': 1, 'a': 2, 'list': 1, 'containing': 1, 'lines': 1, 'of': 1, 'text': 1})