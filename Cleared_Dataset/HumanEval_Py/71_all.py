
def triangle_area(a: int, b: int, c: int) -> float:
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.

    args:
        a: length of side a
        b: length of side b
        c: length of side c

    returns:
        area of the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
        Otherwise return -1

    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
