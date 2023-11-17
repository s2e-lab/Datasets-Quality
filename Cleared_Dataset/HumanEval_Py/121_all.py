from typing import List

def sum_odd_evenpos(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    args:
        lst: list of integers

    returns:
        sum of all of the odd elements that are in even positions

    Examples:
    sum_odd_evenpos([5, 8, 7, 1]) ==> 12
    sum_odd_evenpos([3, 3, 3, 3, 3]) ==> 9
    sum_odd_evenpos([30, 13, 24, 321]) ==>0
    """
