import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class AddElements {
    /**
     * * Given a non-empty array of integers arr and an integer k, return
     * the sum of the elements with at most two digits from the first k elements of arr.

     * Example:

     *     Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
     *     Output: 24 # sum of 21 + 3

     * Constraints:
     *     1. 1 <= len(arr) <= 100
     *     2. 1 <= k <= len(arr)
     * @param arr a non-empty list of integers
     * @param k an input integer
     * @return the sum of the elements with at most two digits from the first k elements of arr
     */
    public static int addElements(List<Integer> arr, int k) {
