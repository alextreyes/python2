def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('Noon')
        True

        >>> is_palindrome('Noon')
        True
    """
    trimed_phrase = phrase.replace(" ", "")
    upper_phrase = trimed_phrase.upper()

    list_phrase = list(trimed_phrase)
    list_phrase.reverse()

    reversed_phrase_done = "".join(list_phrase).upper()

    print(upper_phrase, reversed_phrase_done)
    if upper_phrase == reversed_phrase_done:
        return True
    else:
        return False
