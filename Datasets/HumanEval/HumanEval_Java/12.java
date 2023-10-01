import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Longest {
    /**
     * Out of list of strings, return the longest one. Return the first one in case of multiple
     * strings of the same length. Return null in case the input list is empty.
     * >>> longest([])

     * >>> longest(['a', 'b', 'c'])
     * 'a'
     * >>> longest(['a', 'bb', 'ccc'])
     * 'ccc'
     *
     */
    public static String longest(List<Object> strings) {
