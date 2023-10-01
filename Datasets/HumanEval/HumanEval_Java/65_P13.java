import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class CircularShift {
    /**
     * Circular shift the digits of the integer x, shift the digits right by shift
     * and return the result as a string.
     * If shift > number of digits, return digits reversed.
     * >>> circular_shift(12, 1)
     * "21"
     * >>> circular_shift(12, 2)
     * "12"
     * @param x an input integer
     * @param shift an input integer 
     * @return a string formed by shifting the digits of x right by shift
     *
     */
    public static String circularShift(int x, int shift) {
