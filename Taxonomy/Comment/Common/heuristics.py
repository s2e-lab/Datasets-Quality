

def heuristic_1(comment):
    """
    Heuristic 1: Check if the comment contains a question mark
    """
    if '?' in comment:
        return True
    return False