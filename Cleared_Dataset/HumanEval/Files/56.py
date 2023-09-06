
def correct_bracketing(brackets: str) -> bool:
    """ 
    Brackets are a string of "<" and ">."
    Return True if every opening bracket has a corresponding closing bracket.
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
