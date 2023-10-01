import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class TruncateNumber {
    /**
     * Given a positive floating point number, it can be decomposed into
     * and integer part (largest integer smaller than given number) and decimals
     * (leftover part always smaller than 1).

     * Return the decimal part of the number.
     * >>> truncate_number(3.5)
     * 0.5
     * >>> truncate_number(7.4)
     * 0.4
     * @param number a positive floating point number
     * @return the decimal part of the number
     */
    public static Double truncateNumber(Double number) {
