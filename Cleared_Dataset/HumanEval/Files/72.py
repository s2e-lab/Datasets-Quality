
def will_it_fly(q,w) -> bool:
    """
    Write a function that returns True if the object q will fly and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal to the maximum possible weight w.

    >>> will_it_fly([1, 2], 5)
    False
    >>> will_it_fly([3, 2, 3], 1)
    False
    >>> will_it_fly([3, 2, 3], 9)
    True
    >>> will_it_fly([3], 5)
    True
    """
