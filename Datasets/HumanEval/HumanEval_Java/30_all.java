import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class GetPositive {
    /**
     * Return only positive numbers in the list.
     * >>> get_positive([-1, 2, -4, 5, 6])
     * [2, 5, 6]
     * >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
     * [5, 3, 2, 3, 9, 123, 1]
     * @param l a list of integers
     * @return a list containing only positive numbers from the input list
     *
     */
    public static List<Integer> getPositive(List<Integer> l) {
