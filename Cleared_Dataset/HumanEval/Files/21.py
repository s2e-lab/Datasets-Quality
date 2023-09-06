from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ 
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0])
    [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    """
