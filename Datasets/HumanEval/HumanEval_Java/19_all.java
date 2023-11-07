import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SortNumbers {
    /**
     * Input is a space-delimited string of numbers from 'zero' to 'nine'.
     * Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
     * Return the string with numbers sorted from smallest to largest
     * >>> sort_numbers('three one five')
     * 'one three five'
     * >>> sort_numbers('two one six')
     * 'one two six'
     * @param numbers a space-delimited string of numbers from 'zero' to 'nine'
     * @return the string with numbers sorted from smallest to largest
     */
    public static String sortNumbers(String numbers) {
