import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SpecialFactorial {
    /**
     * The Brazilian factorial is defined as:
     * brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
     * where n > 0

     * For example:
     * >>> special_factorial(4)
     * 288
     * >>> special_factorial(5)
     * 34560

     * The function will receive an integer as input and should return the special
     * factorial of this integer.
     *
     */
    public static long specialFactorial(int n) {
