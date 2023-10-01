import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Monotonic {
    /**
     * Return True if list elements are monotonically increasing or decreasing.
     * >>> monotonic([1, 2, 4, 20])
     * True
     * >>> monotonic([1, 20, 4, 10])
     * False
     * >>> monotonic([4, 1, 0, -10])
     * True
     * @param l a list of integers
     * @return true if list elements monotonically increasing or decreasing, false otherwise.
     *
     */
    public static Boolean monotonic(List<Integer> l) {
