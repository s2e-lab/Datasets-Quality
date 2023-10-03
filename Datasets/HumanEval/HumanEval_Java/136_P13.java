import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class LargestSmallestIntegers {
    /**
     * * Create a function that returns a tuple (a, b), where 'a' is
     * the largest of negative integers, and 'b' is the smallest
     * of positive integers in a list.
     * If there is no negative or positive integers, return them as None.

     * Examples:
     * largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
     * largest_smallest_integers([]) == (None, None)
     * largest_smallest_integers([0]) == (None, None)
     * @param lst a list of integers
     * @return a list [a, b], where 'a' is the largest of negative integers, and 'b' is the smallest
     * of positive integers in lst. If there is no negative or positive integers, return them as None.
     * 
     */
    public static List<Integer> largestSmallestIntegers(List<Object> lst) {
