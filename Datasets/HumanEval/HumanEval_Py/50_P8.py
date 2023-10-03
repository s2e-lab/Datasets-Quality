

def encode_shift(s: str) -> str:
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    >>> encode_shift('abcde')
    fghij
    >>> encode_shift('fghi')
    klmn
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str) -> str:
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    >>> decode_shift('ildoz')
    dgyju
    >>> decode_shift('ikym')
    dfth
    """
