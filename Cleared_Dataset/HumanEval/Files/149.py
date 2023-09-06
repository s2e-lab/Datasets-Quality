
def sorted_list_sum(lst) -> list:
    """
    Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulting list in a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by the length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.    
    >>> sorted_list_sum(["aa", "a", "aaa"])
    ['aa']
    >>> sorted_list_sum(["ab", "a", "aaa", "cd"])
    ['ab', 'cd']
    """