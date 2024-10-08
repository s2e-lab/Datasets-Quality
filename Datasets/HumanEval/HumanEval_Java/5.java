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
     *
     */
    public static List<Object> intersperse(List<Object> numbers, int delimeter) {
