import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SortThird {
    /**
     * This function takes a list l and returns a list l' such that
     * l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
     * to the values of the corresponding indices of l, but sorted.
     * >>> sort_third([1, 2, 3])
     * [1, 2, 3]
     * >>> sort_third([5, 6, 3, 4, 8, 9, 2])
     * [2, 6, 3, 4, 8, 9, 5]
     *
     */
    public static List<Integer> sortThird(List<Integer> l) {
