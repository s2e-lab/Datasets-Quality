import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class DoubleTheDifference {
    /**
     * * Given a list of numbers, return the sum of squares of the numbers
     * in the list that are odd. Ignore numbers that are negative or not integers.
     * 
     * double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
     * double_the_difference([-1, -2, 0]) == 0
     * double_the_difference([9, -2]) == 81
     * double_the_difference([0]) == 0  
   
     * If the input list is empty, return 0.
     *
     * @param lst a list of numbers
     * @return the sum of squares of the numbers, in the list that are odd ignoring numbers that are negative or not integers
     */
    public static int doubleTheDifference(List<Object> lst) {
