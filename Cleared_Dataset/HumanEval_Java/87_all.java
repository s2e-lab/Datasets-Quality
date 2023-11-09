import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class GetRow {
    /**
     * * You are given a 2 dimensional data, as a nested list,
     * which is similar to matrix, however, unlike matrices,
     * each row may contain a different number of columns.
     * Given lst, and integer x, find integers x in the list. If the occurences of 
     * x is marked by x1,x2 and so on, return list of tuples, [(x1, y1), (x2, y2) ...] such that
     * each tuple is a coordinate - (row, columns), starting with 0.
     * Sort coordinates initially by rows in ascending order.
     * Also, sort coordinates of the row by columns in descending order.
     * 
     * Examples:
     * get_row([
     *   [1,2,3,4,5,6],
     *   [1,2,3,4,1,6],
     *   [1,2,3,4,5,1]
     * ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
     * get_row([], 1) == []
     * get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
     * 
     * @param lst a list of integers
     * @param x an integer 
     * @return list of tuples such that for every time x is found in lst(x1,x2,...), a tuple is inserted in the list.
     * In [(x1, y1), (x2, y2) ...] ,each tuple is a coordinate - (row, columns), starting with 0.
     *
     */
    public static List<Object> getRow(List<Integer> lst, int x) {
