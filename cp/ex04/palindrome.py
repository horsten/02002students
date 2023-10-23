"""Exercise 4.3: Checking if a word is a palindrome."""

def is_palindrome(word : str) -> bool:
    """Check if ``word`` is a palindrome.

    :param word: The word to check
    :return: ``True`` if input is a palindrome and otherwise ``False``
    """
    for c in range(len(word)>>1):
        if word[c] != word[len(word)-c-1]:
            return False
    return True

if __name__ == "__main__":
    # here you can try out your functions
    print("Is Madam a palindrome?", is_palindrome('madam'))
    print("Is gentleman a palindrome?", is_palindrome('gentleman'))
