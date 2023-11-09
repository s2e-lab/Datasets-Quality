import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Solve {
    /**
     * Given a positive integer N, return the total sum of its digits in binary.
     * 
     * Example
     *     For N = 1000, the sum of digits will be 1 the output should be "1".
     *     For N = 150, the sum of digits will be 6 the output should be "110".
     *     For N = 147, the sum of digits will be 12 the output should be "1100".
     * 
     * Variables:
     *     @N integer
     *          Constraints: 0 ≤ N ≤ 10000.
     * Output:
     *      a string of binary number
     * 
     * @param n a positive integer
     * @return the total sum of n's digits in binary as a string
     *
     */
    public static String solve(int n) {
