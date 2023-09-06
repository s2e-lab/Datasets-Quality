from typing import List

def all_prefixes(string: str) -> List[str]:
    """ 
    Return a list of all prefixes from shortest to longest of the input string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    >>> all_prefixes('abcd')
    ['a', 'ab', 'abc', 'abcd']
    """
