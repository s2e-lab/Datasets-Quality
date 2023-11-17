from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    args:
        numbers: list of numbers
        delimeter: number to insert between every two consecutive elements of `numbers'
    
    returns:
        list of numbers with delimeter inserted between every two consecutive elements of input list `numbers'
    
    examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
