

def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    args:
        s0: string
        s1: string

    returns:
        True if s0 and s1 have the same characters, False otherwise.

    examples:
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
