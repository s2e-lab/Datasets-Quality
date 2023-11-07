import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Factorize {
    /**
     * Return list of prime factors of given integer in the order from smallest to largest.
     * Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
     * Input number should be equal to the product of all factors
     * >>> factorize(8)
     * [2, 2, 2]
     * >>> factorize(25)
     * [5, 5]
     * >>> factorize(70)
     * [2, 5, 7]
     * @param n an integer input
     * @return a list where each prime factor of n is listed number of times corresponding to how many times it appears in factorization.
     */
    public static List<Integer> factorize(int n) {
