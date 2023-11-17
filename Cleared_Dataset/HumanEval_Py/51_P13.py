

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.

    args:
        text: string to remove vowels from

    returns:
        string without vowels

    examples:
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
