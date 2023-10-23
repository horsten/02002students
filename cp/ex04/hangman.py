"""Exercise 4.12-4.16."""

def is_word_guessed(secret_word : str, letters_guessed : str) -> bool:
    """Determine if the word has been guessed.

    :param secret_word: The word to guess
    :param letters_guessed: A ``str`` containing the letters that have currently been guessed
    :return: True if and only if all letters in ``secret_word`` have been guessed.
    """
    return 0 == sum((letters_guessed.find(c) == -1) for c in secret_word)

def get_available_letters(letters_guessed : str) -> str:
    """
    Return the letters which are available, i.e. have not been guessed so far.

    The input string represents the letters the user have guessed, and the output should then be the lower-case
    letters which are not contained in that string. The function is used to show the user which
    letters are available in each round.

    :param letters_guessed: A `str` representing the letters the user has already guessed
    :return: A `str` containing the letters the user has not guessed at yet.
    """
    #r = ''
    #for c in iter('abcdefghijklmnopqrstuvwxyz'):
    #    if letters_guessed.find(c) == -1:
    #        r += c
    #return r
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for c in iter(letters_guessed):
        letters = letters.replace(c, '')
    return letters

def get_guessed_word(secret_word : str, letters_guessed : str) -> str:
    """Format the secret word for the user by removing letters that have not been guessed yet.

    Given a list of the available letters, the function will replace the letters in the secret word with `'_ '`
    (i.e., a lower-case followed by a space). For instance, if the secret word is ``"cat"``, and the
    available letters are ``"ct"``, then the function should return ``"c_ t"``.

    :param secret_word: A ``str``, the word the user is guessing
    :param letters_guessed:  A ``str`` containing which letters have been guessed so far
    :return: A ``str``, comprised of letters, underscores (_), and spaces that represents which letters in secret_word have been guessed so far.
    """
    n = []
    for c in secret_word:
        if letters_guessed.find(c) != -1:
            n.append(c)
        else:
            n.append('_ ')
    return ''.join(n)

def hangman(secret_word : str, guesses : int):
    """
    Play an interactive game of Hangman.

    This function should launch an interactive game of Hangman. The details of the game is defined in the
    project description available online, and should be read carefully.

    * The game should first display how many letters are in the secret word. You should start by generating this output.
    * Before each round, the user should see how many guesses that are left and which letters are not yet used
    * In each round, the user is prompted to input a letter. Use the ``input('..')`` function for this.
    * The user is given feedback based on whether the letter is in the word or not. The program also performs error handling.
    * The game terminates when the user win, has exceeded the number of guesses, or if the user makes an illegal input.
      in this case the user is shown a score.

    :param secret_word: The secret word to guess, for instance ``"cow"``
    :param guesses: The number of available guesses, for instance ``6``
    """
    print(f'Hangman! To save Bob, you must guess a 3 letter word within {guesses} attempts.')
    letters_guessed = ''
    guesses1 = guesses
    while guesses > 0 and not is_word_guessed(secret_word,letters_guessed):
        print(f"----\nYou have {guesses} guesses left.")
        print(f"The available letters are: {get_available_letters(letters_guessed)}. Guess a letter and press enter: ",end="")
        i = input('')

        if len(i) != 1 or i < 'a' or i > 'z':
            break
            #print("Invalid input dumbo, try again!")
            #continue

        letters_guessed += i

        if is_word_guessed(secret_word,letters_guessed):
            print(f"Success! You guessed '{secret_word}' in {guesses1-guesses} tries.")
            print(f"Your score is {len(secret_word)*(guesses+1)}")
            return

        if secret_word.find(i)!=-1:
            msg = "Good guess"
        else:
            msg = "Oh no"

        print(f'{msg}: {get_guessed_word(secret_word, letters_guessed)}')

        guesses -= 1

    print(f"Game over :-(. Your score is 0 points.")

if __name__ == "__main__":
    # here you can try out your functions
    #print("This should return True: ", is_word_guessed("dog", "tdohg"))
    #print("This should return False: ", is_word_guessed("dog", "dthk"))

    #print("This should be 'c_ w': ", get_guessed_word('cow', 'kcwt'))

    #print("Available letters when we have tried 'abcdefghijk'; this should be about half the alphabet: ", get_available_letters('abcdefghijk'))

    #print("Lets launch hangman. Try the inputs in the exercise description and see if you get the same")
    hangman("cow", 4)
