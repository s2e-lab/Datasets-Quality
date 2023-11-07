import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class ProdSigns {
    /**
     * * You are given an array arr of integers and you need to return
     * sum of magnitudes of integers multiplied by product of all signs
     * of each number in the array, represented by 1, -1 or 0.
     * Note: return null for empty arr.

     * Example:
     * >>> prod_signs([1, 2, 2, -4]) == -9
     * >>> prod_signs([0, 1]) == 0
     * >>> prod_signs([]) == None
     *
     */
    public static Integer prodSigns(List<Integer> arr) {
