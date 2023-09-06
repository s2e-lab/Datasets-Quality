
def strange_sort_list(lst) -> list:
    """
    Given a list of integers, return the list in strange order.
    Strange sorting is when you start with the minimum value,
    then a maximum of the remaining integers, then the minimum, and so on.
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """