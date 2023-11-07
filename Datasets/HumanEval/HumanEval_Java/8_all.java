import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SumProduct {
    /**
     * For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
     * Empty sum should be equal to 0 and empty product should be equal to 1.
     * >>> sum_product([])
     * (0, 1)
     * >>> sum_product([1, 2, 3, 4])
     * (10, 24)
     * @param numbers a list of integers
     * @return a tuple consisting of a sum and a product of all the integers in the input list.
     */
    public static List<Integer> sumProduct(List<Integer> numbers) {
