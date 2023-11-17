from typing import Tuple, List

def largest_smallest_integers(lst: List[int]) -> Tuple[int, int]:
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there are no negative or positive integers, return them as None.

    args:
        lst: list of integers
    
    returns:
        tuple (a, b), where 'a' is the largest of negative integers, and 'b' is
        the smallest of positive integers in a list. If there is no negative or
        positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
