
def pluck(arr) -> list:
    """
    Given an array representing a branch of a tree that has non-negative integer nodes.
    Your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.
    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].
    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    >>> pluck([4,2,3])
    [2, 1]
    >>> pluck([1,2,3])
    [2, 1]
    >>> pluck([])
    []
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    """
