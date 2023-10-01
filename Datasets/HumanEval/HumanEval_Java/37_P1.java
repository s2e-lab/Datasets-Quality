import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SortEven {
    /**
     * This function takes a list l and returns a list l' such that
     * l' is identical to l in the odd indices, while its values at the even indices are equal
     * to the values of the even indices of l, but sorted.
     * >>> sort_even([1, 2, 3])
     * [1, 2, 3]
     * >>> sort_even([5, 6, 3, 4])
     * [3, 6, 5, 4]
     *
     */
    public static List<Integer> sortEven(List<Integer> l) {
