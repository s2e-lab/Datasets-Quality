from typing import List

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers numbers, find the minimum sum of any non-empty sub-array
    of numbers.

    args:
        nums: array of integers

    returns:
        minimum sum of any non-empty sub-array of nums

    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
