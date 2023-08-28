
def maximum(arr, k) -> list:
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)

    >>> maximum([-3, -4, 5], 3)
    [-4, -3, 5]
    >>> maximum([4, -4, 4], 2)
    [4, 4]
    >>> maximum([-3, 2, 1, 2, -1, -2, 1], 1)
    [2]
    """