from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    args:
        a: first string
        b: second string
    
    returns:
        string containing result of binary XOR on a and b

    examples:
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('0010', '1110')
    '1100'
    """
