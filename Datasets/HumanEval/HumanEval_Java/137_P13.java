import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class CompareOne {
    /**
     * * Create a function that takes integers, floats, or strings representing
     * real numbers, and returns the larger variable in its given variable type.
     * Return null if the values are equal.
     * Note: If a real number is represented as a string, the floating point might be . or ,

     * compare_one(1, 2.5) ➞ 2.5
     * compare_one(1, "2,3") ➞ "2,3"
     * compare_one("5,1", "6") ➞ "6"
     * compare_one("1", 1) ➞ None
     * @param a an integer, float or string representing a real number
     * @param b an integer, float or string representing a real number
     * @return the larger one among a and b in its given variable type, return null if a and b are equal.
     */
    public static Object compareOne(Object a, Object b) {
