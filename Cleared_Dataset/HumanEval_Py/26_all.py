from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    args:
        numbers: list of integers
    
    returns:
        list of integers with all elements that occur more than once removed

    examples:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    >>> remove_duplicates([7, 5, 6, 5, 7, 3])
    [6, 3]
    """
