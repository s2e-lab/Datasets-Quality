

def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    >>> decode_shift('fghij')
    'abcde'
    >>> decode_shift('vwxyz')
    'qrstuv'
    """
