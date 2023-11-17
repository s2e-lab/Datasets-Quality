

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.

    args:
        l: list of integers

    returns:
        True if list elements are monotonically increasing or decreasing, False otherwise

    examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
