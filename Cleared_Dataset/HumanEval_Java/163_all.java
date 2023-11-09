import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class GenerateIntegers {
    /**
     * * Given two positive integers a and b, return the even digits between a
     * and b, in ascending order.

     * For example:
     * generate_integers(2, 8) => [2, 4, 6, 8]
     * generate_integers(8, 2) => [2, 4, 6, 8]
     * generate_integers(10, 14) => []
     * 
     * @param a a positive integer denoting the lower limit
     * @param b a positive integer denoting the upper limit
     * @return the even digits between a and b, in ascending order
     *
     */
    public static List<int> generateIntegers(int a, int b) {
