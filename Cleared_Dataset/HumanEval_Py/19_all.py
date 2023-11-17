from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    args:
        numbers: space-delimited string of numberals from 'zero' to 'nine'
    
    returns:
        string with numbers sorted from smallest to largest

    examples:
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('seven two nine')
    'two seven nine'
    """
