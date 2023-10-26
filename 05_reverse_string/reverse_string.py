def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    list_string = list(str(phrase))
    list_string.reverse()
    print("".join(list_string))
