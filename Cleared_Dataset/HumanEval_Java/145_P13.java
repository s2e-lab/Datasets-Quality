import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class OrderByPoints {
    /**
     * * Write a function which sorts the given list of integers
     * in ascending order according to the sum of their digits.
     * Note: if there are several items with similar sum of their digits,
     * order them based on their index in original list.

     * For example:
     * >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
     * >>> order_by_points([]) == []
     * @param nums a list of integers
     * @return a list after sorting the entries of nums in ascending order according to the sum of their digits
     */
    public static List<Object> orderByPoints(List<Object> nums) {
