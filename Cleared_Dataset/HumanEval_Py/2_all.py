

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    args:
        number: positive floating point number
    
    returns:
        decimal part of the number

    examples:

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(9.8)
    0.8
    """
