import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Unique {
    /**
     * Return sorted unique elements in a list
     * >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
     * [0, 2, 3, 5, 9, 123]
     * >>> unique([3, 8, 8, 1, 2])
     * [1, 2, 3, 8]
     * @param l a list of integers
     * @return a list that has sorted unique elements of l
     */
    public static List<Integer> unique(List<Integer> l) {
