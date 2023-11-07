import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class RoundedAvg {
    /**
     * You are given two positive integers n and m, and your task is to compute the
     * average of the integers from n through m (including n and m). 
     * Round the answer to the nearest integer and convert that to binary.
     * If n is greater than m, return -1.
     * Example:
     * rounded_avg(1, 5) => "0b11"
     * rounded_avg(7, 5) => -1
     * rounded_avg(10, 20) => "0b1111"
     * rounded_avg(20, 33) => "0b11010"
     * @param n a positive integer
     * @param m a positive integer
     * @return the binary representation of the average of the integers from n through m after rounding to the nearest integer
     *
     */
    public static String roundedAvg(int n, int m) {
