import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class TriplesSumToZero {
    /**
     * * triples_sum_to_zero takes a list of integers as an input.
     * it returns True if there are three distinct elements in the list that
     * sum to zero, and False otherwise.

     * >>> triples_sum_to_zero([1, 3, 5, 0])
     * False
     * >>> triples_sum_to_zero([1, 3, -2, 1])
     * True
     * >>> triples_sum_to_zero([1, 2, 3, 7])
     * False
     * >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
     * True
     * >>> triples_sum_to_zero([1])
     * False
     * @param l a list of integers
     * @return true if there are three distinct elements in l that sum to zero, false otherwise.
     *
     *
     */
    public static Boolean triplesSumToZero(List<Integer> l) {
