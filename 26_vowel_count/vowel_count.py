def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = set("aeiouAEIOU")

    vowel_counts = {}
    

    for char in phrase:

        if char in vowels and char not in vowel_counts:

            count = phrase.lower().count(char.lower())

            vowel_counts[char.lower()] = count
    
    return vowel_counts