from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    args:
        numbers: list of integers
    
    returns:
        list of rolling maximum element found until given moment in the sequence

    examples:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([4, 2, 6, 1, 3, 7])
    [4, 4, 6, 6, 6, 7]
    """
