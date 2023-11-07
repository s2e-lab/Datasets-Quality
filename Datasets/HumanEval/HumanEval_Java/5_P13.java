import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Intersperse {
    /**
     * Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
     * >>> intersperse([], 4)
     * []
     * >>> intersperse([1, 2, 3], 4)
     * [1, 4, 2, 4, 3]
     * @param a list of numbers
     * @return a list where a delimeter is inserted between every two consecutive elements of the input list
     *
     */
    public static List<Object> intersperse(List<Object> numbers, int delimeter) {
