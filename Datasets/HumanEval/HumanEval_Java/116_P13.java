import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SortArray {
    /**
     * * In this Kata, you have to sort an array of non-negative integers according to
     * number of ones in their binary representation in ascending order.
     * For similar number of ones, sort based on decimal value.

     * It must be implemented like this:
     * >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
     * >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
     * >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
     * @param arr a list of non-negative integers
     * @return a list sorted in ascending order according to the number of ones in binary representation of each element in arr. 
     *
     */
    public static List<Object> sortArray(List<Object> arr) {
