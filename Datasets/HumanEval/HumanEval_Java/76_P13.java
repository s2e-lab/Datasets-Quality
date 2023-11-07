import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class IsSimplePower {
    /**
     * Your task is to write a function that returns true if a number x is a simple
     * power of n and false in other cases.
     * x is a simple power of n if n**int=x
     * For example:
     * is_simple_power(1, 4) => true
     * is_simple_power(2, 2) => true
     * is_simple_power(8, 2) => true
     * is_simple_power(3, 2) => false
     * is_simple_power(3, 1) => false
     * is_simple_power(5, 3) => false
     * @param x an integer
     * @param n an integer
     * @return true if x is a simple power of n, false otherwise.
     */
    public static Boolean isSimplePower(int x, int n) {
