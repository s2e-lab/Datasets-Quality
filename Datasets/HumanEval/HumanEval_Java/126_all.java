import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class IsSorted {
    /**
     * * Given a list of numbers, return whether or not they are sorted
     * in ascending order. If list has more than 1 duplicate of the same
     * number, return False. Assume no negative numbers and only integers.

     * Examples
     * is_sorted([5]) ➞ True
     * is_sorted([1, 2, 3, 4, 5]) ➞ True
     * is_sorted([1, 3, 2, 4, 5]) ➞ False
     * is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
     * is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
     * is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
     * is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
     * is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
     * 
     * @param lst a list of integers
     * @return true if lst is sorted in ascending order, false if lst is not sorted or 
     * list has more than 1 duplicate of the same number
     *
     */
    public static Boolean isSorted(List<Integer> lst) {
