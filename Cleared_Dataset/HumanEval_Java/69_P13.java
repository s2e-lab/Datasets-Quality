import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Search {
    /**
     * * You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
     * zero, and has a frequency greater than or equal to the value of the integer itself. 
     * The frequency of an integer is the number of times it appears in the list.
     * If no such a value exist, return -1.
     * Examples:
     *     search([4, 1, 2, 2, 3, 1]) == 2
     *     search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
     *     search([5, 5, 4, 4, 4]) == -1
     * @param lst a non-empty list of positive integers
     * @return the greatest integer in lst that is greater than 
     * zero, and has a frequency greater than or equal to the value of the integer itself
     *
     */
    public static int search(List<Integer> lst) {
