
def triangle_area(a, b, c) -> float:
    """
    Given the lengths of the three sides of a triangle. Return to the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise, return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    then the third side.

    >>> triangle_area(3, 4, 5)
    6.0
    >>> triangle_area(1, 2, 10)
    -1
    """
