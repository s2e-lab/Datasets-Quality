import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class PairsSumToZero {
    /**
     * * pairs_sum_to_zero takes a list of integers as an input.
     * it returns True if there are two distinct elements in the list that
     * sum to zero, and False otherwise.
     * >>> pairs_sum_to_zero([1, 3, 5, 0])
     * False
     * >>> pairs_sum_to_zero([1, 3, -2, 1])
     * False
     * >>> pairs_sum_to_zero([1, 2, 3, 7])
     * False
     * >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
     * True
     * >>> pairs_sum_to_zero([1])
     * False
     * @param l a list of integers
     * @return true if there are two distinct elements in l that
     * sum to zero, false otherwise
     */
    public static Boolean pairsSumToZero(List<Integer> l) {
