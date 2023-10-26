def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    list_word = list(phrase)
    phrase_dict = {}
    for letter in list_word:
        phrase_dict[letter] = list_word.count(letter)

    print(phrase_dict)
