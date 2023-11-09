import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Common {
    /**
     * Return sorted unique common elements for two lists.
     * >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
     * [1, 5, 653]
     * >>> common([5, 3, 2, 8], [3, 2])
     * [2, 3]
     * @param l1 a list of integers
     * @param l2 a list of integers
     * @return a list of sorted unique common elements of l1 and l2

     *
     */
    public static List<Integer> common(List<Integer> l1, List<Integer> l2) {
