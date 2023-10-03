import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class MakeAPile {
    /**
     * * Given a positive integer n, you have to make a pile of n levels of stones.
     * The first level has n stones.
     * The number of stones in the next level is:
     *     - the next odd number if n is odd.
     *     - the next even number if n is even.
     * Return the number of stones in each level in a list, where element at index
     * i represents the number of stones in the level (i+1).

     * Examples:
     * >>> make_a_pile(3)
     * [3, 5, 7]
     * >>> make_a_pile(4)
     * [4, 6, 8, 10]
     * @param n a positive integer denoting number of levels of stone in a pile
     * @return the number of stones in each level as a list, where element at index i represents the number of stones in the level (i+1).
     */
    public static List<Integer> makeAPile(int n) {
