from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.


    args:
        paren_string: string containing multiple groups of nested parentheses
    
    returns:
        list of strings containing separate groups of nested parentheses

    examples:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    >>> separate_paren_groups('(( )) ((( ))) (( ))')
    ['(())', '((()))', '(())']
    """