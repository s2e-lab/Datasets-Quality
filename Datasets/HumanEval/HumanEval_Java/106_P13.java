import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class F {
    /**
     * Implement the function f that takes n as a parameter,
     * and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
     * or the sum of numbers from 1 to i otherwise.
     * i starts from 1.
     * the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
     * Example:
     * f(5) == [1, 2, 6, 24, 15]
     * 
     * @param n an input integer
     * @return a list of size n, such that the value of the element at index i is the factorial of i if i is even or the sum of numbers from 1 to i otherwise.
     *  
     */
    public static List<Integer> f(int n) {
