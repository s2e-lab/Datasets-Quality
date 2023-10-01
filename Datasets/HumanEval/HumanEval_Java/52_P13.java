import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class BelowThreshold {
    /**
     * Return True if all numbers in the list l are below threshold t.
     * >>> below_threshold([1, 2, 4, 10], 100)
     * True
     * >>> below_threshold([1, 20, 4, 10], 5)
     * False
     * @param l a list of integers
     * @param t the threshold value
     * @return true if all numbers in l are below t, false otherwise
     *
     */
    public static Boolean belowThreshold(List<Integer> l, int t) {
