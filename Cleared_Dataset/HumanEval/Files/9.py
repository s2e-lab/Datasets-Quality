from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2, 3])
    [1, 2, 3, 3, 3, 4, 4, 4]
    """
