
def get_row(lst, x) -> list:
    """
    You are given 2-dimensional data as nested lists,
    which is similar to a matrix; however, unlike matrices,
    each row may contain a different number of columns.
    Given lst and integer x, find integers x in the list,
    and return a list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort the coordinates of the row by columns in descending order.

    >>> get_row([
    ...   [1,2,3,4,5,6],
    ...   [1,2,3,4,1,6],
    ...   [1,2,3,4,5,1]
    ... ], 1)
    [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    >>> get_row([], 1)
    []
    >>> get_row([[], [1], [1, 2, 3]], 3)
    [(2, 2)]
    """