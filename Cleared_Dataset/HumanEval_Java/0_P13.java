import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class HasCloseElements {
    /**
     * Check if in given list of numbers, are any two numbers closer to each other than
     * given threshold.
     * >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
     * False
     * >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
     * True
     * @param numbers a list of numbers
     * @param threshold the given threshold value
     * @return true if any two numbers are closer than threshold, otherwise false
     */
    public static Boolean hasCloseElements(List<Double> numbers, Double threshold) {
