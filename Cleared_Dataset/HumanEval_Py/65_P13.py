
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    args:
        x: integer to shift
        shift: number of digits to shift
    
    returns:
        string representation of x after circular shift

    examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
