import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class TriangleArea {
    /**
     * * Given the lengths of the three sides of a triangle. Return the area of
     * the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
     * Otherwise return -1
     * Three sides make a valid triangle when the sum of any two sides is greater 
     * than the third side.
     * Example:
     * triangle_area(3, 4, 5) == 6.00
     * triangle_area(1, 2, 10) == -1
     * @param a the length of a side of a triangle
     * @param b the length of a side of a triangle
     * @param c the length of a side of a triangle
     * @return the area of the triangle
     */
    public static Number triangleArea(int a, int b, int c) {
