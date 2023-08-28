


def sum_squares(lst) -> int:
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    >>> sum_squares([1, 2, 3])
    6
    >>> sum_squares([])
    0
    >>> sum_squares([-1, -5, 2, -1, -5])
    -126
    """